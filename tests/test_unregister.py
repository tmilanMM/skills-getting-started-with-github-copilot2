from src.app import activities


def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    endpoint = f"/activities/{activity_name}/unregister"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Underwater Robotics Club"
    email = "new.student@mergington.edu"
    endpoint = f"/activities/{activity_name}/unregister"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_missing_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.enrolled@mergington.edu"
    endpoint = f"/activities/{activity_name}/unregister"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found in this activity"}
