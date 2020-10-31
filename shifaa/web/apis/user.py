from flask_restplus import Namespace
from flask_restplus.reqparse import RequestParser

import shifaa.db.constants as constants
import shifaa.db.engine as engine
import shifaa.db.models as models
from shifaa.web.auth import ProtectedResource

USER_NS = Namespace('user')


@USER_NS.route('/profile')
class Profile(ProtectedResource):
    def get(self, user):
        # Create a new portfolio
        # Todo : Do something with the parsed data :)
        return {
            'status': True,
            'user': user.dict()
        }