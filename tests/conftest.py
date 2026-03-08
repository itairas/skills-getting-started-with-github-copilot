import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client() -> TestClient:
    """Provide a clean TestClient with reset in-memory activity data per test."""
    # Arrange: reset mutable global state to avoid cross-test coupling.
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))

    # Act: create the API client used by each test.
    with TestClient(app) as test_client:
        # Assert: fixture yields a ready client for the test.
        yield test_client
