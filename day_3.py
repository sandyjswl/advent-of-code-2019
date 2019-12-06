from dataclasses import dataclass

from intersection import get_intersect, does_intersect


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_intersected = False
        self.intersection_point = (0, 0)

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


def find_and_set_intersection(first_1):
    if not first_1.is_intersected:
        first_1.is_intersected = True
        first_1.intersection_point = (first_1.x, first_1.y)


def set_intersections(first_1, first_2, second_1, second_2):
    find_and_set_intersection(first_1)
    find_and_set_intersection(first_2)
    find_and_set_intersection(second_1)
    find_and_set_intersection(second_2)


def get_last_total(param, param1, intersection_point_value):
    if param.x == param1.x:
        return abs(param.y - intersection_point_value[1])
    elif param.y == param1.y:
        return abs(param.x - intersection_point_value[0])


def get_steps(fir_wire_coordinates, end_index, intersection_point_value):
    for i in range(0, end_index + 1):
        print(fir_wire_coordinates[i])
    total = fir_wire_coordinates[0].x + fir_wire_coordinates[0].y
    # total = 0
    for i in range(0, end_index - 1):
        current = fir_wire_coordinates[i]
        next = fir_wire_coordinates[i + 1]

        if current.is_intersected:
            x_val_current = current.intersection_point[0]
            y_val_current = current.intersection_point[1]
        else:
            x_val_current = current.x
            y_val_current = current.y
        if next.is_intersected:
            x_val_next = next.intersection_point[0]
            y_val_next = next.intersection_point[1]
        else:
            x_val_next = next.x
            y_val_next = next.y
        if x_val_current == x_val_next and y_val_current == y_val_next:
            total = total + 0
        if x_val_current == x_val_next and y_val_current != next.y:
            total = total + abs(y_val_current - next.y)
        if x_val_current != x_val_next and y_val_current == next.y:
            total = total + abs(x_val_current - x_val_next)
        if x_val_current != x_val_next and y_val_current != next.y:
            total = total + abs(x_val_current - x_val_next) + (y_val_current - next.y)
        # total = total + min(abs(fir_wire_coordinates[end_index - 1] - intersection_point_value),
        #                     abs(fir_wire_coordinates[end_index] - intersection_point_value))
    last_total = get_last_total(fir_wire_coordinates[end_index - 1], fir_wire_coordinates[end_index],
                                intersection_point_value)
    print("tot", str(last_total))
    total = total + last_total
    return total


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
    steps = []
    for i in range(len(fir_wire_coordinates) - 1):
        for j in range(len(second_wrie_coordinates) - 1):
            first_1 = fir_wire_coordinates[i]
            first_2 = fir_wire_coordinates[i + 1]

            second_1 = second_wrie_coordinates[j]
            second_2 = second_wrie_coordinates[j + 1]
            intersect = does_intersect(first_1, first_2, second_1, second_2)
            if intersect:
                intersect = get_intersect(first_1.to_tuple(), first_2.to_tuple(), second_1.to_tuple(),
                                          second_2.to_tuple())
                set_intersections(first_1, first_2, second_1, second_2)
                print(intersect)
                first_wire_steps = get_steps(fir_wire_coordinates, i + 1, intersect)
                print(20 * "- -")
                second_wire_steps = get_steps(second_wrie_coordinates, j + 1, intersect)
                steps.append(first_wire_steps + second_wire_steps)
                result.append(intersect)
                print(30 * "- -")
    ans = map(manhattan_distance, result)
    # print(min(ans))
    print(steps)
    print(min(steps))


if __name__ == '__main__':
    solve()
