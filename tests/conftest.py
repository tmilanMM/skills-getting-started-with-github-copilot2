from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide a TestClient for API endpoint tests."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Keep tests isolated by restoring activities after each test."""
    # Arrange: snapshot current in-memory state.
    original_activities = deepcopy(activities)

    yield

    # Assert/cleanup: restore state so tests do not leak mutations.
    activities.clear()
    activities.update(original_activities)
