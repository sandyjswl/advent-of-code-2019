import copy


def read_input():
    with open('input_2.txt', 'r') as f:
        content = f.readlines()
    # print(content)
    inputs = content[0].split(",")
    inputs = [int(x) for x in inputs]
    return inputs


def replace_numbers(inputs_array, noun, verb):
    inputs_array[1] = noun
    inputs_array[2] = verb
    return inputs_array


def add_numbers(array, index):
    current_index = copy.deepcopy(index)
    first_pos = array[current_index + 1]
    second_pos = array[current_index + 2]
    result_pos = array[current_index + 3]
    sum_of_values = array[first_pos] + array[second_pos]
    array[result_pos] = sum_of_values
    # print(array)
    return array


def multiply_numbers(array, index):
    current_index = copy.deepcopy(index)
    first_pos = array[current_index + 1]
    second_pos = array[current_index + 2]
    result_pos = array[current_index + 3]
    sum_of_values = array[first_pos] * array[second_pos]
    array[result_pos] = sum_of_values
    # print(array)
    return array


def solve(noun, verb):
    inputs_array = read_input()
    replaced_numbers = replace_numbers(inputs_array, noun, verb)
    index = 0
    while True:
        # print(index)
        op_code = replaced_numbers[index]
        if op_code == 99:
            break
        elif op_code == 1:
            add_numbers(replaced_numbers, index)

        elif op_code == 2:
            multiply_numbers(replaced_numbers, index)
        index = index + 4
    ans = replaced_numbers[0]
    if ans == 19690720:
        print(noun, verb)


def solve_2():
    for i in range(1, 100):
        for j in range(1, 100):
            solve(i, j)


if __name__ == '__main__':
    solve_2()
