#!/usr/bin/env python3
""" Module for API authentication """

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication class """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Returns the base 64 past of the Authorization header """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            None
        else:
            return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Returns the decoded value of a base64 string """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_data = base64.b64decode(
                base64_authorization_header, validate=True
            )
            return decoded_data.decode('utf-8')
        except Exception:
            return None
