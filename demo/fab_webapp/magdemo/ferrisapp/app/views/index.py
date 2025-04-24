from flask import g, redirect, session
from flask_appbuilder import BaseView, IndexView, expose
from flask_babel import refresh


class FerrisIndexView(IndexView):
    @expose("/")
    def index(self):
        user = g.user

        if user.is_anonymous:
            return self.render_template("ferris/pages/index.html")
        else:
            return redirect("/dashboard")


class LocaleView(BaseView):
    route_base = "/lang"

    default_view = "index"

    @expose("/<string:locale>")
    def index(self, locale):
        session["locale"] = locale
        refresh()
        self.update_redirect()
        return redirect(self.get_redirect())
