from starlette.testclient import TestClient
import pytest
from app.main import app


@pytest.fixture(scope='function')
def client():
    with TestClient(app) as client:
        yield client
