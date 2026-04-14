"""Tests for Market Data Service."""
import pytest
from app import create_app


@pytest.fixture
def app():
    """Create test Flask app."""
    app = create_app({"TESTING": True})
    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    def test_health_returns_ok(self, client):
        """Test health endpoint returns ok status."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "ok"

    def test_health_is_json(self, client):
        """Test health endpoint returns JSON."""
        response = client.get("/health")
        assert response.content_type == "application/json"


class TestAppFactory:
    """Tests for Flask app factory."""

    def test_create_app_returns_flask_instance(self):
        """Test create_app returns Flask instance."""
        from flask import Flask
        app = create_app()
        assert isinstance(app, Flask)

    def test_create_app_with_config(self):
        """Test create_app accepts configuration."""
        app = create_app({"TESTING": True})
        assert app.config["TESTING"] is True