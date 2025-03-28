# Never clean up imports, the generated parts use imports marked unused
import traceback
import connexion
import jsctzi_api.models.address as swagger  # noqa: E501
from jsctzi_api.models.api_classes import db
from jsctzi_api.models.sqla_models import (
    role_access,
    Address,
)  # noqa: E501

from sqlalchemy.exc import IntegrityError
from sqlalchemy import text, not_
import re
import datetime

# Our allowed column name format:
VALID_COL = re.compile("[a-z][a-z0-9_]*")


def create_address(body):  # noqa: E501
    """Create a new address

    Create a new address with new id and provided data  # noqa: E501

    :param body:
    :type body: dict | bytes

    :param usertag:
    :type usertag: string

    :rtype: None
    """

    usertag = connexion.context["token_info"]
    if not role_access('address', usertag, 'can_create'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403

    if connexion.request.is_json:
        try:
            body = connexion.request.get_json()
            obj = Address()
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


def get_address_by_id(oid):  # noqa: E501
    """Get a address by ID

    Get a address by ID  # noqa: E501

    :param usertag:
    :type usertag: string

    :param oid: address ID
    :type oid: integer

    :rtype: Address
    """

    usertag = connexion.context["token_info"]
    if not role_access('address', usertag, 'can_read'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403

    try:
        obj = db.session.query(Address).filter_by(id=oid).first()
        if not obj:
            return "An Address with the specified ID was not found.", 404
        if not obj.id_has_access(usertag):
            return "Record Access Denied", 403
        obj_dict = obj.to_dict()
        return swagger.Address(**obj_dict)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return 'Error: ' + str(e), 500
    finally:
        db.session.close()


def get_addresss(
        offset=0,
        limit=0, 
        order_by=None, 
        list_fields=None,
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
        email_address=None,
        not_email_address=None,
        ilike_email_address=None,
        notilike_email_address=None,
        equal_id=None,
        not_id=None,
        in_list_id=None,
        gte_id=None,
        lte_id=None,
        equal_user_id=None,
        not_user_id=None,
        in_list_user_id=None,
        gte_user_id=None,
        lte_user_id=None,
):  # noqa: E501
    """Get all address IDs

    Get all address IDs  # noqa: E501

    :param usertag:
    :type usertag: string

    

    :rtype: List[dict('id': integer, 'name': string)]
    """
    usertag = connexion.context["token_info"]
    if not role_access('address', usertag, 'can_access'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403

    try:
        query = db.session.query(Address)
        if changed_by:
            query = query.filter(Address.changed_by.like(changed_by))
        if not_changed_by:
            query = query.filter(Address.changed_by.notlike(not_changed_by))
        if ilike_changed_by:
            query = query.filter(Address.changed_by.ilike(ilike_changed_by))
        if notilike_changed_by:
            # not ( c ilike "str") include NULL, while the not exxisting (c notilike "str") would not
            # so filter the NULL as well
            query = query.filter(not_(Address.changed_by.ilike(notilike_changed_by)))
            query = query.filter(Address.changed_by != None)
        if gte_changed_on:
            query = query.filter(Address.changed_on >= gte_changed_on)
        if lte_changed_on:
            query = query.filter(Address.changed_on <= lte_changed_on)
        if created_by:
            query = query.filter(Address.created_by.like(created_by))
        if not_created_by:
            query = query.filter(Address.created_by.notlike(not_created_by))
        if ilike_created_by:
            query = query.filter(Address.created_by.ilike(ilike_created_by))
        if notilike_created_by:
            # not ( c ilike "str") include NULL, while the not exxisting (c notilike "str") would not
            # so filter the NULL as well
            query = query.filter(not_(Address.created_by.ilike(notilike_created_by)))
            query = query.filter(Address.created_by != None)
        if gte_created_on:
            query = query.filter(Address.created_on >= gte_created_on)
        if lte_created_on:
            query = query.filter(Address.created_on <= lte_created_on)
        if email_address:
            query = query.filter(Address.email_address.like(email_address))
        if not_email_address:
            query = query.filter(Address.email_address.notlike(not_email_address))
        if ilike_email_address:
            query = query.filter(Address.email_address.ilike(ilike_email_address))
        if notilike_email_address:
            # not ( c ilike "str") include NULL, while the not exxisting (c notilike "str") would not
            # so filter the NULL as well
            query = query.filter(not_(Address.email_address.ilike(notilike_email_address)))
            query = query.filter(Address.email_address != None)
        if equal_id:
            query = query.filter(Address.id == equal_id)
        if not_id:
            query = query.filter(Address.id != not_id)
        if in_list_id:
            query = query.filter(Address.id.in_(in_list_id))
        if gte_id:
            query = query.filter(Address.id >= gte_id)
        if lte_id:
            query = query.filter(Address.id <= lte_id)
        if equal_user_id:
            query = query.filter(Address.user_id == equal_user_id)
        if not_user_id:
            query = query.filter(Address.user_id != not_user_id)
        if in_list_user_id:
            query = query.filter(Address.user_id.in_(in_list_user_id))
        if gte_user_id:
            query = query.filter(Address.user_id >= gte_user_id)
        if lte_user_id:
            query = query.filter(Address.user_id <= lte_user_id)
        query = query.filter(Address.id_has_access(usertag))
        if order_by:
            order_col = order_by.lstrip("-").lstrip("+").lower()
            if not VALID_COL.match(order_col):
                return 'Error: Invalid Column for order_by', 500
            if order_col == "id":  # fix duplicate id for polymorph entities
                order_col = "address.id"
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


def update_address_by_id(body, oid):  # noqa: E501
    """Update a address by ID

    Update a address by ID with the provided data  # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param usertag:
    :type usertag: string
    :param oid: address ID
    :type oid:  integer

    :rtype: None
    """
    usertag = connexion.context["token_info"]
    if not role_access('address', usertag, 'can_update'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403
    if connexion.request.is_json:
        try:
            body = connexion.request.get_json()
            obj = db.session.query(Address).filter_by(modifiable=True).filter_by(id=oid).first()
            if not obj:
                return "A modifiable Address with the specified ID was not found.", 404
            if not obj.id_has_access(usertag):
                return "Record Access Denied", 403
            body.pop('id', None)
            obj.from_dict(body)
            obj.set_writer(usertag)
            if obj.valid_object_update():
                db.session.merge(obj)
                db.session.commit()
                return 'Address updated'
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


def delete_address_by_id(oid):  # noqa: E501
    """Delete a address by ID

    Delete a address by ID # noqa: E501

    :param usertag:
    :type usertag: string
    :param oid: address ID
    :type oid:  integer

    :rtype: None
    """

    usertag = connexion.context["token_info"]
    if not role_access('address', usertag, 'can_delete'):
        print(usertag, 'Access denied',flush=True)
        return "Service Access Denied", 403
    try:
        obj = db.session.query(Address).filter_by(modifiable=True).filter_by(id=oid).first()
        if not obj:
            return "A deletable Address with the specified ID was not found.", 404
        if not obj.id_has_access(usertag):
            return "Record Access Denied", 403
        db.session.delete(obj)
        db.session.commit()
        return 'Address deleted'
    except Exception as e:
        print(e)
        traceback.print_exc()
        db.session.rollback()
        return 'Error: ' + str(e), 500
    finally:
        db.session.close()


