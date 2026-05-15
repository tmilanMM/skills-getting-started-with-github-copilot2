from src.app import activities


REQUIRED_ACTIVITY_KEYS = {
    "description",
    "schedule",
    "max_participants",
    "participants",
}


def test_get_activities_returns_200(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_expected_activities(client):
    # Arrange
    endpoint = "/activities"
    expected_names = set(activities.keys())

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert set(payload.keys()) == expected_names


def test_each_activity_has_required_shape(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    for activity_name, activity_data in payload.items():
        assert set(activity_data.keys()) == REQUIRED_ACTIVITY_KEYS, activity_name
        assert isinstance(activity_data["description"], str), activity_name
        assert isinstance(activity_data["schedule"], str), activity_name
        assert isinstance(activity_data["max_participants"], int), activity_name
        assert isinstance(activity_data["participants"], list), activity_name
