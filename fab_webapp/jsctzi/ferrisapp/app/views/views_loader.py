from ferrisapp.app import appbuilder, db
from ferrisapp.app.views.dashboard import FerrisDashboardView

appbuilder.add_view(FerrisDashboardView, "Dashboard")

db.create_all()
