from constants import north_value, east_value, south_value, west_value, ORIENTATION_DISPLAY

from schema import PlaceSchema

class Robot:
    def __init__(self, x_coord, y_coord, orientation_value, orientation):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.orientation_value = orientation_value
        self.orientation = orientation

    def face_left(self):
        new_orientation = (self.orientation_value - 1) % 4
        self.orientation = ORIENTATION_DISPLAY[new_orientation]

    def face_right(self):
        new_orientation = (self.orientation_value + 1) % 4
        self.orientation = ORIENTATION_DISPLAY[new_orientation]

    def move(self):
        if self.orientation_value == north_value:
            self.y_coord += 1
        elif self.orientation_value == east_value:
            self.x_coord += 1
        elif self.orientation_value == south_value:
            self.y_coord -= 1
        elif self.orientation_value == west_value:
            self.x_coord -= 1

    def get_robot(self):
        data = {
            "x_coord": self.x_coord,
            "y_coord": self.y_coord,
            "orientation": self.orientation
        }

        return PlaceSchema(**data)
