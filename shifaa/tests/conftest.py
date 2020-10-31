import pytest
import shifaa.db.models.base as base

import shifaa.db.core as core
from .factory import UserFactory

@pytest.fixture('function', name='ds')
def create_global_data_source():
    test_ds = core.get_data_source(is_test=True)

    # In order to avoid having many test files for different database
    # We decided to keep the same files but clean them everytime we relaunch this test
    base.Base.metadata.drop_all(bind=test_ds.engine())

    # Create tables
    core.setup_db()

    # Return
    return test_ds


@pytest.fixture('function', name='user')
def user():
    return UserFactory.build(email='test@bbles.tech', password='tototo')
