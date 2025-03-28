from flask import render_template
from flask_appbuilder import ModelView

from ..widgets import (
    FerrisFormWidget,
    FerrisListWidget,
    FerrisSearchWidget,
    FerrisShowWidget,
)


class Templates:
    list_template = "ferris/general/model/list.html"
    add_template = "ferris/general/model/add.html"
    edit_template = "ferris/general/model/edit.html"
    show_template = "ferris/general/model/show.html"
    login_template = "ferris/general/security/login_db.html"

    @staticmethod
    def apply_modelview_templates(modelview):
        modelview.list_template = Templates.list_template
        modelview.add_template = Templates.add_template
        modelview.edit_template = Templates.edit_template
        modelview.show_template = Templates.show_template


class Widgets:
    add_widget = FerrisFormWidget
    edit_widget = FerrisFormWidget
    show_widget = FerrisShowWidget
    list_widget = FerrisListWidget
    search_widget = FerrisSearchWidget

    @staticmethod
    def apply_widgets(modelview):
        modelview.add_widget = Widgets.add_widget
        modelview.edit_widget = Widgets.edit_widget
        modelview.list_widget = Widgets.list_widget
        modelview.show_widget = Widgets.show_widget
        modelview.search_widget = Widgets.search_widget

    @staticmethod
    def json_preview(json, skip_if_empty=False, height=600):
        if skip_if_empty and (not json or len(json) < 1):
            return "N/A"

        return render_template(
            "ferris/general/widgets/json_edit.html",
            field={"name": ""},
            value=json,
            read_only=True,
            skip_if_empty=skip_if_empty,
            height=height,
        )


class FerrisModelView(ModelView):
    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)
