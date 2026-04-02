def test_get_activities_returns_expected_structure(client):
    # Arrange
    # (state setup via fixture)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]


def test_root_redirects_to_index(client):
    # Arrange

    # Act
    response = client.get("/", follow_redirects=True)

    # Assert
    assert response.status_code == 200
    assert "Mergington High School" in response.text
