from dataclasses import dataclass

from intersection import get_intersect, does_intersect


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def to_tuple(self):
        return (self.x, self.y)


def get_coordinates(current_location: Coordinates, move):
    if move[0] == "R":
        x_coordinates = current_location.x + int(move[1:])
        y_coordinates = current_location.y
        return Coordinates(x_coordinates, y_coordinates)
    elif move[0] == "U":
        x_coordinates = current_location.x
        y_coordinates = current_location.y + int(move[1:])
        return Coordinates(x_coordinates, y_coordinates)
    elif move[0] == "L":
        x_coordinates = current_location.x - int(move[1:])
        y_coordinates = current_location.y
        return Coordinates(x_coordinates, y_coordinates)
    elif move[0] == "D":
        x_coordinates = current_location.x
        y_coordinates = current_location.y - int(move[1:])
        return Coordinates(x_coordinates, y_coordinates)


def read_input():
    with open('input_3.txt', 'r') as f:
        content = f.readlines()
    # print(content)
    first_wire = content[0].split(",")
    first_wire[-1] = first_wire[-1].strip()
    second_wire = content[1].split(",")
    return [first_wire, second_wire]


def find_distance(res: Coordinates):
    return abs(res.x) + abs(res.y)


def manhattan_distance(args):
    return abs(args[0]) + abs(args[1])


def solve():
    inputs = read_input()
    first_wire = inputs[0]
    second_wire = inputs[1]
    fir_wire_coordinates = []
    current_location = Coordinates(0, 0)
    # fir_wire_coordinates.append(current_location)
    for location in first_wire:
        current_location = get_coordinates(current_location, location)
        fir_wire_coordinates.append(current_location)
    second_wrie_coordinates = []
    current_location = Coordinates(0, 0)
    # second_wrie_coordinates.append(current_location)
    for location in second_wire:
        current_location = get_coordinates(current_location, location)
        second_wrie_coordinates.append(current_location)

    # print(len(fir_wire_coordinates), len(first_wire))
    # print(len(second_wrie_coordinates), len(second_wire))
    result = []

    for i in range(len(fir_wire_coordinates) - 1):
        for j in range(len(second_wrie_coordinates) - 1):
            first_1 = fir_wire_coordinates[i]
            first_2 = fir_wire_coordinates[i + 1]

            second_1 = second_wrie_coordinates[j]
            second_2 = second_wrie_coordinates[j + 1]
            intersect = does_intersect(first_1, first_2, second_1, second_2)
            if intersect != False:
                intersect = get_intersect(first_1.to_tuple(), first_2.to_tuple(), second_1.to_tuple(),
                                          second_2.to_tuple())
                print(intersect)
                result.append(intersect)
    ans = map(manhattan_distance, result)
    print(min(ans))


if __name__ == '__main__':
    solve()
