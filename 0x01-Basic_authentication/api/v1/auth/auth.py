#!/usr/bin/env python3
""" Module for API authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requires authentication and returns a bool """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        if path + "/" in excluded_paths:
            return False
        for i in excluded_paths:
            if path.startswith(i.split("*")[0]):
                return False
        if path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header to return a string """
        if request is None:
            return None
        if "Authorization" not in request.headers.keys():
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user that returns a string like object """
        return None
