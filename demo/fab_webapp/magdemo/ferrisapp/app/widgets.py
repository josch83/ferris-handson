import json

from flask import render_template
from flask.globals import _request_ctx_stack
from flask_appbuilder.widgets import (
    FormWidget,
    ListWidget,
    RenderTemplateWidget,
    SearchWidget,
    ShowWidget,
)
from markupsafe import Markup, escape
from wtforms.fields.simple import Field, StringField, TextAreaField
from wtforms.widgets.core import TextArea, html_params


class FerrisFormWidget(FormWidget):
    template = "ferris/general/widgets/form.html"
    show_search_widget = None

    def search_widget(self):
        return ""


class FerrisShowWidget(ShowWidget):
    template = "ferris/general/widgets/show.html"
    show_search_widget = None

    def search_widget(self):
        return ""


class FerrisListWidget(ListWidget):
    template = "ferris/general/widgets/list.html"
    show_search_widget = None

    def __call__(self, **kwargs):
        ctx = _request_ctx_stack.top
        jinja_env = ctx.app.jinja_env

        template = jinja_env.get_template(self.template)
        args = self.template_args.copy()
        args.update(kwargs)

        return template.render(args)

    def search_widget(self):
        if self.show_search_widget:
            return self.show_search_widget()

        return ""


class FerrisListBlockWidget(ListWidget):
    template = "ferris/general/widgets/list_block.html"
    show_search_widget = None

    def __call__(self, **kwargs):
        ctx = _request_ctx_stack.top
        jinja_env = ctx.app.jinja_env

        template = jinja_env.get_template(self.template)
        args = self.template_args.copy()
        args.update(kwargs)

        return template.render(args)

    def search_widget(self):
        if self.show_search_widget:
            return self.show_search_widget()

        return ""


class FerrisSearchWidget(SearchWidget):
    template = "ferris/general/widgets/search.html"
    show_search_widget = None

    def search_widget(self):
        return ""


class FerrisJSONWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        if "required" not in kwargs and "required" in getattr(field, "flags", []):
            kwargs["required"] = True

        return render_template("ferris/general/widgets/json_edit.html", field=field, value=field._value(), **kwargs)


class NonEditableWidget(object):
    def __call__(self, field, **kwargs):
        if kwargs.get("submit_value", True):
            return Markup(
                '<div %s disabled="disabled">%s<input type="hidden" name="%s" value="%s"></div>'
                % (
                    html_params(**kwargs),
                    escape(field._value()),
                    field.name,
                    escape(field._value()),
                )
            )

        return Markup('<div %s disabled="disabled">%s</div>' % (html_params(**kwargs), escape(field._value())))


class HiddenInputWidget(object):
    def __call__(self, field, **kwargs):
        return Markup(
            '<input type="hidden" name="%s" value="%s">'
            % (
                field.name,
                escape(field._value()),
            )
        )


class NonEditableTextareaWidget(object):
    def __call__(self, field, **kwargs):
        import logging

        logging.getLogger().debug(field._value())

        return Markup(
            '<textarea %s readonly="readonly" name="%s" value="%s">%s</textarea>'
            % (
                html_params(**kwargs),
                escape(field._value()),
                field.name,
                escape(field._value()),
            )
        )


class FerrisFileWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        if "required" not in kwargs and "required" in getattr(field, "flags", []):
            kwargs["required"] = True
        return render_template("ferris/general/widgets/file_select.html", field=field, value=field._value(), **kwargs)


class FerrisFileField(TextAreaField):
    widget = FerrisFileWidget()


class FerrisJsonField(TextAreaField):
    widget = FerrisJSONWidget()


class FerrisNonEditableField(StringField):
    widget = NonEditableWidget()


class FerrisNonEditableTextarea(StringField):
    widget = NonEditableTextareaWidget()


class FerrisHiddenInputField(StringField):
    widget = HiddenInputWidget()
