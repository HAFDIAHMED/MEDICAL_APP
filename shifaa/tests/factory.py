import factory

import shifaa.db.models as models


class UserFactory(factory.Factory):
    class Meta:
        model = models.User
