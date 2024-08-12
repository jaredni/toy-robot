import json

from fastapi import FastAPI, HTTPException

from robot import Robot
from schema import PlaceSchema

app = FastAPI()

def read_robot():
    robot = open("robot.json", "r")
    data = json.load(robot)

    if not data:
        raise HTTPException(status_code=404, detail="No robot placed yet.")

    return json.loads(data)


def set_robot(data):
    robot = open("robot.json", "w")
    json.dump(data, robot)


@app.post("/place/")
def place_robot(place: PlaceSchema):
    data = place.model_dump_json()
    set_robot(data)

    return place.model_dump(exclude={'orientation_value'})


@app.post("/left/", status_code=204)
def face_left():
    data = read_robot()

    robot = Robot(**data)
    robot.face_left()
    set_robot(robot.get_robot().model_dump_json())


@app.post("/right/", status_code=204)
def face_right():
    data = read_robot()

    robot = Robot(**data)
    robot.face_right()
    set_robot(robot.get_robot().model_dump_json())


@app.post("/move/", status_code=204)
def move_robot():
    data = read_robot()

    robot = Robot(**data)
    robot.move()

    try:
        data = robot.get_robot().model_dump_json()
    except ValueError:
        pass

    set_robot(data)


@app.get("/report/")
def get_report():
    data = read_robot()
    return PlaceSchema(**data).model_dump(exclude={'orientation_value'})
