from flask import request, jsonify, make_response
from flask_restplus import Namespace, Resource, fields  # type: ignore
from src import db
from .model import User, user_schema, users_schema
from .wrappers import user_required
from src.auth.wrappers import admin_required

api = Namespace('user', description='User related stuff')

user_create_request = api.model('User Create Request', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

user_modify_request = api.model('User Modify Request', {
    'username': fields.String(required=False),
    'password': fields.String(required=False)
})


@api.route('')
class UserListRes(Resource):

    @staticmethod
    @admin_required
    @api.response(200, 'OK')
    def get():
        all_users = User.query.all()
        return users_schema.jsonify(all_users)

    @staticmethod
    @api.expect(user_create_request)
    @api.response(201, 'OK')
    @api.response(400, 'No JSON body found')
    @api.response(401, 'Bad username or password')
    def post():
        if not request.is_json:
            return jsonify(msg='No JSON body found'), 400

        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return make_response(jsonify(msg='Missing username or password'), 401)

        if User.find_by_username(username):
            return make_response(jsonify(msg='User with that username already exists'), 401)

        new_user = User(username, password)

        db.session.add(new_user)
        db.session.commit()
        return make_response(user_schema.jsonify(new_user), 201)


@api.route('/<int:user_id>')
class UserRes(Resource):

    @staticmethod
    @user_required
    @api.response(200, 'OK')
    @api.response(404, 'User not found')
    def get(user_id):
        user = User.find_by_id(user_id)
        if not User:
            return make_response(jsonify(msg='User not found'), 404)

        return user_schema.jsonify(user)

    @staticmethod
    @user_required
    @api.response(204, 'OK')
    @api.response(404, 'User not found')
    def delete(user_id):
        user = User.find_by_id(user_id)
        if not User:
            return make_response(jsonify(msg='User not found'), 404)

        db.session.delete(user)
        db.session.commit()
        return None, 204

    @staticmethod
    @user_required
    @api.expect(user_modify_request)
    @api.response(200, 'OK')
    @api.response(404, 'User not found')
    def put(user_id):
        user = User.find_by_id(user_id)
        if not User:
            return make_response(jsonify(msg='User not found'), 404)

        if request.json['username']:
            user.username = request.json['username']
        if request.json['password']:
            user.set_password(request.json['password'])

        db.session.commit()
        return user_schema.jsonify(user)
