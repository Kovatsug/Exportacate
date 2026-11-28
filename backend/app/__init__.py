from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

from .config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Validate production settings
    config[config_name].validate_production()

    db.init_app(app)
    migrate.init_app(app, db)

    # Configure CORS with restricted origins
    cors_origins = app.config.get("CORS_ORIGINS", ["http://localhost:3000"])
    CORS(app, origins=cors_origins, supports_credentials=True)

    # Import models to register them with SQLAlchemy
    from . import models  # noqa: F401

    # Register blueprints (routes) - will be added in future tasks
    # from .routes import api_bp
    # app.register_blueprint(api_bp, url_prefix='/api')

    @app.route("/health")
    def health_check():
        return {"status": "ok", "service": "exportacate-api"}

    return app

