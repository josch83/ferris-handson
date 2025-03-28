from ferris_fab_oauth.views import AuthOAUTHView
from ferrisapp.app.views import Templates, Widgets
from flask_appbuilder.security.registerviews import (
    RegisterUserDBView,
    RegisterUserOAuthView,
    RegisterUserOIDView,
)
from flask_appbuilder.security.views import (
    AuthDBView,
    AuthLDAPView,
    AuthOAuthView,
    AuthOIDView,
    AuthRemoteUserView,
    AuthView,
    PermissionModelView,
    PermissionViewModelView,
    RegisterUserModelView,
    ResetMyPasswordView,
    ResetPasswordView,
    RoleModelView,
    UserDBModelView,
    UserInfoEditView,
    UserLDAPModelView,
    UserOAuthModelView,
    UserOIDModelView,
    UserRemoteUserModelView,
    UserStatsChartView,
    ViewMenuModelView,
)


class FerrisUserModelView(UserDBModelView):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)


class FerrisRoleModelView(RoleModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisPermissionModelView(PermissionModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisAuthDBView(AuthDBView):

    login_template = Templates.login_template


class FerrisUserOAuthModelView(UserOAuthModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisUserOIDModelView(UserOIDModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisUserLDAPModelView(UserLDAPModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisUserRemoteUserModelView(UserRemoteUserModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisViewMenuModelView(ViewMenuModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisPermissionViewModelView(PermissionViewModelView):

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisUserStatsChartView(UserStatsChartView):

    chart_template = "ferris/general/charts/jsonchart.html"

    def __init__(self, **kwargs):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__(**kwargs)


class FerrisRegisterUserDBView(RegisterUserDBView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisRegisterUserOAuthView(RegisterUserOAuthView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisRegisterUserOIDView(RegisterUserOIDView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisRegisterUserModelView(RegisterUserModelView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisAuthOIDView(AuthOIDView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisAuthView(AuthView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisAuthLDAPView(AuthLDAPView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


# class FerrisAuthOAuthView(AuthOAuthView):  # default
class FerrisAuthOAuthView(AuthOAUTHView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisAuthRemoteUserView(AuthRemoteUserView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisResetMyPasswordView(ResetMyPasswordView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisResetPasswordView(ResetPasswordView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()


class FerrisUserInfoEditView(UserInfoEditView):

    def __init__(self):
        Templates.apply_modelview_templates(self)
        Widgets.apply_widgets(self)

        super().__init__()
