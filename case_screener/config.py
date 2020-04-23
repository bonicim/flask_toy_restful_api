import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    CSRF_ENABLED = True


class DevelopmentConfig(BaseConfig):
    TESTING = True


class TestingConfig(BaseConfig):
    TESTING = True
