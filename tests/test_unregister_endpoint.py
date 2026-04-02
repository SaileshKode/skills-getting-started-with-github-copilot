def test_unregister_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert f"Unregistered {email} from {activity_name}" in response.json()["message"]

    snapshot = client.get("/activities").json()
    assert email not in snapshot[activity_name]["participants"]


def test_unregister_nonexistent_student_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not_registered@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert "Student is not signed up" in response.json()["detail"]


def test_unregister_invalid_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Club"
    email = "test_student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
