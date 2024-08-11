from pydantic import BaseModel, field_validator, Field, computed_field

from constants import NUM_COLS, NUM_ROWS, ORIENTATION_DISPLAY, ORIENTATION_VALUE


class PlaceSchema(BaseModel):
    x_coord: int
    y_coord: int
    orientation: str

    @field_validator('x_coord')
    def validate_x_coord(cls, v):
        if v not in list(range(0, NUM_COLS)):
            raise ValueError('values must be 0-4')
        return v

    @field_validator('y_coord')
    def validate_y_coord(cls, v):
        if v not in list(range(0, NUM_ROWS)):
            raise ValueError('values must be 0-4')
        return v

    @field_validator('orientation')
    def validate_orientation(cls, v):
        if v not in ORIENTATION_VALUE.keys():
            raise ValueError('values must be NORTH, EAST, SOUTH, or WEST')
        return v

    @computed_field(return_type=int)
    @property
    def orientation_value(self):
        return ORIENTATION_VALUE[self.orientation]
