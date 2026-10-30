from fastapi.testclient import TestClient

from src.app import app


def test_get_activities_returns_available_activities():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert activities["Chess Club"]["description"]
    assert isinstance(activities["Chess Club"]["participants"], list)
