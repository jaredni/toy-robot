from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_place_robot():
    response = client.post("/place/", json={"x_coord": 0, "y_coord": 0, "orientation": "NORTH"})
    assert response.status_code == 200
    assert response.json() == {"x_coord": 0, "y_coord": 0, "orientation": "NORTH"}


def test_face_left():
    client.post("/place/", json={"x_coord": 0, "y_coord": 0, "orientation": "NORTH"})

    response = client.post("/left/")
    assert response.status_code == 204

    response = client.get("/report/")
    assert response.json() == {"x_coord": 0, "y_coord": 0, "orientation": "WEST"}


def test_face_right():
    client.post("/place/", json={"x_coord": 0, "y_coord": 0, "orientation": "NORTH"})

    response = client.post("/right/")
    assert response.status_code == 204

    response = client.get("/report/")
    assert response.json() == {"x_coord": 0, "y_coord": 0, "orientation": "EAST"}


def test_move():
    client.post("/place/", json={"x_coord": 0, "y_coord": 0, "orientation": "NORTH"})

    response = client.post("/move/")
    assert response.status_code == 204

    response = client.get("/report/")
    assert response.json() == {"x_coord": 0, "y_coord": 1, "orientation": "NORTH"}
