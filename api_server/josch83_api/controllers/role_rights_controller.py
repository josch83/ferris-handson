# Never clean up imports, the generated parts use imports marked unused
import traceback
import connexion
import josch83_api.models.role_rights as swagger  # noqa: E501
from josch83_api.models.api_classes import db
from josch83_api.models.sqla_models import (
    role_access,
    RoleRights,
)  # noqa: E501

from sqlalchemy.exc import IntegrityError
from sqlalchemy import text, not_
import re
import datetime

# Our allowed column name format:
VALID_COL = re.compile("[a-z][a-z0-9_]*")


def create_role_rights(body):  # noqa: E501
    """Create a new role_rights

    Create a new role_rights with new id and provided data  # noqa: E501

    :param body:
    :type body: dict | bytes

    :param usertag:
    :type usertag: string

    :rtype: None
    """

    usertag = connexion.context["token_info"]
    if not role_access('role_rights', usertag, 'can_create'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403

    if connexion.request.is_json:
        try:
            body = connexion.request.get_json()
            obj = RoleRights()
            body.pop('id', None)
            obj.from_dict(body)
            obj.set_writer(usertag)
            if obj.valid_object_create():
                db.session.add(obj)
                db.session.flush()  # update relationships
                if not obj.id_has_access(usertag):
                    db.session.rollback()
                    return "Record Access Denied", 403
                # Ensure inconsistencies are found by the DB, before a possible kc_registration
                db.session.flush()
                db.session.commit()
                return {'oid': obj.id}, 201
            return "Not valid, create denied", 400
        except ValueError as e:
            print(e)
            db.session.rollback()
            return 'Error: ' + str(e), 400
        except IntegrityError as e:
            print(e)
            db.session.rollback()
            return 'Error: ' + str(e), 400
        except Exception as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return 'Error: ' + str(e), 500
        finally:
            db.session.close()
    return "Error: No object to create", 400


def get_role_rights_by_id(oid):  # noqa: E501
    """Get a role_rights by ID

    Get a role_rights by ID  # noqa: E501

    :param usertag:
    :type usertag: string

    :param oid: role_rights ID
    :type oid: integer

    :rtype: RoleRights
    """

    usertag = connexion.context["token_info"]
    if not role_access('role_rights', usertag, 'can_read'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403

    try:
        obj = db.session.query(RoleRights).filter_by(id=oid).first()
        if not obj:
            return "An RoleRights with the specified ID was not found.", 404
        if not obj.id_has_access(usertag):
            return "Record Access Denied", 403
        obj_dict = obj.to_dict()
        return swagger.RoleRights(**obj_dict)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return 'Error: ' + str(e), 500
    finally:
        db.session.close()


def get_role_rightss(
        offset=0,
        limit=0, 
        order_by=None, 
        list_fields=None,
        equal_can_access=None,
        not_can_access=None,
        isnull_can_access=None,
        equal_can_create=None,
        not_can_create=None,
        isnull_can_create=None,
        equal_can_delete=None,
        not_can_delete=None,
        isnull_can_delete=None,
        equal_can_read=None,
        not_can_read=None,
        isnull_can_read=None,
        equal_can_update=None,
        not_can_update=None,
        isnull_can_update=None,
        changed_by=None,
        not_changed_by=None,
        ilike_changed_by=None,
        notilike_changed_by=None,
        gte_changed_on=None,
        lte_changed_on=None,
        created_by=None,
        not_created_by=None,
        ilike_created_by=None,
        notilike_created_by=None,
        gte_created_on=None,
        lte_created_on=None,
        entity=None,
        not_entity=None,
        ilike_entity=None,
        notilike_entity=None,
        isnull_entity=None,
        equal_id=None,
        not_id=None,
        in_list_id=None,
        gte_id=None,
        lte_id=None,
        equal_role=None,
        not_role=None,
        in_list_role=None,
        isnull_role=None,
):  # noqa: E501
    """Get all role_rights IDs

    Get all role_rights IDs  # noqa: E501

    :param usertag:
    :type usertag: string

    

    :rtype: List[dict('id': integer, 'name': string)]
    """
    usertag = connexion.context["token_info"]
    if not role_access('role_rights', usertag, 'can_access'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403

    try:
        query = db.session.query(RoleRights)
        if equal_can_access is not None:
            query = query.filter(RoleRights.can_access == equal_can_access)
        if not_can_access is not None:
            query = query.filter(RoleRights.can_access != not_can_access)
        if isnull_can_access:
            query = query.filter(RoleRights.can_access == None)
        if equal_can_create is not None:
            query = query.filter(RoleRights.can_create == equal_can_create)
        if not_can_create is not None:
            query = query.filter(RoleRights.can_create != not_can_create)
        if isnull_can_create:
            query = query.filter(RoleRights.can_create == None)
        if equal_can_delete is not None:
            query = query.filter(RoleRights.can_delete == equal_can_delete)
        if not_can_delete is not None:
            query = query.filter(RoleRights.can_delete != not_can_delete)
        if isnull_can_delete:
            query = query.filter(RoleRights.can_delete == None)
        if equal_can_read is not None:
            query = query.filter(RoleRights.can_read == equal_can_read)
        if not_can_read is not None:
            query = query.filter(RoleRights.can_read != not_can_read)
        if isnull_can_read:
            query = query.filter(RoleRights.can_read == None)
        if equal_can_update is not None:
            query = query.filter(RoleRights.can_update == equal_can_update)
        if not_can_update is not None:
            query = query.filter(RoleRights.can_update != not_can_update)
        if isnull_can_update:
            query = query.filter(RoleRights.can_update == None)
        if changed_by:
            query = query.filter(RoleRights.changed_by.like(changed_by))
        if not_changed_by:
            query = query.filter(RoleRights.changed_by.notlike(not_changed_by))
        if ilike_changed_by:
            query = query.filter(RoleRights.changed_by.ilike(ilike_changed_by))
        if notilike_changed_by:
            # not ( c ilike "str") include NULL, while the not exxisting (c notilike "str") would not
            # so filter the NULL as well
            query = query.filter(not_(RoleRights.changed_by.ilike(notilike_changed_by)))
            query = query.filter(RoleRights.changed_by != None)
        if gte_changed_on:
            query = query.filter(RoleRights.changed_on >= gte_changed_on)
        if lte_changed_on:
            query = query.filter(RoleRights.changed_on <= lte_changed_on)
        if created_by:
            query = query.filter(RoleRights.created_by.like(created_by))
        if not_created_by:
            query = query.filter(RoleRights.created_by.notlike(not_created_by))
        if ilike_created_by:
            query = query.filter(RoleRights.created_by.ilike(ilike_created_by))
        if notilike_created_by:
            # not ( c ilike "str") include NULL, while the not exxisting (c notilike "str") would not
            # so filter the NULL as well
            query = query.filter(not_(RoleRights.created_by.ilike(notilike_created_by)))
            query = query.filter(RoleRights.created_by != None)
        if gte_created_on:
            query = query.filter(RoleRights.created_on >= gte_created_on)
        if lte_created_on:
            query = query.filter(RoleRights.created_on <= lte_created_on)
        if entity:
            query = query.filter(RoleRights.entity.like(entity))
        if not_entity:
            query = query.filter(RoleRights.entity.notlike(not_entity))
        if ilike_entity:
            query = query.filter(RoleRights.entity.ilike(ilike_entity))
        if notilike_entity:
            # not ( c ilike "str") include NULL, while the not exxisting (c notilike "str") would not
            # so filter the NULL as well
            query = query.filter(not_(RoleRights.entity.ilike(notilike_entity)))
            query = query.filter(RoleRights.entity != None)
        if isnull_entity:
            query = query.filter(RoleRights.entity == None)
        if equal_id:
            query = query.filter(RoleRights.id == equal_id)
        if not_id:
            query = query.filter(RoleRights.id != not_id)
        if in_list_id:
            query = query.filter(RoleRights.id.in_(in_list_id))
        if gte_id:
            query = query.filter(RoleRights.id >= gte_id)
        if lte_id:
            query = query.filter(RoleRights.id <= lte_id)
        if equal_role:
            query = query.filter(RoleRights.role == equal_role)
        if not_role:
            query = query.filter(RoleRights.role != not_role)
        if in_list_role:
            query = query.filter(RoleRights.role.in_(in_list_role))
        if isnull_role:
            query = query.filter(RoleRights.role == None)
        query = query.filter(RoleRights.id_has_access(usertag))
        if order_by:
            order_col = order_by.lstrip("-").lstrip("+").lower()
            if not VALID_COL.match(order_col):
                return 'Error: Invalid Column for order_by', 500
            if order_col == "id":  # fix duplicate id for polymorph entities
                order_col = "role_rights.id"
            order = " DESC NULLS LAST" if order_by[0] == "-" else " ASC NULLS LAST"
            query = query.order_by(text(order_col + order))
        if offset > 0:
            query = query.offset(offset)
        if limit > 0:
            query = query.limit(limit)
        # found_list = (row for row in query.all() if row.id_has_access(usertag))
        found_list = query.all()
        id_list = []
        for obj in found_list:
            obj_dict = dict()
            obj_dict['id'] = obj.id
            if list_fields is None:
                obj_dict['name'] = obj.__repr__()
            else:
                od = obj.to_dict()
                for lf in list_fields:
                    obj_dict[lf] = od.get(lf, None)
            id_list.append(obj_dict)
        return id_list
    except Exception as e:
        print(e)
        traceback.print_exc()
        return 'Error: ' + str(e), 500
    finally:
        db.session.close()


def update_role_rights_by_id(body, oid):  # noqa: E501
    """Update a role_rights by ID

    Update a role_rights by ID with the provided data  # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param usertag:
    :type usertag: string
    :param oid: role_rights ID
    :type oid:  integer

    :rtype: None
    """
    usertag = connexion.context["token_info"]
    if not role_access('role_rights', usertag, 'can_update'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403
    if connexion.request.is_json:
        try:
            body = connexion.request.get_json()
            obj = db.session.query(RoleRights).filter_by(modifiable=True).filter_by(id=oid).first()
            if not obj:
                return "A modifiable RoleRights with the specified ID was not found.", 404
            if not obj.id_has_access(usertag):
                return "Record Access Denied", 403
            body.pop('id', None)
            obj.from_dict(body)
            obj.set_writer(usertag)
            if obj.valid_object_update():
                db.session.merge(obj)
                db.session.commit()
                return 'RoleRights updated'
            return "Not valid, update denied", 400
        except ValueError as e:
            print(e)
            db.session.rollback()
            return 'Error: ' + str(e), 400
        except IntegrityError as e:
            print(e)
            db.session.rollback()
            return 'Error: ' + str(e), 400
        except Exception as e:
            print(e)
            traceback.print_exc()
            db.session.rollback()
            return 'Error: ' + str(e), 500
        finally:
            db.session.close()

    return "Error: No object to update", 400


def delete_role_rights_by_id(oid):  # noqa: E501
    """Delete a role_rights by ID

    Delete a role_rights by ID # noqa: E501

    :param usertag:
    :type usertag: string
    :param oid: role_rights ID
    :type oid:  integer

    :rtype: None
    """

    usertag = connexion.context["token_info"]
    if not role_access('role_rights', usertag, 'can_delete'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403
    try:
        obj = db.session.query(RoleRights).filter_by(modifiable=True).filter_by(id=oid).first()
        if not obj:
            return "A deletable RoleRights with the specified ID was not found.", 404
        if not obj.id_has_access(usertag):
            return "Record Access Denied", 403
        db.session.delete(obj)
        db.session.commit()
        return 'RoleRights deleted'
    except Exception as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return 'Error: ' + str(e), 500
    finally:
        db.session.close()


