from functools import wraps
from flask import make_response, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt_claims  # type: ignore
from .model import Roles


def user_required(fn):
    """
    This wrapper allows endpoints to be only executed by specified user_id
    (or multiple user_ids) or admins. It requires parent function to be called with
    `user_id` kwarg.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        claims = get_jwt_claims()
        if Roles.admin == claims['role'] or identity == kwargs['user_id']:
            return fn(*args, **kwargs)
        else:
            return make_response(jsonify(msg='Unauthorized'), 403)

    return wrapper
