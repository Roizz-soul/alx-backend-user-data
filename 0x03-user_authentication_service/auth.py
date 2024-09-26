#!/usr/bin/env python3
""" auth module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ returns a salted hash of the password """
    p_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    h_p = bcrypt.hashpw(p_bytes, salt)
    return h_p
