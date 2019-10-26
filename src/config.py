class Config(object):
    SECRET_KEY = "hunter2"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../flask_base.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    RESTPLUS_VALIDATE = True
