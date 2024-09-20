#!/usr/bin/env python3
""" Module for API authentication """

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class SessionAuth(Auth):
    """ Session Authentication class """
