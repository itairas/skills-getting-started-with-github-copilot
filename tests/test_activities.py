def test_get_activities_returns_all_activities_with_expected_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert payload

    for activity_name, activity_data in payload.items():
        assert isinstance(activity_name, str)
        assert required_fields.issubset(activity_data.keys())
        assert isinstance(activity_data["participants"], list)
