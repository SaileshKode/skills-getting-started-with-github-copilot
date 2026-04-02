import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """FastAPI TestClient fixture."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def activities_snapshot():
    """Reset activities state before and after each test."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
