import json
import redis

from fastapi import FastAPI, HTTPException

from robot import Robot
from schema import PlaceSchema

app = FastAPI()
r = redis.Redis(host='redis', port=6379, db=0)


def get_robot_from_cache():
    robot = r.get('toy-robot')

    if robot is None:
        raise HTTPException(status_code=404, detail="No robot placed yet.")

    return json.loads(robot)


def set_robot(data: dict):
    r.set('toy-robot', data)


@app.post("/place/")
def place_robot(place: PlaceSchema):
    data = place.model_dump_json()
    set_robot(data)

    return place.model_dump(exclude={'orientation_value'})


@app.post("/left/", status_code=204)
def face_left():
    data = get_robot_from_cache()

    robot = Robot(**data)
    robot.face_left()
    r.set('toy-robot', robot.get_robot().model_dump_json())


@app.post("/right/", status_code=204)
def face_right():
    data = get_robot_from_cache()

    robot = Robot(**data)
    robot.face_right()
    r.set('toy-robot', robot.get_robot().model_dump_json())


@app.post("/move/", status_code=204)
def move_robot():
    data = get_robot_from_cache()

    robot = Robot(**data)
    robot.move()

    try:
        data = robot.get_robot().model_dump_json()
    except ValueError:
        pass

    set_robot(data)


@app.get("/report/")
def get_report():
    data = get_robot_from_cache()
    return PlaceSchema(**data).model_dump(exclude={'orientation_value'})
