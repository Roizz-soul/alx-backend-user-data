#!/usr/bin/env python3
""" Module for session expiration """

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from models.user import User
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Expiration Authentication class """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None):
        """ Creates a Session """
        sess_id = super().create_session(user_id)
        if sess_id is None:
            return None
        self.user_id_by_session_id[sess_id] = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        return sess_id

    def user_id_for_session_id(self, session_id: str = None):
        """ Returns user id based on session id """

        if session_id is None:
            return None
        if self.user_id_by_session_id.get(session_id) is None:
            return None
        sess_key = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return sess_key['user_id']
        if sess_key.get('created_at') is None:
            return None
        time_span = timedelta(seconds=self.session_duration)
        check = sess_key.get('created_at') + time_span
        if check < datetime.now():
            return None
        return sess_key['user_id']
