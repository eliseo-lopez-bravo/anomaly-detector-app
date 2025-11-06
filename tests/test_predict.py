from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_predict_valid():
    r = client.post("/predict", json={"values": [0.1, 0.0, -0.1]})
    assert r.status_code == 200
    assert "anomaly_score" in r.json()


def test_predict_invalid():
    # wrong size
    r = client.post("/predict", json={"values": [1.0, 2.0]})
    assert r.status_code == 422