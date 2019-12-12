import copy


def read_input():
    with open('day_5.txt', 'r') as f:
        content = f.readlines()
    # print(content)
    inputs = content[0].split(",")
    inputs = [int(x) for x in inputs]
    return inputs


# TRUE = IMMEDIATE_MODE
def replace_numbers(inputs_array, noun, verb):
    inputs_array[1] = noun
    inputs_array[2] = verb
    return inputs_array


def add_numbers(array, index):
    current_index = copy.deepcopy(index)
    first_pos = array[current_index + 1]
    second_pos = array[current_index + 2]
    result_pos = array[current_index + 3]
    print(first_pos, second_pos)
    print("pos")
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


def save_to_position(array, the_integer, the_position):
    # current_index = copy.deepcopy(index)
    # the_integer = array[current_index + 1]
    # the_position = array[current_index + 2]

    array[the_position] = the_integer
    return array


def display_from_position(array, index):
    current_index = copy.deepcopy(index)
    value = array[current_index + 1]
    print(value)
    return value


def get_all_parameters(parameterss):
    op_code = parameterss[-2:]
    rest_params = parameterss[:-2]
    # params = list(rest_params)
    if len(rest_params) == 0:
        return [op_code] + [0, 0, 0]
    if len(rest_params) == 1:
        return [op_code] + [0, 0, int(rest_params)]
    if len(rest_params) == 2:
        return [op_code] + [0, int(rest_params[0]), int(rest_params[1])]
    if len(rest_params) == 3:
        return map(int, list(rest_params))


def add_numbers_second_part(array, index):
    pass


def get_data_using_mode(array, param, mode=0):
    if mode == 1:
        return param
    return array[param]


def second_part(array, index):
    params = array[index]
    parameterss = str(params)
    # op_code_and_params = get_all_parameters(parameterss)
    # op_code = op_code_and_params[0]
    # print(parameterss)
    if (len(parameterss)) > 2:
        print(parameterss)
        op_code, param_3_mode, param_2_mode, param_1_mode = get_all_parameters(parameterss)
    else:
        op_code = array[index]
        param_3_mode = param_2_mode = param_1_mode = 0
    # print(op_code, param_1_mode, param_2_mode, param_3_mode)
    if op_code == 99:
        print("FOUND 99")
    elif int(op_code) == 1:
        param_1 = array[index + 1]
        param_2 = array[index + 2]
        result_param = array[index + 3]

        param_1 = get_data_using_mode(array, param_1, param_1_mode)
        param_2 = get_data_using_mode(array, param_2, param_2_mode)
        res_pos = get_data_using_mode(array, result_param, param_3_mode)
        array[result_param] = param_1 + param_2

    elif int(op_code) == 2:
        param_1 = array[index + 1]
        param_2 = array[index + 2]
        result_param = array[index + 3]
        # print(result_param)
        # print(param_3_mode)
        param_1 = get_data_using_mode(array, param_1, param_1_mode)
        param_2 = get_data_using_mode(array, param_2, param_2_mode)
        res_pos = get_data_using_mode(array, result_param, param_3_mode)
        # print(param_1, param_2, res_pos)
        array[result_param] = param_1 * param_2

    elif int(op_code) == 4:
        param_1 = array[index + 1]
        param_1 = get_data_using_mode(array, param_1, param_1_mode)
        display_from_position(array, param_1)

    elif op_code == 3:
        param_1 = array[index + 1]
        param_1 = get_data_using_mode(array, param_1)
        save_to_position(array, 1, param_1)


def solve():
    inputs_array = read_input()
    # op_code = inputs_array[0]
    # value = 1
    # position = inputs_array[1]
    # array = save_to_position(inputs_array, value, position)
    # index = 2
    array = inputs_array
    index = 0
    while True:
        # print(index)
        op_code = array[index]
        second_part(array, index)
        if len(str(op_code))==1:
            index = index+4
        else:
            index = index + len(str(op_code))
        print(array)


if __name__ == '__main__':
    solve()
