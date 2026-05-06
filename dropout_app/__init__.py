from flask import Flask

from .config import Config
from .model_service import PredictionService
from .routes import dashboard_bp


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    app.config.from_object(config_class)
    app.prediction_service = PredictionService(app.config["MODEL_PATH"])
    app.register_blueprint(dashboard_bp)
    return app
