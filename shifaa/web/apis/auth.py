from flask_restplus import Resource, Namespace, reqparse

import shifaa.db.engine as engine
from shifaa.web.validators import EmailValidator

AUTH_NS = Namespace('auth')


@AUTH_NS.route('/login')
class LoginResource(Resource):
    def _get_post_req(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('email', type=EmailValidator, required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('g_recaptcha_response', required=True)
        return parser.parse_args(strict=True)

    def post(self):
        # Create a new portfolio
        # Todo : Do something with the parsed data :)
        req = self._get_post_req()
        user, token, profil = engine.authenticate_user(req.email, req.password)
        if token:
            return {
                'status': True,
                'token': token,
            }
        return {'message': 'Error with password or usename', 'status': False}, 401


@AUTH_NS.route('/register')
class RegisterResource(Resource):
    def post(self):
        user = engine.add_user("marouane.benalla@gmail.com", password="tototototo")
        return {'status': True, 'user': user.dict()}


@AUTH_NS.route('/password/email')
class PasswordResetRequestResource(Resource):
    def post(self):
        pass


@AUTH_NS.route('/password/reset')
class PasswordResetResource(Resource):
    def post(self):
        pass
