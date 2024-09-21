#!/usr/bin/env python3
""" Module for API authentication """

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64
import uuid


class SessionAuth(Auth):
    """ Session Authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session """
        if user_id is None or not isinstance(user_id, str):
            return None
        sess_id = str(uuid.uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns user id based on session id """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a user instance based on a cookie value """
        cooki = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cooki)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes the user session / logout """
        if request is None:
            return False
        sess_id = self.session_cookie(request)
        if sess_id is None:
            return False
        if not self.user_id_for_session_id(sess_id):
            return False
        del self.user_id_by_session_id[sess_id]
