from flask_appbuilder import BaseView, expose, has_access


class FerrisDashboardView(BaseView):
    route_base = "/dashboard"
    default_view = "index"

    @expose("/")
    @has_access
    def index(self):
        return self.render_template("ferris/pages/dashboard.html")
