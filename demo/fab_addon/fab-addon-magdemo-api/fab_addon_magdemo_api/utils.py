# pylint: disable=not-callable
# File auto generated, DO NOT edit because it will be smashed
import datetime
import importlib
import inspect
import logging
import ssl
import certifi
import os
import re
from typing import Any, Optional, Type
import requests
import jwt

from flask import g, session
from flask_appbuilder.models.generic.filters import (
    BaseFilter,
    BaseFilterConverter,
    FilterContains,
    FilterEqual,
    FilterGreater,
    FilterIContains,
    FilterNotContains,
    FilterNotEqual,
    FilterSmaller,
    FilterStartsWith,
)
from flask_appbuilder._compat import as_unicode
from flask_babel import lazy_gettext
from ferris_cli.v2 import FerrisLogging
#from logstash_formatter import LogstashFormatterV1
#from ferris_cli.ferris_cli import FerrisKafkaLoggingHandler

from ferrisapp.app.models.generic import (
    FerrisGenericModel,
    FerrisGenericColumn,
    FerrisGenericSession,
    FerrisGenericInterface,
    FilterRelationManyToManyEqual,
    FilterRelationOneToManyEqual,
)
from ferrisapp.app import get_appbuilder
from .services.service_factory import (
    ServiceFactory,
    AddressService,
    UserAccountService,
    RoleRightsService,
    services_available,
)
from .custom_utils import *


READ_ONLY_FIELDS = ["changed_by", "changed_on", "created_by", "created_on"]


def remove_prefix(text, prefix):
    if text.startswith(prefix):  # only modify the text if it starts with the prefix
        text = text.replace(prefix, "", 1)  # remove one instance of prefix
    return text


def q_points_render(question_points: int) -> str:
    return str(question_points) if (question_points and question_points > 0) else ""


def datetime_render(datetime_object) -> str:
    return datetime_object.strftime("%Y-%m-%d %H:%M:%S %Z") if datetime_object else ""


def datetime_render_v2(datetime_object) -> str:
    return datetime_object.strftime("%Y-%m-%d %H:%M:%S.%f%z") if datetime_object else ""


def date_render(date_object) -> str:
    return date_object.strftime("%Y-%m-%d") if date_object else ""


def reply_to_post_id_render(post_id) -> str:
    if post_id is not None and post_id != "None" and post_id != "":
        return post_id
    return ""


def last_name_render(surname) -> str:
    if surname is not None and surname != "None" and surname != "":
        return surname
    return ""


def file_struct_render(file_obj: dict) -> str:
    if file_obj:
        buck = file_obj.get("bucket", None)
        file_name = file_obj.get("filepath", None)

        return "/".join([buck, file_name])
    return ""


def render_audio(url_audio) -> str:
    if url_audio.startswith("https"):
        return f"""<audio controls src="{url_audio}">
                Your browser does not support the audio tag.
            </audio>"""
    return ""


def render_image(url_sign) -> str:
    if url_sign.startswith("https"):
        return f'<img src="{url_sign}" style="width: 15%; height: 15%">'
    return ""


def render_video(url_video) -> str:
    if url_video.startswith("https"):
        return f"""<video width="320" height="240" controls src="{url_video}">
                Your browser does not support the video tag.
            </video>"""
    return ""


def forum_status_render(forum_status) -> str:
    if forum_status is not None and forum_status != "":
        if forum_status == "active":
            return f"""<b style='color:green;'>{forum_status.capitalize()}</b>"""
        if forum_status == "blocked":
            return f"""<b style='color:red;'>{forum_status.capitalize()}</b>"""
        if forum_status == "archived":
            return f"""<b style='color:grey;'>{forum_status.capitalize()}</b>"""
        if forum_status == "flagged":
            return f"""<b style='color:orange;'>{forum_status.capitalize()}</b>"""
    return ""


def remove_read_only_fields(input_dictionary: dict) -> dict:
    for field in READ_ONLY_FIELDS:
        input_dictionary.pop(field, None)
    return input_dictionary


def clean_empty_fields(fields_object: (dict | list)) -> (dict | list):
    if isinstance(fields_object, dict):
        return {
            k: v
            for k, v in ((k, clean_empty_fields(v)) for k, v in fields_object.items())
            if v or v == 0
        }
    if isinstance(fields_object, list):
        return [v for v in map(clean_empty_fields, fields_object) if v or v == 0]
    return fields_object


def remove_non_filled_fields(obj: object) -> object:
    # Remove empty fields before forwarding the request to the API
    # Should handle nested empty fields if any. Not fully tested on any object
    class_item = obj.__class__
    dictionary = obj.to_dict()
    empty_keys = []
    all_keys = set(dictionary.keys())
    for key, value in dictionary.items():
        if value is None or value == "":
            empty_keys.append(key)
    empty = set(empty_keys)
    available_keys = all_keys - empty
    obj_new = {}
    for keys in list(available_keys):
        obj_new[keys] = dictionary[keys]

    return class_item(**obj_new)


def create_logger(name):
    """Create a logger that will write the log to elastic search using logstash format
    :param name: the name of the logger
    :return: a logger
    """
    logger = FerrisLogging().get_logger(name=name, use_colors=True)
    return logger


#def create_logger(name):
#    """Create a logger that will write the log to elastic search using logstash format
#    :param name: the name of the logger
#    :return: a logger
#    """
#    logger = logging.getLogger(name)
#
#    kafka_logging_handler = FerrisKafkaLoggingHandler()
#    formatter = LogstashFormatterV1()
#    kafka_logging_handler.setFormatter(formatter)
#    logger.setLevel(logging.DEBUG)
#    logger.addHandler(kafka_logging_handler)
#    return logger


def get_partner_id() -> int:
    # current_user_id = g.user.id
    user_id = 0  # right now the only one
    return user_id


def get_user_roles():
    current_user_email = g.user.email
    app_builder = get_appbuilder()
    if (
        app_builder.app.config.get("WEBAPP_ADDRESS").startswith("http://localhost")
        or "gkg-freiburg" not in current_user_email
    ):  # only for dev
        user_roles = ["admin", "expert"]
    else:
        user_roles = [r.name for r in g.user.roles]
    return user_roles


def get_access_token():

    app_builder = get_appbuilder()

    if app_builder.app.config.get('API_DATA_MODEL_SECURITY').lower() == "false":
        final_token = g.user.email
    else:
        
        temp_token = app_builder.sm.oauth_tokengetter()[0]
        refresh_token = app_builder.sm.oauth_tokengetter()[2]
        header_data = jwt.get_unverified_header(temp_token)
        
        for oauth_provider in app_builder.sm.oauth_providers:
                
            keycloak_client_id = oauth_provider["remote_app"]["client_id"]
            keycloak_client_secret = oauth_provider["remote_app"]["client_secret"]
            token_url = oauth_provider["remote_app"]["access_token_url"]
            certs = oauth_provider["remote_app"]["jwks_uri"]
            issuer = "/".join(token_url.split("/")[:token_url.split("/").index("protocol")])

        # Retrieve available endpoints from available OpenID config
        certs_url = certs
        ctx = ssl.create_default_context()
        ctx.load_verify_locations(cafile=certifi.where())
        #ctx.load_verify_locations(cafile="certs/fx-bundle.crt")
        
        jwks_client = jwt.PyJWKClient(certs_url, ssl_context=ctx)
        signing_key = jwks_client.get_signing_key_from_jwt(temp_token)
        issuers = [issuer]

        options = {
            'verify_signature': True,
            'verify_iss': True,
            'verify_exp': True,
            'verify_nbf': True,
            'verify_iat': True,
            'verify_aud': False,
            'require_exp': True,
            'require_iat': True,
            'require_nbf': True,
            'require_iss': True
        }

        try:
            payload = jwt.decode(temp_token, signing_key.key,
                                 algorithms=[header_data['alg'], ], issuer=issuers, options=options
                                 )
        except jwt.ExpiredSignatureError:
            # Signature has expired/ token not valid anymore, what should we return in this case?
            print("Expired token!", flush=True)
            print("Let's fetch new token using refresh token!", flush=True)
                
            for oauth_provider in app_builder.sm.oauth_providers:
                
                keycloak_client_id = oauth_provider["remote_app"]["client_id"]
                keycloak_client_secret = oauth_provider["remote_app"]["client_secret"]
                token_url = oauth_provider["remote_app"]["access_token_url"]

            header_token = {"Content-Type": "application/x-www-form-urlencoded"}

            data_token_payload = {
                    "client_id": keycloak_client_id,
                    "grant_type": "refresh_token",
                    "client_secret": keycloak_client_secret,
                    "scope": "openid",
                    "refresh_token": refresh_token,
            }
            #token_url = "http://fx-keycloak.core/realms/ferris/protocol/openid-connect/token"   # for testing
            token_request = requests.post(token_url, data=data_token_payload, headers=header_token)
            #token_request = app_builder.sm.oauth.keycloak.post("token", data=data_token_payload, headers=header_token)
            #print(f"Token request: {token_request}", flush=True)
            access_token = token_request.json()["access_token"]
            new_refresh_token = token_request.json()["refresh_token"]
            
            final_token = access_token

            session["oauth"] = (
                access_token,
                "",
                new_refresh_token,
            )
            #oatoken = app_builder.sm.oauth.keycloak.fetch_access_token(refresh_token=refresh_token, grant_type="refresh_token")
            #oatoken = app_builder.sm.oauth.keycloak.refresh_token(refresh_token=refresh_token, token_endpoint=)
            #print(f"Response from fetch_access_token(): {oatoken}", flush=True)
            #final_token = oatoken
        else:
            print(f"Access token not expired!", flush=True)
            final_token = temp_token
    
    return final_token


def dict_to_str(list_dict: list[dict]) -> str:
    if list_dict and len(list_dict) > 0:
        return ",".join(["/".join([d["bucket"], d["filepath"]]) for d in list_dict])
    return ""


class FilterEnumEqual(BaseFilter):
    name = lazy_gettext("Equal enum to")

    def apply(self, query, value):
        return query.equal(self.column_name, value)


class FilterEndsWith(BaseFilter):
    name = lazy_gettext("Ends with (Case insensitive)")

    def apply(self, query, value):
        return query.ends_with(self.column_name, value)


class MAGDEMOFilterConverter(BaseFilterConverter):
    """
    Class for converting columns into a supported list of filters
    specific for SQLAlchemy.
    """

    conversion_table = (
        (
            "is_relation_many_to_one",
            [FilterRelationOneToManyEqual],
        ),
        (
            "is_relation_one_to_one",
            [FilterRelationOneToManyEqual],
        ),
        ("is_relation_many_to_many", [FilterRelationManyToManyEqual]),
        ("is_relation_one_to_many", [FilterRelationOneToManyEqual]),
        ("is_enum", [FilterEqual, FilterNotEqual]),
        (
            "is_text",
            [
                FilterContains,
                FilterIContains,
                FilterNotContains,
                FilterEqual,
                FilterNotEqual,
                FilterStartsWith,
                FilterEndsWith,
            ],
        ),
        (
            "is_string",
            [
                FilterContains,
                FilterIContains,
                FilterNotContains,
                FilterEqual,
                FilterNotEqual,
                FilterStartsWith,
                FilterEndsWith,
            ],
        ),
        ("is_integer", [FilterEqual, FilterNotEqual, FilterGreater, FilterSmaller]),
        ("is_date", [FilterEqual, FilterNotEqual, FilterGreater, FilterSmaller]),
        ("is_float", [FilterEqual, FilterNotEqual, FilterGreater, FilterSmaller]),
        ("is_boolean", [FilterEqual, FilterNotEqual]),
        ("is_datetime", [FilterEqual, FilterNotEqual, FilterGreater, FilterSmaller]),
    )


def convert_to_snake_case(original_string):
    """
    Convert string into snake case.
    Join punctuation with underscore
    Args:
        string: String to convert.
    Returns:
        string: Snake cased string.
    """
    string = re.sub(r"[\-\.\s]", "_", str(original_string))
    if not string:
        return string
    return str(string[0]).lower() + re.sub(
        r"[A-Z]", lambda matched: "_" + str(matched.group(0)).lower(), string[1:]
    )


class MAGDEMOGenericSession(FerrisGenericSession):
    def __init__(self, model: Optional[Type] = None, service: Optional[Type] = None, logger_var: logging.Logger = None) -> None:
        super().__init__()
        if model is None:
            raise TypeError(
                "model shouldn't be None! It should be the name of one of your generic models"
            )

        if service is None:
            raise TypeError(
                "service shouldn't be None! It should be the name of one of your services"
            )

        if logger_var is None:
            raise TypeError("logger_var shouldn't be None!")

        self._model = model
        self._service = service
        self._logger_var = logger_var

    @property
    def model(self):
        return self._model

    def service(self, **kwargs):  # caters for either using the service factory or just the class service name
        if inspect.isclass(self._service):
            return self._service(**kwargs)
        return None

    @property
    def logger_var(self):
        return self._logger_var

    def extract_endpoint_name(self) -> str:
        return "".join(
            "_" + x if x.isupper() and index > 0 else x
            for index, x in enumerate(self.model.__name__[:-5])
        ).lower()

    def query(self, model_cls):
        """
        SQLAlchemy query like method
        """
        self._filters_cmd = []
        self.query_filters = []
        self._order_by_cmd = None
        self._offset = 0  # Our api wants 1...
        self._limit = 0
        self.query_class = model_cls._name
        return self

    def offset(self, offset=0):
        self._offset = offset
        return self

    def limit(self, page_size=25):
        self._limit = page_size
        return self

    def starts_with(self, col_name, value):
        value_forwarded = value + "%"
        self._filters_cmd.append((self._starts_with, col_name, value_forwarded))
        return self

    def ends_with(self, col_name, value):
        modified_col_name = "ilike_" + col_name
        value_forwarded = "%" + value
        self._filters_cmd.append((self._ilike, modified_col_name, value_forwarded))
        return self

    def greater(self, col_name, value):
        modified_col_name = "gte_" + col_name
        self._filters_cmd.append((self._greater, modified_col_name, value))
        return self

    def smaller(self, col_name, value):
        modified_col_name = "lte_" + col_name
        self._filters_cmd.append((self._smaller, modified_col_name, value))
        return self

    def equal(self, col_name, value):
        modified_col_name = "equal_" + col_name
        self._filters_cmd.append((self._equal, modified_col_name, value))
        return self

    def not_equal(self, col_name, value):
        modified_col_name = "not_" + col_name
        self._filters_cmd.append((self._not_equal, modified_col_name, value))
        return self

    def like(self, col_name, value):
        value_forwarded = "%" + value + "%"
        self._filters_cmd.append((self._like, col_name, value_forwarded))
        return self

    def not_like(self, col_name, value):
        modified_col_name = "not_" + col_name
        value_forwarded = "%" + value + "%"
        self._filters_cmd.append((self._not_like, modified_col_name, value_forwarded))
        return self

    def ilike(self, col_name, value):
        modified_col_name = "ilike_" + col_name
        value_forwarded = "%" + value + "%"
        self._filters_cmd.append((self._ilike, modified_col_name, value_forwarded))
        return self

    def contains_related_item(self, col_name, value):
        modified_col_name = "in_list_" + col_name
        self._filters_cmd.append(
            (self._contains_related_item, modified_col_name, value)
        )
        return self

    def _contains_related_item(self, item, col_name, value):
        # it doesn't matter, is not used because is not send in the request to the api
        return False

    

    

    def _add_object(self, dictionary):
        model = self.model(**dictionary)
        self._add(model)

    def _add(self, model):
        model_cls_name = model._name
        cls_list = self.store.get(model_cls_name)

        if not cls_list:
            self.store[model_cls_name] = []

        self.store[model_cls_name].append(model)


class MAGDEMOGenericColumn(FerrisGenericColumn):
    """
    Extended Ferris Generic column to support enum string columns
    """

    def __init__(
        self,
        col_type,
        primary_key=False,
        unique=False,
        nullable=False,
        foreign_key=None,
        foreign_key_class=None,
        relationship_type=None,
        read_only_fk=True,
        is_enum=False,
    ):
        """
        :param col_type: Type of the column (str, int, date...)
        :param primary_key: True if column represents primary key
        :param unique: True if the column must have unique value
        :param nullable: True if column value can be None
        :param foreign_key: True if column represents "foreign key"
        :param foreign_key_class: name of the model class of foreign key
        :param relationship_type: Type of the relationship
                                    (FerrisGenericRelationshipType.MANY_TO_ONE,
                                    FerrisGenericRelationshipType.MANY_TO_MANY,
                                    FerrisGenericRelationshipType.ONE_TO_ONE)
        :param read_only_fk: True if object cannot be modified when rendered as related view
        :param is_enum: False if object should be rendered/filtered as enum
        """

        self.is_enum = is_enum

        super().__init__(
            col_type,
            primary_key,
            unique,
            nullable,
            foreign_key,
            foreign_key_class,
            relationship_type,
            read_only_fk,
        )


class MAGDEMOGenericInterface(FerrisGenericInterface):

    filter_converter_class = MAGDEMOFilterConverter

    def __init__(
        self, model, session=None, service=None, logger_var=None
    ) -> None:  # instead of model can use object
        super().__init__(model, session)
        if model is None:
            raise TypeError(
                "model shouldn't be None! It should be the name of one of your generic models"
            )

        if service is None:
            raise TypeError(
                "service shouldn't be None! It should be the name of one of your services"
            )

        if logger_var is None:
            raise TypeError("logger_var shouldn't be None!")

        self.message = ""

        self._model = model
        self._service = service
        self._logger_var = logger_var

    def is_string(self, col_name):
        return (
            self.obj.properties[col_name].col_type == str
            and not self.obj.properties[col_name].is_enum
        )

    def is_float(self, col_name):
        return self.obj.properties[col_name].col_type == float

    def is_boolean(self, col_name):
        return self.obj.properties[col_name].col_type == bool

    def is_date(self, col_name: str) -> bool:
        return self.obj.properties[col_name].col_type == datetime.date

    def is_datetime(self, col_name: str) -> bool:
        return self.obj.properties[col_name].col_type == datetime.datetime

    def get_related_interface(self, col_name: str):
        return self.__class__(self.get_related_model(col_name), self.session)

    def get_related_model(self, col_name: str) -> Type[FerrisGenericModel]:
        class_string_name = self.obj.properties[col_name].foreign_key_class

        mod_name = (
            f"fab_addon_magdemo_api.models.{convert_to_snake_case(class_string_name[:-5])}"
        )
        module = importlib.import_module(mod_name)
        class_ = getattr(module, class_string_name)
        return class_

    def get_related_obj(
        self, col_name: str, value: Any
    ) -> Optional[Type[FerrisGenericModel]]:
        rel_model = self.get_related_model(col_name)
        if self.session:
            return self.session.query(rel_model).get(value)
        return None

    def is_enum(self, col_name: str) -> bool:
        return (
            self.obj.properties[col_name].col_type == str
            and self.obj.properties[col_name].is_enum
        )

    @property
    def model(self):
        return self._model

    def service(self, **kwargs):  # caters for either using the service factory or just the class service name
        if inspect.isclass(self._service):
            return self._service(**kwargs)
        return None

    @property
    def logger_var(self):
        return self._logger_var

    def extract_endpoint_name(self) -> str:
        ### NOTE: It assumes a model name of the form {EntityImportant}Model and gets translated to --> entity_important
        return "".join(
            "_" + x if x.isupper() and index > 0 else x
            for index, x in enumerate(self.model.__name__[:-5])
        ).lower()

    
def generate_dropdowns(service_chosen: services_available, **filters):
    service_instance = ServiceFactory(service=service_chosen)
    # access token to send to API
    access_token = get_access_token()
    returned_items = service_instance(access_token).get_all_dropdowns(**filters)
    if returned_items and len(returned_items) > 0:
        return [(item.get("id"), item.get("name")) for item in returned_items]  # how to generalize to a certain pk and display name?

    return []


def add_html_underline(href) -> str:
    return f'{href} style="text-decoration: underline;"'

