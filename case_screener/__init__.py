from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from case_screener.resources.case_resource import CaseResource
from case_screener.config import BaseConfig


API_BLUEPRINT = Blueprint("api", __name__)
api = Api(API_BLUEPRINT)

migrate = Migrate()

SWAGGER_URL = "/api/spec"
API_URL = "/static/swagger.yaml"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "ParaTech-MVP-1"}
)


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
    app.register_blueprint(API_BLUEPRINT)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
