def read_file():
    with open('day_7.txt', 'r') as f:
        content = f.readlines()
    map_data = []
    for line in content:
        map_data.append(line.strip())
    return map_data


if __name__ == '__main__':
    inputs = read_file()
