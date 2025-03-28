import datetime
import os
from typing import Dict, List

from ferris_cli.v2 import ApplicationConfigurator
from ferris_cli.v2.services.storage import MinioService as MS
from werkzeug.utils import secure_filename

from ..utils import create_logger

logger = create_logger(__name__)


class StorageService(MS):
    def __init__(self, entity=None):
        self.entity = entity

        super().__init__(ApplicationConfigurator.get())

    def create_object_full(self, data: Dict, user_defined_metadata: Dict):
        """This function creates an object on Minio using data about the object and
           user defined metadata.

        Args:
            data (Dict): main object data in form of a dictionary
            user_defined_metadata (Dict): user defined metadata to be added to the object in form of dictionary

        Returns:
            [str]: file name
        """
        ## One should actually add checks for the types of the arguments passed if both are dictionaries.
        ## Also we assume user metadata keys are well formed. Read Minio documentation or source code for details.

        logger.debug("Creating minio object")
        logger.debug(f"Data passed: {data}")
        logger.debug(f"Metadata passed by user: {user_defined_metadata}")

        file_object = data["file"]
        file_name = file_object.filename

        sanitize_filename = secure_filename(file_name)
        file_type = file_object.content_type
        logger.debug(f"File type before adding: {file_type}")

        bucket_name = data["bucket_name"]
        prefix = data["prefix"]

        metadata = user_defined_metadata if user_defined_metadata else None

        logger.debug(f"Metadata submitted to minio: {metadata}")

        # file_name_on_storage = self.generate_file_name(file_object.filename) if self.entity else file_object.filename
        size = os.fstat(file_object.fileno()).st_size

        prefixed_filename = f"{prefix}/{sanitize_filename}"  # should use the secure filename function?
        logger.debug(f"Prefixed name: {prefixed_filename}")

        try:
            self.service.put_object(
                bucket_name,
                prefixed_filename,
                file_object,
                size,
                content_type=file_type,
                metadata=metadata,
            )
        except Exception as exception:
            logger.exception(f"Exception trying to save the file! -> {exception}")

        return file_name  # , fhash

    def create_object(self, data):
        file_object = data["file"]
        file_name = file_object.filename
        file_type = data["file_type"]
        bucket_name = data["bucket_name"]
        self.validate_object_type(file_name, file_type)

        file_name_on_storage = self.generate_file_name(file_object.filename) if self.entity else file_object.filename
        fname, fhash = super().create_object(
            file_object,
            bucket_name,
            file_name=file_name_on_storage,
            supported_extensions=data.get("supported_extensions", None),
        )

        return fname, fhash

    def generate_file_name(self, original_file_name):
        timestamp = datetime.datetime.utcnow().strftime("%d-%m-%Y_%H:%M:%S")

        return self.entity + "_" + timestamp + "." + self.get_file_extension(original_file_name)

    @staticmethod
    def get_file_extension(original_file_name):
        return original_file_name.split(".")[-1]

    def validate_object_type(self, file_name, type_selected):
        extension = self.get_file_extension(file_name)
        type_csv_table = "CSV Table"
        expected_extension = type_selected.lower() if type_selected != type_csv_table else "csv"
        if expected_extension not in {"csv", "txt", "json"}:
            raise Exception("Invalid type selected")
        if extension != expected_extension:
            raise Exception(f"File is not {expected_extension.upper()} as selected!")

    def get_objects_from_bucktes(
        self,
        *,
        bucket_name: str = "",
        prefix: str = "",
        recurse: bool = True,
        include_metadata: bool = True,
    ) -> List[Dict]:
        """Method to retrieve objects from buckets with extra parameters

        Returns:
            [List[Dict]]: List of dictionaries where each dictionary represents an object in Minio
        """
        print(f"Bucket name requested to get_all(): {bucket_name}", flush=True)

        buckets = bucket_name if bucket_name else self.get_buckets()

        extra_keywords = {}

        if prefix:
            extra_keywords["prefix"] = prefix
        if recurse:
            extra_keywords["recursive"] = recurse
        if include_metadata:
            extra_keywords["include_user_meta"] = include_metadata
        print(f"Metadata keywords: {extra_keywords}", flush=True)

        objects_list = []

        if isinstance(buckets, list):
            for bucket in buckets:
                objects_in_bucket = self.service.list_objects(bucket["_name"], **extra_keywords)

                for obj in objects_in_bucket:
                    objects_list.append(obj.__dict__)

        elif isinstance(buckets, str):
            objects_in_bucket = self.service.list_objects(buckets, **extra_keywords)

            for obj in objects_in_bucket:
                objects_list.append(obj.__dict__)

        return objects_list
