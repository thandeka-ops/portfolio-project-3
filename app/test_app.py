from app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["application"] == "CI/CD Demo Application"
    assert response.get_json()["version"] == "3.0.4"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_version():
    client = app.test_client()
    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json()["version"] == "3.0.4"
