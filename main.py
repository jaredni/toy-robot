import json
import redis

from typing import Union

from fastapi import FastAPI

from robot import Robot
from schema import PlaceSchema

app = FastAPI()
r = redis.Redis(host='redis', port=6379, db=0)

def get_robot_from_cache():
    robot = r.get('toy-robot')

    if robot is None:
        return {"error": "No robot placed yet."}

    return json.loads(robot)


@app.post("/place/")
def place_robot(place: PlaceSchema):
    data = place.model_dump_json()
    r.set('toy-robot', data)

    return place.model_dump(exclude={'orientation_value'})


@app.post("/left/")
def face_left():
    data = get_robot_from_cache()

    robot = Robot(**data)
    robot.face_left()
    r.set('toy-robot', robot.get_robot().model_dump_json())

    return {"message": "Robot faced left."}


@app.post("/right/")
def face_right():
    data = get_robot_from_cache()

    robot = Robot(**data)
    robot.face_right()
    r.set('toy-robot', robot.get_robot().model_dump_json())

    return {"message": "Robot faced right."}


@app.post("/move/")
def move_robot():
    data = get_robot_from_cache()

    robot = Robot(**data)
    robot.move()

    try:
        data = robot.get_robot().model_dump_json()
    except ValueError:
        return {"error": "Command Ignored. Robot will fall off the table."}

    r.set('toy-robot', data)
    return {"message": "Robot moved."}


@app.get("/report/")
def get_report():
    data = get_robot_from_cache()
    return PlaceSchema(**data).model_dump(exclude={'orientation_value'})
