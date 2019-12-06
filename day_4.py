def adjacent_present(number):
    number = str(number)
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            return True
    return False


def non_decreasing(number):
    number = str(number)
    last_digit = 0
    for i in range(len(number)):
        if int(int(number[i])) < last_digit:
            return False
        elif int(number[i]) >= last_digit:
            last_digit = int(number[i])
    return True


def twice_adjacent(number):
    number = str(number)
    pairs = {}
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            if number[i] not in pairs:
                pairs[number[i]] = 2
            elif number[i] in pairs:
                pairs.pop(number[i])

    for k, v in pairs.items():
        count = number.count(k)
        if count == 2:
            return True
    return False


def is_valid():
    start = 138241
    end = 674035
    part_1 = []
    part_2 = []
    for i in range(start, end):
        if adjacent_present(i) and non_decreasing(i):
            part_1.append(i)
    for i in range(start, end):
        if adjacent_present(i) and non_decreasing(i) and twice_adjacent(i):
            part_2.append(i)

    print(len(set(part_1)))
    print(len(set(part_2)))


if __name__ == '__main__':
    # print(adjacent_present(111122) and non_decreasing(111122) and twice_adjacent(111122))
    # print(adjacent_present(123444) and non_decreasing(123444) and twice_adjacent(123444))
    # print(adjacent_present(112233) and non_decreasing(112233) and twice_adjacent(112233))
    is_valid()
