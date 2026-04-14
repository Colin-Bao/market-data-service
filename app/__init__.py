"""Market Data Service - Flask application factory."""
from flask import Flask, jsonify
from flasgger import Swagger


def create_app(config=None):
    """Create Flask application instance.

    Args:
        config: Optional configuration dict

    Returns:
        Flask app instance
    """
    app = Flask(__name__)

    # Default configuration
    app.config["TESTING"] = config.get("TESTING", False) if config else False
    app.config["API_KEY"] = config.get("API_KEY", "") if config else ""

    # Swagger configuration
    app.config["SWAGGER"] = {
        "title": "Market Data Service API",
        "version": "1.0.0",
        "uiversion": 3,
    }
    Swagger(app)

    # Health check endpoint
    @app.route("/health")
    def health():
        """Health check endpoint.

        Returns service status.
        ---
        responses:
          200:
            description: Service is healthy
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: ok
        """
        return jsonify({"status": "ok"})

    # Register blueprints (placeholder)
    # from app.routes.weather import weather_bp
    # from app.routes.prices import prices_bp
    # from app.routes.duos import duos_bp
    # app.register_blueprint(weather_bp, url_prefix="/api/v1/weather")
    # app.register_blueprint(prices_bp, url_prefix="/api/v1/prices")
    # app.register_blueprint(duos_bp, url_prefix="/api/v1/duos")

    return app