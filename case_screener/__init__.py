from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_restful import Api
from case_screener.resources.case_resource import CaseResource
from case_screener.config import BaseConfig

api_bp = Blueprint("api", __name__)
api = Api(api_bp)
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)
    if not config:
        app.config.from_object(BaseConfig)
    else:
        app.config.from_object(config)

    # database config
    from case_screener.models import db

    db.init_app(app)

    # database migrations config
    migrate.init_app(app, db)

    # Restful config
    api.add_resource(CaseResource, "/case")

    # Blueprint config
    app.register_blueprint(api_bp)

    return app
