#!/usr/bin/env python3
""" Module for API authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requires authentication and returns a bool """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header to return a string """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user that returns a string like object """
        return None
