import os

from flask_appbuilder.filemanager import (
    FileManager,
    get_file_original_name,
    uuid_namegen,
)
from flask_appbuilder.upload import FileUploadField
from markupsafe import Markup
from minio import Minio
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from wtforms.widgets import html_params

try:
    from wtforms.fields.core import _unset_value as unset_value
except ImportError:
    from wtforms.utils import unset_value


class MinioFileUploadFieldWidget:
    empty_template = """
        <div class="input-group">
        <span class="input-group-addon"><i class="fa fa-upload"></i>
        </span>
        <input class="form-control" %(file)s/>
        </div>
        """

    data_template = """
        <div>
        <input %(text)s>
        <input type="checkbox" name="%(marker)s">Delete</input>
        </div>
        <div class="input-group">
        <span class="input-group-addon"><i class="fa fa-upload"></i>
        </span>
        <input class="form-control" %(file)s/>
        </div>
        """

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        kwargs.setdefault("name", field.name)

        template = self.data_template if field.data else self.empty_template
        templ = Markup(
            template
            % {
                "text": html_params(type="text", readonly="readonly", value=field.data),
                "file": html_params(type="file", **kwargs),
                "marker": f"_{field.name}-delete",
            }
        )
        print(f"Print template: {templ}", flush=True)
        return templ


# 'text="something"'


class MinioFileUploadField(FileUploadField):
    """File upload field for Minio"""

    widget = MinioFileUploadFieldWidget()

    def __init__(self, label=None, validators=None, filemanager=None, **kwargs):
        """
        Constructor.

        :param label:
            Display label
        :param validators:
            Validators
        """
        super().__init__(label, validators, **kwargs)

        if filemanager is not None:
            self.filemanager = filemanager
        else:
            self.filemanager = FileManager()
        self.data = None
        self._should_delete = False
        self._preexisting_file = {"exist": False, "filepath": None}

    def _is_uploaded_file(self, data):
        return data and isinstance(data, FileStorage) and data.filename

    def process(self, formdata, data=unset_value):
        if formdata:
            print(f"Print field formdata: {formdata}", flush=True)
            if f"_{self.name}-delete" in formdata:
                self._should_delete = True

        return super().process(formdata, data)

    def process_formdata(self, valuelist):
        if self._should_delete:
            self.data = None
        elif valuelist:
            data = valuelist[0]

            if self._is_uploaded_file(data):
                self.data = data

    def populate_obj(self, obj, name):
        if getattr(obj, name, None):
            # If field should be deleted, clean it up
            if self._should_delete:
                setattr(obj, name, None)
                return

        if self._is_uploaded_file(self.data):
            filename = self.filemanager.generate_name(self.data)
            # update filename of FileStorage to our validated name
            self.data.filename = filename

            setattr(obj, name, filename)


class MinioFileManager(FileManager):
    """File upload to Minio"""

    def __init__(
        self,
        bucket_name=None,
        relative_path="",  # is the prefix
        namegen=None,
        allowed_extensions=None,
        **kwargs,
    ):
        from ferrisapp.app import get_appbuilder

        ctx = get_appbuilder()

        if (minio_access_key := "MINIO_ACCESS_KEY") in ctx.app.config:
            self.minio_access_key = ctx.app.config[minio_access_key]
        else:
            raise KeyError(f"Config key {minio_access_key} is mandatory")
        if (minio_secret_key := "MINIO_SECRET_KEY") in ctx.app.config:
            self.minio_secret_key = ctx.app.config[minio_secret_key]
        else:
            raise KeyError(f"Config key {minio_secret_key} is mandatory")

        # @TODO: generalize bucket var name or take it as input from cookiecutter! Check if needs to be quoted...
        if (minio_working_bucket := "random") in ctx.app.config and not bucket_name:
            bucket_name = ctx.app.config[minio_working_bucket]
        if not bucket_name:
            raise KeyError(f"Config key {minio_working_bucket} is mandatory")

        self.bucket_name = bucket_name
        self.relative_path = relative_path
        self.namegen = namegen or uuid_namegen
        # if not allowed_extensions and 'FILE_ALLOWED_EXTENSIONS' in ctx.app.config:
        #     self.allowed_extensions = ctx.app.config['FILE_ALLOWED_EXTENSIONS']
        # else:
        self.allowed_extensions = allowed_extensions
        self._should_delete = False

    def get_minio_client(self):
        # @TODO: pass the secure False/True param, do not fix it!
        secure_connection = True if self.ctx.app.config["MINIO_SECURE_CONNECTION"] == "true" else False
        minio_client = Minio(
            self.ctx.app.config["MINIO_HOST"],  # get thourgh config  self.ctx.app.config["MINIO_HOST"]
            access_key=self.minio_access_key,
            secret_key=self.minio_secret_key,
            secure=secure_connection,
        )

        return minio_client

    def delete_file(self, filename):
        client = self.get_minio_client()
        file_path = os.path.join(self.relative_path, filename)
        client.remove_object(self.bucket_name, file_path)

    def save_file(self, data, filename):
        client = self.get_minio_client()
        sec_filename = secure_filename(filename)
        file_path = os.path.join(self.relative_path, sec_filename)
        size = os.fstat(data.fileno()).st_size
        client.put_object(self.bucket_name, file_path, data, size)

        return sec_filename

    def file_exists(self, filename):
        client = self.get_minio_client()
        # orig_filename = get_file_original_name(filename)
        orig_filename = filename
        file_path = os.path.join(self.relative_path, orig_filename)
        try:
            client.stat_object(self.bucket_name, file_path)
        except:  # most probably not found
            return False

        return True

    def get_file(self, filename):
        client = self.get_minio_client()
        orig_filename = get_file_original_name(filename)
        file_path = os.path.join(self.relative_path, orig_filename)
        response = client.get_object(self.bucket_name, file_path)
        body = response["Body"]
        return body

    def is_file_allowed(self, filename):
        if not self.allowed_extensions:
            return True
        dot = "."
        return dot in filename and filename.rsplit(dot, 1)[1].lower() in self.allowed_extensions

    def generate_name(self, file_data):
        return self.namegen(file_data)
