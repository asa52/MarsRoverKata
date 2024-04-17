from main import Rover


def test_rover_exists():
    rover = Rover()


def test_rover_receives_command():
    rover = Rover()
    rover.receive_command('move')


def test_reports_position():
    rover = Rover()
    position = rover.report_position()
    assert position[0] in ['N', 'S', 'E', 'W']
    assert isinstance(position[1], int)
    assert isinstance(position[2], int)


def test_move_forward():
    rover = Rover()
    current_position = rover.report_position()
    new_position = rover.move('F')

    assert new_position[2] == current_position[2] + 1


def test_move_forward_twice():
    rover = Rover()
    current_position = rover.report_position()
    new_position = rover.move('FF')

    assert new_position[2] == current_position[2] + 2


def test_move_backward():
    rover = Rover()
    current_position = rover.report_position()
    new_position = rover.move('B')

    assert new_position[2] == current_position[2] - 1


def test_move_backward_twice():
    rover = Rover()
    current_position = rover.report_position()
    new_position = rover.move('BB')

    assert new_position[2] == current_position[2] - 2


def test_turn_left():
    rover = Rover()
    new_position = rover.move('L')

    assert new_position[0] == 'W'


def test_turn_left_twice():
    rover = Rover()
    new_position = rover.move('LL')

    assert new_position[0] == 'S'


def test_turn_right():
    rover = Rover()
    new_position = rover.move('R')

    assert new_position[0] == 'E'


def test_get_initial_start():
    rover = Rover(['E', 2, 3])
    assert rover.report_position() == ['E', 2, 3]


def test_size_of_planet_north():
    rover = Rover(['N', 0, 9], size_of_planet=10)
    rover.move('F')
    assert rover.report_position() == ['N', 0, 0]


def test_size_of_planet_backwards():
    rover = Rover(['N', 0, -9], size_of_planet=10)
    rover.move('B')
    assert rover.report_position() == ['N', 0, 0]


def test_size_of_planet_east():
    rover = Rover(['E', 9, 0], size_of_planet=10)
    rover.move('F')
    assert rover.report_position() == ['E', 0, 0]
