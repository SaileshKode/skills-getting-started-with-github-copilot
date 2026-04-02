def test_signup_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new_student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email} for {activity_name}" in response.json()["message"]

    snapshot = client.get("/activities").json()
    assert email in snapshot[activity_name]["participants"]


def test_signup_existing_student_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_invalid_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Club"
    email = "test_student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
