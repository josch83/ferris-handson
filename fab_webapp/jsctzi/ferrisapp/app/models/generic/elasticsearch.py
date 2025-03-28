import logging
from copy import deepcopy

from ferris_cli.v2 import ApplicationConfigurator
from flask_appbuilder.models.filters import BaseFilterConverter, FilterRelation
from flask_appbuilder.models.generic.filters import *
from flask_appbuilder.models.generic.filters import BaseFilter
from flask_babel import lazy_gettext

from . import FerrisGenericInterface, FerrisGenericSession

conf = ApplicationConfigurator.get()
es_limit = conf.get("ES_RESULT_LIMIT", 10000)


class ElasticSearchGenericSession(FerrisGenericSession):
    """
    Implementation of FerrisGenericSession that supports Elasticsearch
    """

    sort_column = None

    base_query = {
        "bool": {
            "must": [],
            "must_not": [],
        }
    }

    model = None
    elastic_service = None

    def limit(self, page_size=25):
        self._limit = page_size
        return self

    def get(self, pk):
        return None

    def all(self):
        """
        Overriden so it returns proper data and count based on ES query
        :return:
        """
        items = list()
        total_length = 0
        try:
            self.delete_all(self.model)
            print("printin query", flush=True)
            print(self.base_query, flush=True)

            count = self.elastic_service.count(query=deepcopy(self.base_query))
            if count > 0:
                if self.sort_column:
                    data = self.elastic_service.get_all(
                        offset=self._offset,
                        count=self._limit,
                        query=deepcopy(self.base_query),
                        sort_column=self.sort_column,
                    )
                else:
                    data = self.elastic_service.get_all(
                        offset=self._offset, count=self._limit, query=deepcopy(self.base_query)
                    )
                for d in data:
                    self._add_object(d)

                items = self.store.get(self.query_class)
                total_length = count if count < es_limit else es_limit

            return total_length, items

        except Exception as e:
            logging.getLogger("ferris.modules.logs").exception(e)

        finally:
            self.base_query = {
                "bool": {
                    "must": [],
                    "must_not": [],
                }
            }

        return total_length, items

    def _add_object(self, d):
        raise NotImplementedError

    def _add(self, model):
        model_cls_name = model._name
        cls_list = self.store.get(model_cls_name)

        if not cls_list:
            self.store[model_cls_name] = []

        self.store[model_cls_name].append(model)


class ElasticFilterContains(BaseFilter):
    name = lazy_gettext("Contains")

    def apply(self, query, value):
        column_name = "_id" if self.column_name == "id" else self.column_name

        query.base_query["bool"]["must"].append({"wildcard": {column_name: f"*{value}*"}})

        return query


class ElasticFilterDoesntContain(BaseFilter):
    name = lazy_gettext("Doesn't Contain")

    def apply(self, query, value):
        column_name = "_id" if self.column_name == "id" else self.column_name

        query.base_query["bool"]["must_not"].append({"term": {column_name: value}})

        return query


class ElasticFilterEqual(FilterEqual):
    name = lazy_gettext("Equal")

    def apply(self, query, value):
        column_name = "_id" if self.column_name == "id" else self.column_name

        query.base_query["bool"]["must"].append({"term": {column_name: value}})

        return query


class ElasticFilterNotEqual(BaseFilter):
    name = lazy_gettext("Not Equal")

    def apply(self, query, value):
        column_name = "_id" if self.column_name == "id" else self.column_name

        query.base_query["bool"]["must_not"] = {"term": {column_name: value}}

        return query


class ElasticFilterRelationOneToManyEqual(FilterRelation):
    name = "Relation"
    arg_name = "rel_o_m"

    def apply(self, query, value):
        query.base_query["bool"]["must"].append({"match": {self.column_name: value}})

        return query


class ElasticGenericFilterConverter(BaseFilterConverter):
    """
    Class for converting columns into a supported list of filters
    specific for ElasticSearch.

    """

    conversion_table = (
        ("is_enum", [ElasticFilterEqual, FilterNotEqual]),
        ("is_id", [ElasticFilterEqual]),
        (
            "is_text",
            [
                ElasticFilterContains,
                FilterIContains,
                FilterNotContains,
                ElasticFilterEqual,
                FilterNotEqual,
                FilterStartsWith,
            ],
        ),
        (
            "is_string",
            [
                ElasticFilterContains,
                ElasticFilterDoesntContain,
                ElasticFilterEqual,
                ElasticFilterNotEqual,
            ],
        ),
        ("is_integer", [ElasticFilterEqual, FilterNotEqual, FilterGreater, FilterSmaller]),
        ("is_date", [ElasticFilterEqual, FilterNotEqual, FilterGreater, FilterSmaller]),
    )


class ElasticSearchGenericInterface(FerrisGenericInterface):
    filter_converter_class = ElasticGenericFilterConverter

    def __init__(self, obj, session=None):
        self.session = session

        self.FilterContains = ElasticFilterContains
        self.FilterRelationOneToManyEqual = ElasticFilterRelationOneToManyEqual

        self.obj = obj

    def is_id(self, col_name):
        return True if col_name == "id" else False
