from flask import jsonify, make_response
from flask_restplus import Namespace, Resource  # type: ignore

api = Namespace('health', description='Health endpoints useful for testing')


@api.route('/ping')
class PingRes(Resource):

    @staticmethod
    @api.response(200, 'OK')
    def get():
        return make_response(jsonify(msg='pong'), 200)
