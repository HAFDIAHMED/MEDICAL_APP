import datetime
import logging
from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from .base import Base, AlchemyEncoder, JsonifiableCollection


class RoleUser(Base):
    '''
    CREATE TABLE `role_user` (
      `id` int(11) NOT NULL,
      `user_id` int(11) NOT NULL,
      `role_id` int(11) NOT NULL,
      `created_at` datetime DEFAULT NULL,
      `updated_at` datetime DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    __tablename__ = 'role_user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    role_id = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class User(Base, AlchemyEncoder):
    '''
    CREATE TABLE `users` (
      `id` int(11) NOT NULL,
      `name` varchar(255) DEFAULT NULL,
      `last_name` varchar(255) DEFAULT NULL,
      `display_name` varchar(255) NOT NULL,
      `email` varchar(255) NOT NULL,
      `password` varchar(255) DEFAULT NULL,
      `phone` varchar(255) DEFAULT NULL,
      `country` varchar(255) NOT NULL,
      `date_birth` varchar(50) NOT NULL,
      `remember_token` varchar(100) DEFAULT NULL,
      `confirmation_token` varchar(255) DEFAULT NULL,
      `google2fa_secret` text,
      `wallet` varchar(500) DEFAULT NULL,
      `updates` varchar(50) DEFAULT NULL,
      `login_notification` varchar(50) DEFAULT NULL,
      `userip` varchar(255) NOT NULL,
      `status` smallint(6) NOT NULL,
      `blocked` smallint(6) NOT NULL,
      `created_at` datetime DEFAULT NULL,
      `updated_at` datetime DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    _bcrypt = Bcrypt()

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    display_name = Column(String)
    email = Column(String, unique=True)
    _password = Column('password', String)
    phone = Column(String, unique=True)
    country = Column(String)
    date_birth = Column(String)
    remember_token = Column(String)
    confirmation_token = Column(String)
    google2fa_secret = Column(String)
    login_notification = Column(String)
    userip = Column(String)
    status = Column(Integer)
    blocked = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime)


    @validates('email')
    def validate_email(self, key, value):
        return value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd):
        import sys
        self._password = self._bcrypt.generate_password_hash(passwd, rounds=15).decode('utf-8')

    def check_passwd(self, passwd):
        return self._bcrypt.check_password_hash(self.password, passwd)

    def __eq__(self, other):
        return self.id == other.id

    def _fields_to_expand(self):
        return ['id',
                'email',
                'country_code',
                'country_list',
                'phone',
                'verification_code',
                'name',
                'last_name',
                'account_type',
                'nationality',
                'country',
                'date_birth',
                ]
