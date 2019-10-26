from flask import jsonify, make_response
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims  # type: ignore
from src import jwt
from src.user.model import User, Roles
from functools import wraps
from typing import Dict


@jwt.user_claims_loader
def add_claims_to_access_token(user) -> Dict[str, str]:
    """
    Create a function that will be called whenever create_access_token
    is used. It will take whatever object is passed into the
    create_access_token method, and lets us define what custom claims
    should be added to the access token.
    """
    return {'role': user.role}


@jwt.user_identity_loader
def user_identity_lookup(user: User) -> str:
    """
    Create a function that will be called whenever create_access_token
    is used. It will take whatever object is passed into the
    create_access_token method, and lets us define what the identity
    of the access token should be.
    """
    return user.id


def admin_required(fn):
    """
    Here is a custom decorator that verifies the JWT is present in
    the request, as well as insuring that this user has a role of
    `admin` in the access token
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['role'] != Roles.admin:
            return make_response(jsonify(msg='Unauthorized'), 403)
        else:
            return fn(*args, **kwargs)

    return wrapper
