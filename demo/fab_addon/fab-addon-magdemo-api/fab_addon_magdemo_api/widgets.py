# File auto generated, DO NOT edit because it will be smashed

from flask import Markup, url_for
from flask_babel import lazy_gettext as _
from wtforms.fields import SelectMultipleField, StringField
from wtforms.widgets import Select, TextInput


from .models.address import AddressSession, AddressModel

from .utils import get_access_token



class AddressListWidget(object):
    @staticmethod
    def render(list_items):
        html = ""
        session = AddressSession()
        for list_item in list_items:
            obj = session.get(list_item)
            repr_str = repr(obj)
            
            html += (
                '<a href="'
                + url_for("MAGDEMOAddressView.show", pk=list_item)
                + '" class="btn btn-xs btn-neutral btn-outline" data-toggle="tooltip" rel="tooltip" title="Show address"><i class="fa fa-tag"></i> '
                + repr_str
                + "</a> "
            )
        session.delete_all(AddressModel())
        return Markup(html)


def as_unicode(s):
    if isinstance(s, bytes):
        return s.decode("utf-8")

    return str(s)


class Select2TagsWidget(TextInput):

    def __call__(self, field, **kwargs):
        return super(Select2TagsWidget, self).__call__(field, **kwargs)


class TestSelect2TagsField(StringField):
    """`Select2 <http://ivaynberg.github.com/select2/#tags>`_ styled text field.
    You must include select2.js, form-x.x.x.js and select2 stylesheet for it to work.
    """

    widget = Select2TagsWidget()

    def __init__(self, label=None, validators=None, save_as_list=False, coerce=str, **kwargs):
        """Initialization
        :param save_as_list:
            If `True` then populate ``obj`` using list else string
        """
        self.save_as_list = save_as_list
        self.coerce = coerce

        super(TestSelect2TagsField, self).__init__(label, validators, **kwargs)

    def process_formdata(self, valuelist):
        if valuelist:
            if self.save_as_list:
                self.data = [self.coerce(v.strip()) for v in valuelist[0].split(",") if v.strip()]
            else:
                self.data = self.coerce(valuelist[0])

    def _value(self):
        if isinstance(self.data, (list, tuple)):
            return ",".join(as_unicode(v) for v in self.data)
        elif self.data:
            return as_unicode(self.data)
        else:
            return ""


class Select2ManyTagsWidget(Select):
    extra_classes = None

    def __init__(self, extra_classes=None, style=None):
        self.extra_classes = extra_classes
        self.style = style
        super(Select2ManyTagsWidget, self).__init__()

    def __call__(self, field, **kwargs):
        kwargs["class"] = "my_select2 form-control"
        if self.extra_classes:
            kwargs["class"] = kwargs["class"] + " " + self.extra_classes
        if self.style:
            kwargs["style"] = self.style
        kwargs["data-placeholder"] = _("Create a new tag or select an existing one")
        kwargs["multiple"] = "true"
        kwargs["data-tags"] = "true"
        kwargs["data-token-separators"] = "[',', ' ', ';']"
        kwargs["data-allow-clear"] = "true"
        kwargs["theme"] = "bootstrap"
        if "name_" in kwargs:
            field.name = kwargs["name_"]
        return super(Select2ManyTagsWidget, self).__call__(field, **kwargs)


class NonValidatingSelectMultipleField(SelectMultipleField):  # Custom for tags processing

    def iter_choices(self):
        for value, label in self.choices:
            print(f"Inside iter_choices!", flush=True)

            try:
                existing_value = self.coerce(value)
                selected = self.data is not None and existing_value in self.data
            except (ValueError, TypeError):
                selected = False
            print(f"What is the choices tuple: ({value}, {label}, {selected} )", flush=True)

            yield (value, label, selected)

    def process_data(self, value):
        print(f"Inside process_data!", flush=True)
        print(f"What is value: {value}", flush=True)
        print(f"Type of value: {type(value)}", flush=True)
        self.data = []
        if value is not None:
            for v in value:
                if v is not None:
                    try:
                        self.data.append(self.coerce(v))
                    except (ValueError, TypeError):
                        self.data.append(v)
                else:
                    self.data = None
        else:
            self.data = None
        print(f"What is self.data inside process_data: {self.data}", flush=True)

    def process_formdata(self, valuelist):
        print(f"Inside process_formdata!", flush=True)
        print(f"What is valuelist: {valuelist}", flush=True)
        print(f"Type of valuelist: {type(valuelist)}", flush=True)
        self.data = [x for x in valuelist]
        print(f"What is self.data inside process_formdata: {self.data}", flush=True)

    def pre_validate(self, form):
        print(f"Inside pre_validate!", flush=True)
        pass

    def post_validate(self, form, validation_stopped):
        print(f"Inside post_validate!", flush=True)
        pass
