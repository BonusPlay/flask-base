# Flask-base

![GitHub Actions status | BonusPlay/flask-base](https://github.com/BonusPlay/flask-base/workflows/Python%20application/badge.svg)

This is a _base_ repository containing easily extendable backend server.

### Features
 - ORM - [flask_sqlalchemy](https://pypi.org/project/Flask-SQLAlchemy/)
 - Request/Response marshalling - [flask_marshmallow](https://pypi.org/project/flask-marshmallow/)
 - JWT authentication - [flask_jwt_extended](https://pypi.org/project/Flask-JWT-Extended/)
 - auto-generated swagger docs - [flask_restplus](https://pypi.org/project/flask-restplus/)
 - static typing (kinda) - [mypy](https://pypi.org/project/mypy/)
 - unit tests - [unittest](https://docs.python.org/3/library/unittest.html)
 - test coverage - [coverage](https://pypi.org/project/coverage/)
 
### How to run:
 - create virtualenv
 - install dependencies
 - modify `src/config.py`
 - `python -m src`
 - ???
 - Profit

### Run unit tests and coverage
 - `coverage run --source=src -m unittest discover`
 - `coverage html -i`
 - open `htmlcov/index.html`

### How to extend:
 - add more restplus resources
 - import them in `src/__main__.py`
 - write unit tests
 - visit your swagger docs at `/api/v1`
