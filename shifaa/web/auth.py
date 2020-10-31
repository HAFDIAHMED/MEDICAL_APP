from flask import g as local
from flask_restplus import Resource
from flask_httpauth import HTTPTokenAuth
import shifaa.db.engine as engine

_AUTH = HTTPTokenAuth()


@_AUTH.verify_token
def verify_token(token):
    user = engine.authenticate_token(token)
    setattr(local, "current_user", user)
    return True


# @_AUTH.login_required
class ProtectedResource(Resource):
    @_AUTH.login_required
    def dispatch_request(self, *args, **kwargs):
        # self.method_decorators.append(_AUTH.login_required)
        return super().dispatch_request(local.current_user, *args, **kwargs)
