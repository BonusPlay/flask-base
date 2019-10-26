from flask import Blueprint
from flask_restplus import Api  # type: ignore

from src import app, db
from src.auth.controller import api as ns_auth
from src.health.controller import api as ns_health
from src.user.controller import api as ns_user

db.create_all()

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, version='1.0')

api.add_namespace(ns_auth)
api.add_namespace(ns_health)
api.add_namespace(ns_user)
app.register_blueprint(blueprint)

app.run(debug=True)
