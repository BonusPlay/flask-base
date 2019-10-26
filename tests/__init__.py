import unittest
from flask import Blueprint
from flask_restplus import Api  # type: ignore
from src import app, db
from src.auth.controller import api as ns_auth
from src.health.controller import api as ns_health
from src.user.controller import api as ns_user


blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(blueprint, version='1.0')

api.add_namespace(ns_auth)
api.add_namespace(ns_health)
api.add_namespace(ns_user)

app.register_blueprint(blueprint)


class BasicTests(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()

        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        pass

    def get(self, url, **kwargs):
        kwargs['headers'] = {
            'Authorization': f"Bearer {kwargs.pop('jwt', None)}"
        }
        return self.app.get(url, **kwargs)

    def post(self, url, data, **kwargs):
        kwargs['headers'] = {
            'Authorization': f"Bearer {kwargs.pop('jwt', None)}"
        }
        kwargs['json'] = data
        return self.app.post(url, **kwargs)

    def put(self, url, data, **kwargs):
        kwargs['headers'] = {
            'Authorization': f"Bearer {kwargs.pop('jwt', None)}"
        }
        kwargs['json'] = data
        return self.app.put(url, json=data, **kwargs)

    def delete(self, url, **kwargs):
        kwargs['headers'] = {
            'Authorization': f"Bearer {kwargs.pop('jwt', None)}"
        }
        return self.app.delete(url, **kwargs)


if __name__ == '__main__':
    unittest.main()
