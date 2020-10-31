import contextlib
import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from shifaa.db.constants import CONSTANTS
from shifaa.db.models import Base

LOGGER = logging.getLogger(__file__)
LOGGER.setLevel(logging.WARN)


class DataSource:
    def __init__(self,
                 schema='postgresql+psycopg2',
                 host='localhost',
                 port=5432,
                 password=None,
                 user=None,
                 database: str = None,
                 is_test=False):
        self.schema = schema
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database.lower()
        self.is_test = is_test

    def engine(self):
        if not self.is_test and not all([self.host, self.database, self.password, self.port,
                                         self.user]):
            raise ValueError('Please specify the database connection')
        if self.is_test:
            return create_engine(f'sqlite:////tmp/{self.database.lower()}.db')
        return create_engine(
            f"{self.schema}://{self.user}:{self.password}"
            "@"
            f"{self.host}:{self.port}"
            "/"
            f"{self.database}"
        )

    @contextlib.contextmanager
    def session(self) -> Session:
        """Provide a transactional scope around a series of operations."""
        session = sessionmaker(self.engine(), expire_on_commit=False)()
        try:
            yield session
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            # TODO: What should we expect to see in this expunge
            session.expunge_all()
            session.close()


_DataSource = DataSource(
    schema='postgresql+psycopg2',
    host='db-shifaa',
    database=os.getenv('DATABASE_NAME', 'postgres'),
    password=os.getenv('DATABASE_PASSWORD', 'example'),
    port=int(os.getenv('DATABASE_PORT', 5432)),
    user=os.getenv('DATABASE_USER', 'postgres'))


def get_data_source(source='local-test', is_test=False):
    # TODO : Do we want to keep the model like this ?
    assert source, 'Source should not be None'
    is_test = os.getenv('PYTEST_CURRENT_TEST', '')
    if not is_test and source:
        return _DataSource
    else:
        return DataSource(database=source, is_test=is_test)


def setup_db():
    # TODO : Find a way to change this: This is so ugly to be
    #  kept like this.
    with get_data_source().session() as sess:
        Base.metadata.create_all(bind=sess.get_bind())
        for constant in CONSTANTS:
            for cst_string in filter(lambda x: not (x.startswith('_') or x.startswith('get')), dir(constant)):
                cst = getattr(constant, cst_string, None)
                previous = (sess
                            # TODO : Very bad idea to use this kind of reflection
                            #  in the code. We should change it to better code
                            .query(constant.get_class_source())
                            .filter(constant.get_class_source().name == cst.name)
                            .one_or_none())
                if previous:
                    cst = previous
                else:
                    sess.add(cst)
                sess.commit()
                setattr(constant, cst_string, cst)
