import pytest

import shifaa.db.constants as constants
import shifaa.db.engine as engine
import shifaa.db.models as models


def test_authenticate_user(user: models.User, ds):
    with ds.session() as sess:
        sess.add(user)
