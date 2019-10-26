# Flask-base

This is a _base_ repository containing easily extendable backend server.

### Features
 - ORM - [flask_sqlalchemy](https://pypi.org/project/Flask-SQLAlchemy/)
 - Request/Response marshalling - [flask_marshmallow](https://pypi.org/project/flask-marshmallow/)
 - JWT authentication - [flask_jwt_extended](https://pypi.org/project/Flask-JWT-Extended/)
 - auto-generated swagger docs - [flask_restplus](https://pypi.org/project/flask-restplus/)
 - static typing (kinda) - [mypy](https://pypi.org/project/mypy/)
 
### How to run:
 - create virtualenv
 - install dependencies
 - modify `src/config.py`
 - `python -m src`
 - ???
 - Profit
 
### How to extend:
 - add more restplus resources
 - import them in `src/__main__.py`
 - visit your swagger docs at `/api/v1`