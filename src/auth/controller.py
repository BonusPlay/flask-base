from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt_claims  # type: ignore
from flask_restplus import Namespace, fields, Resource  # type: ignore
from src.user.model import User

api = Namespace('auth', description='Authorization')


login_request = api.model('Login Request', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})


@api.route('/login')
class LoginRes(Resource):

    @staticmethod
    @api.expect(login_request)
    @api.response(200, 'OK')
    @api.response(400, 'Missing parameters')
    @api.response(401, 'Bad username or password')
    def post():
        if not request.is_json:
            return make_response(jsonify(msg='Missing JSON in request'), 400)

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username or not password:
            return make_response(jsonify(msg='Missing username or password'), 400)

        user = User.find_by_username(username)
        if not user or not user.check_password(password):
            return make_response(jsonify(msg='Bad username or password'), 401)

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=user)
        return make_response(jsonify(access_token=access_token), 200)


@api.route('/test')
class ProtectedRes(Resource):
    """
    Protect a view with jwt_required, which requires a valid access token
    in the request to access.
    """
    @staticmethod
    @jwt_required
    @api.response(200, 'OK')
    @api.response(401, 'Unauthorized')
    def get():
        identity = get_jwt_identity()
        claims = get_jwt_claims()
        return make_response(jsonify(identity=identity, claims=claims), 200)
