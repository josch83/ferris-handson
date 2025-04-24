# File auto generated, DO NOT edit because it will be smashed

import datetime
import uuid

from flask import request, abort, flash, redirect, url_for
from flask_babel import lazy_gettext
from flask_appbuilder import expose, has_access
from flask_appbuilder.fieldwidgets import Select2Widget, Select2ManyWidget, DateTimePickerWidget, DatePickerWidget
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.urltools import (
    get_filter_args,
    get_order_args,
    get_page_args,
    get_page_size_args,
)
from flask_login import login_required

from wtforms import (
    validators,
    SelectField,
    SelectMultipleField,
    DateTimeField,
    StringField,
    IntegerField,
    DateField,
    BooleanField,
    FloatField,
    PasswordField,
    TextAreaField,
)
from wtforms.widgets import TextArea
from markupsafe import Markup

from ferrisapp.app.views import Templates, Widgets
from ferrisapp.app.views.generic import FerrisGenericModelView
from ferrisapp.app.widgets import FerrisJsonField, FerrisListWidget, FerrisListBlockWidget
#from ferrisapp.app import get_appbuilder

from ..utils import (
    datetime_render,
    date_render,
    generate_dropdowns,
    get_partner_id,
    get_user_roles,
    
    
)
from ..custom_renders import *

from ..models.user_account import UserAccountModel, UserAccountInterface, UserAccountSession
from ..services.service_factory import services_available, ServiceFactory

from ..widgets import *
from ..views.address import MAGDEMOAddressView
from ..custom_utils import *



class StringListField(TextAreaField):

    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class MAGDEMOUserAccountAddForm(DynamicForm):

    fullname = StringField(
        lazy_gettext("Fullname"),
        validators=[validators.optional()],
        
        #render_kw={"style": "width:343px; height:123px;"},
        render_kw={"style": "width: 25%"},
        
        
        description=lazy_gettext("Fullname"),
        )
    name = StringField(
        lazy_gettext("Name"),
        validators=[validators.optional()],
        
        #render_kw={"style": "width:343px; height:123px;"},
        render_kw={"style": "width: 25%"},
        
        
        description=lazy_gettext("Name"),
        )
    addresses = SelectMultipleField(
        lazy_gettext("Addresses"),
        validators=[validators.optional()],
        
        
        coerce=int,
        
        widget=Select2ManyWidget(),
        render_kw={"style": "width: 25%"},
        default=[],
        description=lazy_gettext("Addresses"),
        )
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        addresses_get = request.args.get("_flt_0_addresses", type=int)
        filters_addresses = {"gte_id": addresses_get, "lte_id": addresses_get}

        if addresses_get is not None:
            self.addresses.choices = [(0, "--------")] + generate_dropdowns(
                service_chosen=services_available.ADDRESS, **filters_addresses
            )
        else:
            
            self.addresses.choices = [(0, "--------")] + generate_dropdowns(
                service_chosen=services_available.ADDRESS
            )
            



class MAGDEMOUserAccountSearchForm(DynamicForm):

    fullname = StringField(
        lazy_gettext("Fullname"),
        validators=[validators.optional()],
        
        #render_kw={"style": "width:343px; height:123px;"},
        render_kw={"style": "width: 25%"},
        
        
        description=lazy_gettext("Fullname"),
        )
    name = StringField(
        lazy_gettext("Name"),
        validators=[validators.optional()],
        
        #render_kw={"style": "width:343px; height:123px;"},
        render_kw={"style": "width: 25%"},
        
        
        description=lazy_gettext("Name"),
        )
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class MAGDEMOUserAccountView(FerrisGenericModelView):
    route_base = "/user_account"

    datamodel = UserAccountInterface(UserAccountModel, UserAccountSession())

    base_permissions = ['can_add', 'can_list', 'can_show', 'can_edit']
    list_title = lazy_gettext("List user_account")
    show_title = lazy_gettext("Show a user_account")
    add_title = lazy_gettext("Add a user_account")
    edit_title = lazy_gettext("Edit a user_account")

    add_form = edit_form = MAGDEMOUserAccountAddForm
    
    search_form = MAGDEMOUserAccountSearchForm
    
    related_views = [
        MAGDEMOAddressView,
    ]

    list_columns = [
        "changed_by",
        "changed_on",
        "created_by",
        "created_on",
        "fullname",
        "id",
        "name",
        
    ]
    search_columns = [
        "fullname",
        "name",
    ]
    order_columns = [
        "changed_on",
        "created_on",
        "id",
    ]
    add_columns = [
        "fullname",
        "name",
        "addresses",
    ]
    edit_columns = [
        "fullname",
        "name",
        "addresses",
    ]
    show_columns = [
        "changed_by",
        "changed_on",
        "created_by",
        "created_on",
        "fullname",
        "id",
        "name",
        
    ]
    formatters_columns = {
        "changed_on": lambda x: datetime_render(x),
        "created_on": lambda x: datetime_render(x),
    }

    label_columns = {
        "changed_by": lazy_gettext("Changed by"),
        "changed_on": lazy_gettext("Changed on"),
        "created_by": lazy_gettext("Created by"),
        "created_on": lazy_gettext("Created on"),
        "fullname": lazy_gettext("Fullname"),
        "name": lazy_gettext("Name"),
        "addresses": lazy_gettext("Addresses"),
    }

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        
        Widgets.list_widget = FerrisListWidget
        Widgets.apply_widgets(self)
        

        super().__init__(**kwargs)
    

    
    def _add(self):
        """
        Add function logic, override to implement different logic
        returns add widget or None
        """
        is_valid_form = True
        get_filter_args(self._filters)
        exclude_cols = self._filters.get_relation_cols()
        form = self.add_form.refresh()
        
        if request.method == "POST":
            self._fill_form_exclude_cols(exclude_cols, form)
            if form.validate():
                self.process_form(form, True)
                item = self.datamodel.obj()

                try:
                    # form.populate_obj(item)

                    item.fullname = form.fullname.data
                    item.name = form.name.data
                    item.addresses = form.addresses.data if form.addresses.data else []


                    self.pre_add(item)
                except Exception as exception:
                    flash(str(exception), "danger")
                else:
                    if self.datamodel.add(item):
                        self.post_add(item)
                    flash(*self.datamodel.message)
                finally:
                    return None
            else:
                is_valid_form = False
        if is_valid_form:
            self.update_redirect()
        return self._get_add_widget(form=form, exclude_cols=exclude_cols)
    

    
    def _edit(self, primary_key):
        """
        Edit function logic, override to implement different logic
        returns Edit widget and related list or None
        """
        is_valid_form = True
        pages = get_page_args()
        page_sizes = get_page_size_args()
        orders = get_order_args()
        get_filter_args(self._filters)
        exclude_cols = self._filters.get_relation_cols()

        item = self.datamodel.get(primary_key, self._base_filters)
        if not item:
            abort(404)
        # convert primary key to correct type, if primary key is non string type.
        primary_key = self.datamodel.get_pk_value(item)
        

        if request.method == "POST":
            form = self.edit_form.refresh(request.form)
            # fill the form with the suppressed cols, generated from exclude_cols
            self._fill_form_exclude_cols(exclude_cols, form)
            # trick to pass unique validation
            form._id = primary_key
            if form.validate():
                self.process_form(form, False)

                try:

                    # form.populate_obj(item)
                    item.fullname = form.fullname.data
                    item.name = form.name.data
                    item.addresses = form.addresses.data if form.addresses.data else []


                    self.pre_update(item)
                except Exception as exception:
                    print("Something wrong in the form population!!!", flush=True)
                    flash(str(exception), "danger")
                else:
                    if self.datamodel.edit(item):
                        self.post_update(item)
                    flash(*self.datamodel.message)
                finally:
                    return None
            else:
                is_valid_form = False
        else:
            form = self.edit_form.refresh(obj=item)
            
            
            if item.addresses == 0:
                form.addresses.data = None
            else:
                form.addresses.data = item.addresses


            # Perform additional actions to pre-fill the edit form.
            self.prefill_form(form, primary_key)

        widgets = self._get_edit_widget(form=form, exclude_cols=exclude_cols, pk=primary_key)
        widgets = self._get_related_views_widgets(
            item,
            filters={},
            orders=orders,
            pages=pages,
            page_sizes=page_sizes,
            widgets=widgets,
        )
        if is_valid_form:
            self.update_redirect()
        return widgets
    

    # Decorator function to use in every view class
    # Not used right now because we're testing without security, but might be needed later.
    

    
    @expose("/add", methods=["GET", "POST"])
    @has_access
    @login_required
    def add(self):

        return super().add()
    

    
    @expose("/list/", methods=["GET"])
    @has_access
    @login_required
    def list(self):

        return super().list()
    
    
    @expose("/show/<int:pk>", methods=["GET"])
    @has_access
    @login_required
    def show(self, pk):

        return super().show(pk)
    
    
    @expose("/edit/<int:pk>", methods=["GET", "POST"])
    @has_access
    @login_required
    def edit(self, pk):

        return super().edit(pk)
    
    



    
    def pre_add(self, item):
        item.id = uuid.uuid1().int
        
    def pre_update(self, item):
        ## Handle properly the edge case of int fields
        for key, value in request.form.items():
            if key not in ["csrf_token", "id",
                        "addresses",
                        ]:

                if value != "":
                    if item.properties[key].col_type == datetime.date:
                        date_value = datetime.datetime.strptime(value, "%Y-%m-%d").date()
                        setattr(item, key, date_value)
                    elif item.properties[key].col_type == datetime.datetime:
                        datetime_value = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
                        setattr(item, key, datetime_value)
                    else:
                        #ja = item.properties[key].col_type(value)  # it doesn't look it is needed...
                        #print(ja, flush=True)

                        setattr(item, key, item.properties[key].col_type(value))
                        

                else:

                    setattr(item, key, None)
                    