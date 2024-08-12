from robot import Robot


class TestRobot:
    def test_face_left(self):
        robot = Robot(0, 0, 0, 'NORTH')
        robot.face_left()
        assert robot.orientation == 'WEST'

    def test_face_right(self):
        robot = Robot(0, 0, 0, 'NORTH')
        robot.face_right()
        assert robot.orientation == 'EAST'

    def test_move(self):
        robot = Robot(0, 0, 0, 'NORTH')
        robot.move()
        assert robot.y_coord == 1

    def test_get_robot(self):
        robot = Robot(0, 0, 0, 'NORTH')
        data = robot.get_robot()
        assert data.x_coord == 0
        assert data.y_coord == 0
        assert data.orientation == 'NORTH'
