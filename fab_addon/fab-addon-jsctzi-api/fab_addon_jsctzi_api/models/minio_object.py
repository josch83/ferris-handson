import datetime
import mimetypes
import os

from ferris_cli.v2 import ApplicationConfigurator, FerrisEvents
from ferrisapp.app.models.generic import (
    FerrisGenericColumn,
    FerrisGenericInterface,
    FerrisGenericModel,
    FerrisGenericRelationshipType,
    FerrisGenericSession,
)
from flask import Markup, current_app, url_for
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.models.generic import GenericColumn

from ..services.minio_ferris_service import StorageService


class MinioObjectModel(FerrisGenericModel):
    file = GenericColumn(str, nullable=False, primary_key=True)
    br_id = FerrisGenericColumn(
        int,
        foreign_key=True,
        foreign_key_class="BusinessRelationshipModel",
        relationship_type=FerrisGenericRelationshipType.MANY_TO_ONE,
    )
    bucket_name = GenericColumn(str)
    prefix = GenericColumn(str)
    last_modified = FerrisGenericColumn(datetime.datetime)
    uploaded_by = FerrisGenericColumn(int)
    created_on = FerrisGenericColumn(datetime.datetime)
    description = FerrisGenericColumn(str)
    minio_service = StorageService()

    def __repr__(self):
        return self.file_name

    def to_dict(self):
        return {"file_name": self.file, "file": self.prefix + "/" + self.file}

    def prepare_for_add(self) -> tuple[dict, dict]:
        data = {
            "file": self.file,
            "prefix": self.prefix,
            "bucket_name": self.bucket_name,
        }
        user_metadata = {
            "Uploadedby": self.uploaded_by,
            "Createdon": str(self.created_on.strftime("%Y-%m-%d %H:%M:%S %Z")),
            "Description": self.description,
        }
        return data, user_metadata

    def download(self):
        filename = self.prefix + "/" + self.file
        return Markup(
            '<a href="'
            + url_for(
                "MinioObjectViewImplCompliance.download",
                bucketname=self.bucket_name,
                filename=filename,
            )
            + """
                " class="btn btn-sm btn-info" data-toggle="tooltip" rel="tooltip" title="Download File">
                <i class ="fa fa-download" ></i> Download</a>
            """
        )


class MinioObjectSession(FerrisGenericSession):
    def __init__(self, bucket_name) -> None:
        super().__init__()
        self.bucket_name = bucket_name

    model = MinioObjectModel
    minio_service = StorageService()

    def all(self):
        print("Print filters:")
        print(self._filters_cmd)

        search_criteria_dict = {filter_cmd[1]: filter_cmd[2] for filter_cmd in self._filters_cmd}
        print(search_criteria_dict, flush=True)

        external_reference = ""  # Adapt to work with all the projects. The previous code worked only for GkG.
        self.delete_all(self.model())

        data = self.minio_service.get_objects_from_bucktes(bucket_name=self.bucket_name, prefix=external_reference)

        for data_object in data:
            data_object["br_id"] = search_criteria_dict["br_id"]
            print(f"Single object: {data_object}", flush=True)
            print(
                f"Adding object where name is split: {data_object['_object_name'].split('/')}",
                flush=True,
            )

            self._add_object(data_object)

        return super().all()

    def _add_object(self, object_data):
        object_name = object_data["_object_name"]
        parts = object_name.split("/")
        extracted_prefix = parts[0]
        extracted_file = "/".join(parts[1:])
        max_parts = 2
        file_content_type = mimetypes.MimeTypes().guess_type(parts[-1] if len(parts) > max_parts else extracted_file)[0]
        print(f"File content type: {file_content_type}", flush=True)

        metadata = object_data["_metadata"]
        print(f"User metadata retrieved: {metadata}", flush=True)

        description = metadata.get("X-Amz-Meta-Description", "")

        uploaded_by = None
        for key in (
            "X-Amz-Meta-Uploadeby",
            "X-Amz-Meta-UploadedBy",
            "X-Amz-Meta-Uploadedby",
        ):
            if metadata.get(key, None):
                uploaded_by = int(metadata.get(key))
                break

        created_on = None
        for key in ("X-Amz-Meta-Createdon", "X-Amz-Meta-CreatedOn"):
            if metadata.get(key, None):
                created_on = datetime.datetime.strptime(metadata.get(key), "%Y-%m-%d %H:%M:%S %Z")
                break

        print(f"Prefix: {extracted_prefix}", flush=True)
        print(f"Filename: {extracted_file}", flush=True)

        if object_data["_bucket_name"] not in current_app.config.get("MINIO_SKIP_BUCKETS", []):
            model = self.model(
                br_id=object_data["br_id"],
                file=extracted_file,
                bucket_name=object_data["_bucket_name"],
                prefix=extracted_prefix,
                description=description,
                uploaded_by=uploaded_by,
                created_on=created_on,
                last_modified=object_data.get("_last_modified", None),
            )
            self._add(model)
            print("Object should have been added...", flush=True)

    def _add(self, model):
        model_cls_name = model._name

        if not self.store.get(model_cls_name):
            self.store[model_cls_name] = []

        self.store[model_cls_name].append(model)


class MinioObjectInterface(FerrisGenericInterface):
    def __init__(self):
        self.message = None

    minio_service = StorageService()

    def add(self, data: MinioObjectModel):
        data, user_metadata = data.prepare_for_add()

        print(
            f"Data dictionary submitted after add for creating object: {data}",
            flush=True,
        )
        print(
            f"User metadata dictionary submitted after add for creating object: {user_metadata}",
            flush=True,
        )
        file_name = self.minio_service.create_object_full(data, user_metadata)

        data.pop("file")
        data["file_name"] = file_name

        FerrisEvents().send(
            event_type="ferris.apps.newcent.minio.file_uploaded",
            event_source=os.environ["APP_NAME"],
            data=data,
            topic=ApplicationConfigurator.get().get("DEFAULT_TOPIC", None),
        )

        self.message = (as_unicode(self.add_row_message), "success")

        return True

    def delete(self, data: MinioObjectModel):
        data = data.__dict__
        full_filename = data["prefix"] + "/" + data["file"]
        try:
            self.minio_service.delete_object(data["bucket_name"], full_filename)
        except Exception as exception:
            self.message = (f"Delete failed! Error: {exception}", "danger")
            return True

        self.message = (as_unicode(self.delete_row_message), "success")
        return True

    def download(self):
        return True
