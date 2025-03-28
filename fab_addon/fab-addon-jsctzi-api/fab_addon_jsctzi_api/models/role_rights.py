# pylint: disable=no-member
# File auto generated, DO NOT edit because it will be smashed

import datetime

from ferrisapp.app.models.generic import (
    FerrisGenericModel,
    FerrisGenericRelationshipType,
)
from flask import g, url_for, Markup, flash
from flask_appbuilder._compat import as_unicode
from ferrisapp.app import get_appbuilder
from ..services.service_factory import ServiceFactory, services_available
from ..utils import (
    JSCTZIGenericColumn,
    JSCTZIGenericInterface,
    JSCTZIGenericSession,
    create_logger,
    get_access_token,
    remove_read_only_fields,
)

logger = create_logger(__name__)


class RoleRightsModel(FerrisGenericModel):

    can_access = JSCTZIGenericColumn(
        bool,
        nullable=True,
        foreign_key=False,
    )
    can_create = JSCTZIGenericColumn(
        bool,
        nullable=True,
        foreign_key=False,
    )
    can_delete = JSCTZIGenericColumn(
        bool,
        nullable=True,
        foreign_key=False,
    )
    can_read = JSCTZIGenericColumn(
        bool,
        nullable=True,
        foreign_key=False,
    )
    can_update = JSCTZIGenericColumn(
        bool,
        nullable=True,
        foreign_key=False,
    )
    changed_by = JSCTZIGenericColumn(
        str,
        nullable=True,
        foreign_key=False,
    )
    changed_on = JSCTZIGenericColumn(
        datetime.datetime,
        nullable=True,
        foreign_key=False,
    )
    created_by = JSCTZIGenericColumn(
        str,
        nullable=True,
        foreign_key=False,
    )
    created_on = JSCTZIGenericColumn(
        datetime.datetime,
        nullable=True,
        foreign_key=False,
    )
    entity = JSCTZIGenericColumn(
        str,
        nullable=True,
        foreign_key=False,
    )
    id = JSCTZIGenericColumn(
        int,
        primary_key=True,
        nullable=True,
    )
    role = JSCTZIGenericColumn(
        str,
        nullable=True,
        is_enum=True,
        foreign_key=False,
    )
    
    def to_dict(self):
        model_dict = {}

        for col_name in self.columns:
            if "<fab_addon_jsctzi_api.utils.JSCTZIGenericColumn" in repr(
                getattr(self, col_name)
            ):  # hacky way to recognize a null value in this case
                pass
            else:
                model_dict[col_name] = getattr(self, col_name)
        model_dict["id"] = getattr(self, self.pk, None)
        return model_dict

    def prepare_for_add(self) -> tuple[(int | str), dict]:
        model_payload = self.to_dict()

        _ = model_payload.pop("changed_by", None)  # safely pop
        _ = model_payload.pop("changed_on", None)  # safely pop
        _ = model_payload.pop("created_by", None)  # safely pop
        _ = model_payload.pop("created_on", None)  # safely pop
        oid = model_payload.pop(self.pk, None)  # safely pop
        _ = model_payload.pop("id", None)  # safely pop
        return oid, model_payload




class RoleRightsSession(JSCTZIGenericSession):
    def __init__(self) -> None:
        super().__init__(RoleRightsModel, ServiceFactory(service=services_available.ROLE_RIGHTS), logger)

    def all(self):
        """
        Get items from the respective Model.
        Overriden so it returns the correct amount of data, based on the number of items, page size and page number.
        If any Search criteria is applied in the UI, it also takes that into account to filter the results.
        :return:    items_amount -> int - The total amount of items found
                    items -> [Object] - A list of the items found, where each Object is related to the respective Model
        """
        items_amount = 0
        items = []
        app_builder = get_appbuilder()
        try:
            self.delete_all(self.model)

            # self._filters_cmd is a list of tuples of type: (self._equal, col_name, value)
            search_criteria_dict = {
                filter_cmd[1]: filter_cmd[2] for filter_cmd in self._filters_cmd
            }
            access_token = get_access_token()
            items_amount = len(
                self.service(token_passed=access_token).get_all(**search_criteria_dict)
            )  # total items in the DB for this search criteria

            if items_amount:
                # Only send the parameters if they are defined
                pagination_dict = {
                    field[0]: field[1]
                    for field in [("limit", self._limit), ("offset", self._offset)]
                    if field[1]
                }

                if self._order_by_cmd:
                    api_orderby_direction = ""
                    col_name, direction = self._order_by_cmd.split(" ")
                    if direction == "desc":
                        api_orderby_direction = "-"
                    order_by_dict = {"order_by": api_orderby_direction + col_name}
                    access_token = get_access_token()
                    data = self.service(token_passed=access_token).get_all(
                        **pagination_dict,
                        **search_criteria_dict,
                        **order_by_dict,
                    )

                else:
                    order_by_dict = {"order_by": None}
                    access_token = get_access_token()
                    data = self.service(token_passed=access_token).get_all(
                        **pagination_dict,
                        **search_criteria_dict,
                    )

                for oid in data:
                    access_token = get_access_token()
                    model_dict = self.service(token_passed=access_token).get(oid)
                    model_dict["id"] = oid
                    self._add_object(model_dict)

                items = self.store.get(self.query_class)

        except Exception as exception:
            self.logger_var.exception(f"Exception {exception} on method all().")

        return items_amount, items


    def get(self, primary_key):
        endpoint_name = self.extract_endpoint_name()
        self.delete_all(self.model())
        access_token = get_access_token()
        model_dict = self.service(token_passed=access_token).get(primary_key)
        model_dict["id"] = primary_key
        self._add_object(model_dict)
        user_and_action_info = {
            "userid": g.user.id,
            "username": g.user.username,
            "user_role": g.user.roles,
            "action": f"GET /{endpoint_name}/{primary_key}",
        }
        self.logger_var.debug("GET operation", extra=user_and_action_info)
        return self.model(**model_dict)


class RoleRightsInterface(JSCTZIGenericInterface):
    def __init__(self, obj, session) -> None:
        super().__init__(obj, session, ServiceFactory(service=services_available.ROLE_RIGHTS), logger)

    def add(self, item):
        try:
            endpoint_name = self.extract_endpoint_name()
            _, payload_dict = item.prepare_for_add()  # It assumes that we create the model in the pre_add
            final_payload = remove_read_only_fields(payload_dict)
            access_token = get_access_token()
            self.service(token_passed=access_token).add(final_payload)  # can change to get the new id and the status
        except Exception as exception:  # TODO: can use exception instead of debug, leave it for now
            self.logger_var.debug(str(exception))
            self.message = (exception.body, "danger")
        else:  # Only if no errors
            self.message = (as_unicode(self.add_row_message), "success")
            user_and_action_info = {
                "userid": g.user.id,
                "username": g.user.username,
                "user_role": g.user.roles,
                "action": f"POST /{endpoint_name}",
            }
            # here we could also link the id of entity created and the status return of the op
            self.logger_var.debug(
                f"Final payload we passed after successfull operation: {final_payload}",
                extra=user_and_action_info,
            )

        return True

    def edit(self, item):
        try:
            endpoint_name = self.extract_endpoint_name()
            oid, payload_dict = item.prepare_for_add()
            final_payload = remove_read_only_fields(payload_dict)
            access_token = get_access_token()
            self.service(token_passed=access_token).edit(final_payload, oid)
        except Exception as exception:
            self.logger_var.debug(str(exception))
            self.message = (exception.body, "danger")
        else:  # Only if no errors
            self.message = (as_unicode(self.edit_row_message), "success")
            user_and_action_info = {
                "userid": g.user.id,
                "username": g.user.username,
                "user_role": g.user.roles,
                "action": f"PUT /{endpoint_name}/{oid}",
            }
            self.logger_var.debug(
                f"Final payload we passed after successfull operation: {final_payload}",
                extra=user_and_action_info,
            )

        return True
