from ferrisapp.app.views.auth import (
    FerrisAuthDBView,
    FerrisAuthLDAPView,
    FerrisAuthOAuthView,
    FerrisAuthOIDView,
    FerrisAuthRemoteUserView,
    FerrisAuthView,
    FerrisPermissionModelView,
    FerrisPermissionViewModelView,
    FerrisRegisterUserDBView,
    FerrisRegisterUserModelView,
    FerrisRegisterUserOAuthView,
    FerrisRegisterUserOIDView,
    FerrisResetMyPasswordView,
    FerrisResetPasswordView,
    FerrisRoleModelView,
    FerrisUserInfoEditView,
    FerrisUserLDAPModelView,
    FerrisUserModelView,
    FerrisUserOAuthModelView,
    FerrisUserOIDModelView,
    FerrisUserRemoteUserModelView,
    FerrisUserStatsChartView,
    FerrisViewMenuModelView,
)
from flask import current_app
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.sqla.models import User


class FerrisUser(User):
    __tablename__ = "ab_user"

    @property
    def is_admin(self):
        admin_role = current_app.config.get("AUTH_ROLE_ADMIN", "admin")
        return admin_role in self.role_names

    @property
    def role_names(self):
        return [role.name for role in self.roles]


class FerrisSecurityManager(SecurityManager):

    userdbmodelview = FerrisUserModelView
    userldapmodelview = FerrisUserLDAPModelView
    useroidmodelview = FerrisUserOIDModelView
    useroauthmodelview = FerrisUserOAuthModelView
    userremoteusermodelview = FerrisUserRemoteUserModelView
    registerusermodelview = FerrisRegisterUserModelView

    authdbview = FerrisAuthDBView
    authldapview = FerrisAuthLDAPView
    authoidview = FerrisAuthOIDView
    authoauthview = FerrisAuthOAuthView
    authremoteuserview = FerrisAuthRemoteUserView

    registeruserdbview = FerrisRegisterUserDBView
    registeruseroidview = FerrisRegisterUserOIDView
    registeruseroauthview = FerrisRegisterUserOAuthView

    resetmypasswordview = FerrisResetMyPasswordView
    resetpasswordview = FerrisResetPasswordView
    userinfoeditview = FerrisUserInfoEditView

    rolemodelview = FerrisRoleModelView
    permissionmodelview = FerrisPermissionModelView
    userstatschartview = FerrisUserStatsChartView
    viewmenumodelview = FerrisViewMenuModelView
    permissionviewmodelview = FerrisPermissionViewModelView

    user_model = FerrisUser

    def __init__(self, appbuilder):

        super().__init__(appbuilder)

    def register_views(self):
        if not self.appbuilder.get_app.config.get("WORKER_MODE", False):
            super(FerrisSecurityManager, self).register_views()
            self.appbuilder.security_cleanup()
