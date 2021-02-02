from app.config.settings import settings


def test_get_hello(client):
    response = client.get(f"{settings.API_V1}/users")
    assert response.status_code == 200