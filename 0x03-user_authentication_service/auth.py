#!/usr/bin/env python3
""" auth module """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ returns a salted hash of the password """
    p_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    h_p = bcrypt.hashpw(p_bytes, salt)
    return h_p


class Auth:
    """ Auth class to interact with the authentication database. """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user """
        db = self._db
        try:
            db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return db.add_user(email, _hash_password(password))
