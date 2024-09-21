#!/usr/bin/env python3
""" Module of Session Auth views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Login function """
    email = request.form.get("email")
    passwd = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not passwd:
        return jsonify({"error": "password missing"}), 400

    user_list = User.search({"email": email})
    if not user_list or len(user_list) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_list[0]
    if not user.is_valid_password(passwd):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth

    sess_id = auth.create_session(user.id)
    res = jsonify(user.to_json())
    res.set_cookie(os.getenv("SESSION_NAME"), sess_id)
    return res
