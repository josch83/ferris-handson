from ferrisapp.app.views import Templates, Widgets
from ferrisapp.app.views.generic import FerrisGenericModelView


class ElasticView(FerrisGenericModelView):
    route_base = ""
    base_permissions = ["can_list"]

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)

        self.title = "Elastic"
