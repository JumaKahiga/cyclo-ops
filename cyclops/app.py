"""
Cyclone scraper Flask application
"""
import logging
from flask import Flask, request
from flask_apispec import FlaskApiSpec

import cyclops.settings as app_settings
from cyclops.endpoints.health import health

SERVICE_NAME = 'cyclops'
docs = FlaskApiSpec()


def create_app(**config_overrides):
    """Create Flask app instance."""
    logger = logging.getLogger(__name__)
    app = Flask(SERVICE_NAME)
    app.config.from_object(app_settings)
    app.config.update(config_overrides)

    app.register_blueprint(health)

    @app.errorhandler
    def handle_generic_error(err):
        """Generic error handler."""

        logger.exception('Application Exception',
                         extra={'flask_request': request})

    if not app.testing:
        docs.init_app(app)
        docs.register_existing_resources()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
