from flask import Flask
from flask_jwt_extended import JWTManager  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from flask_marshmallow import Marshmallow  # type: ignore
from flask_bcrypt import Bcrypt  # type: ignore
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
