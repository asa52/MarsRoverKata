
from typing import Optional
from operator import add, sub


class Rover():
    def __init__(self, position: Optional[list] = None,
                 size_of_planet: int = 20):
        if position is None:
            position = ['N', 0, 0]
        self.current_position = position
        self.size_of_planet = size_of_planet

    def receive_command(self, command: str):
        pass

    def report_position(self):
        return self.current_position.copy()

    def move(self, directions: str):
        orientations = ['N', 'E', 'S', 'W']
        forward_mapper = {'N': (2, add),
                            'E': (1, add),
                            'S': (2, sub),
                            'W': (1, sub)}

        for command in directions:
            orientation = self.current_position[0]
            direction, operation = forward_mapper[orientation]
            if command == 'F':
                self.current_position[direction] = operation(
                    self.current_position[direction], 1)
                if self.current_position[direction] >= 0:
                    self.current_position[direction] %= self.size_of_planet
                else:
                    self.current_position[direction] %= -self.size_of_planet
            elif command == 'B':
                self.current_position[direction] = operation(
                    self.current_position[direction], -1)
                if self.current_position[direction] >= 0:
                    self.current_position[direction] %= self.size_of_planet
                else:
                    self.current_position[direction] %= -self.size_of_planet
            elif command == 'L':
                orientation_idx = orientations.index(orientation)
                self.current_position[0] = orientations[orientation_idx - 1]
            elif command == 'R':
                orientation_idx = orientations.index(orientation)
                self.current_position[0] = orientations[(orientation_idx + 1) % len(orientations)]

        return self.current_position

