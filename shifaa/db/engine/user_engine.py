# All the interaction that we may need with our db
import datetime
import logging
import typing

import shifaa.db.constants as constants
import shifaa.db.core as core
import shifaa.db.models as models


# TODO  : Should I explain the reason why some queries may not work as I expect them to work
def add_user(email: str, password: str):
    with (core.get_data_source().session()) as sess:
        user = models.User(email=email)
        user.password = 'tototo'
        sess.add(user)
        return user


def authenticate_user(email: str, password: str) \
        -> typing.Tuple[models.User, str, typing.List[str]]:
    # Todo: Ensure to generate the right token
    user, token, sources = None, None, []
    with (core.get_data_source()
            .session()) as pec_sess:
        user = (pec_sess
                .query(models.User)
                .filter(models.User.email == email)
                .one_or_none())
        if user:
            if not user.check_passwd(password):
                return user


def authenticate_token(token):
    # We should return also from which source the user is comming from to ensure that we are able to connect the user
    with core.get_data_source().session() as sess:
        return sess.query(models.User).first()
