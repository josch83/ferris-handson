from ferris_fab_minio.services.minio_ferris_service import StorageService
from ferrisapp.app.models.generic import (
    FerrisGenericInterface,
    FerrisGenericModel,
    FerrisGenericSession,
)
from flask import Markup, current_app, session, url_for
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.models.generic import GenericColumn

minio_service = StorageService()


class MinioBucketModel(FerrisGenericModel):
    bucket_name = GenericColumn(str, primary_key=True)
    objects_contained = GenericColumn(str)

    def __repr__(self):
        return self.bucket_name

    def to_dict(self):
        return {"bucket_name": self.bucket_name}

    def action(self):
        if self.objects_contained > 0:
            return Markup(
                '<a href="'
                + url_for("MinioObjectViewImplF.list", _flt_0_bucket_name=self.bucket_name)
                + """
                    class="btn btn-sm btn-info" data-toggle="tooltip" rel="tooltip" title="Show Objects"><i
                        class ="fa fa-file" ></i> Show Objects</a>
                    """
            )
        return Markup(
            """
                <a href="javascript:;" class="btn btn-sm btn-primary" data-toggle="tooltip" rel="tooltip"
                title="Show Objects" disabled="disabled"><i class ="fa fa-file" ></i> Show Objects</a>
            """
        )


class MinioBucketSession(FerrisGenericSession):
    def get(self, pk):
        data = minio_service.get_bucket_by_name(pk)

        self._add_object(data)

        return super().get(pk)

    def all(self):
        self.delete_all(MinioBucketModel())

        print(session, flush=True)

        buckets = minio_service.get_buckets()

        for bucket in buckets:
            self._add_object(bucket)

        return super().all()

    def _add_object(self, bucket):
        if bucket["_name"] not in current_app.config.get("MINIO_SKIP_BUCKETS", []):
            model = MinioBucketModel(
                bucket_name=bucket["_name"],
                objects_contained=minio_service.get_number_of_objects_in_bucket(bucket["_name"]),
            )

            self._add(model)

    def _add(self, model):
        model_cls_name = model._name

        if not self.store.get(model_cls_name):
            self.store[model_cls_name] = []

        self.store[model_cls_name].append(model)


class MinioBucketInterface(FerrisGenericInterface):
    def __init__(self):
        self.message = None

    def add(self, data):
        data = data.__dict__
        try:
            minio_service.create_bucket(data["bucket_name"])
        except Exception:
            self.message = ("Adding new bucket failed!", "danger")
            return True

        self.message = (as_unicode(self.add_row_message), "success")
        return True

    def delete(self, data):
        data = data.__dict__
        try:
            minio_service.delete_bucket(data["bucket_name"])
        except Exception:
            self.message = ("Delete failed!", "danger")
            return True

        self.message = (as_unicode(self.delete_row_message), "success")
        return True
