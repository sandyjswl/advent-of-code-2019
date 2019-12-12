import numpy as np


def read_file():
    with open('day_8.txt', 'r') as f:
        content = f.readlines()
    # print(len(content))
    # print(input_array)
    input_array = list(content[0])
    # print(input_array)
    return input_array


def calculate_curr_pixel(all_layers, i, j):
    all_pizels = []
    for layer in all_layers:
        nd_array = np.array(layer)
        layer = nd_array.reshape(25, 6)
        current_pixel = layer[i][j]
        all_pizels.append(current_pixel)

    # if ("0" in all_pizels and all_pizels.index("0")) < ("1" in all_pizels and all_pizels.index("1")):
    #     return "0"
    # if ("1" in all_pizels and all_pizels.index("1")) < ("0" in all_pizels and all_pizels.index("0")):
    #     return "1"
    # if ("0" in all_pizels and "1" not in all_pizels):
    #     return "0"
    # if ("1" in all_pizels and "0" not in all_pizels):
    #     return "1"
    # return "2"
    white_found = False
    black_found = False
    for i in all_pizels:
        if i == "0" and black_found == False and white_found == False:
            return "0"
        elif i == "1" and black_found == False and white_found == False:
            return "1"
    return "2"


def solve():
    inpu_array = read_file()
    width = 25
    height = 6
    total = width * height
    all_layers = []
    for i in range(0, len(inpu_array), total):
        current_layer = inpu_array[i:i + total]
        print(current_layer)
        nd_array = np.array(current_layer)
        # print(nd_array)
        layer = nd_array.reshape(height, width)
        # print(layer)
        all_layers.append(current_layer)
    lowest_zeroes = 99999
    current_index = -1
    for i in range(len(all_layers)):
        number_of_zeroes = all_layers[i].count('0')
        if number_of_zeroes < lowest_zeroes:
            lowest_zeroes = number_of_zeroes
            current_index = i

    res = all_layers[current_index].count("1") * all_layers[current_index].count("2")
    print(res)

    res = []
    for i in range(25):
        for j in range(6):
            current = calculate_curr_pixel(all_layers, i, j)
            res.append(current)
    
    print(res)
    result = ""
    for r in res:
        result = result + r
    print(result)
    result = result.replace('1', '#')
    result = result.replace('0', ' ')
    # print(result)
    rr = list(result)
    for i in range(0, len(rr), 25):
        temp = rr[i:i + 25]
        print(''.join(temp))
    # print(res)
    # for i in range(0, len(res), total):
    #     current_layer = res[i:i + total]
    #     nd_array = np.array(current_layer)
    #     # print(nd_array)
    #     layer = nd_array.reshape(height, width)
    #     print(layer)
    # all_layers.append(current_layer)


if __name__ == '__main__':
    solve()
