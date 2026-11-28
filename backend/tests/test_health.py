"""Basic health check tests to verify test infrastructure."""

from flask.testing import FlaskClient


def test_health_endpoint(client: FlaskClient):
    """Test that the health endpoint returns OK."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "exportacate-api"