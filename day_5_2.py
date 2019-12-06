def parent_in_sub(orbiters_parent_map, parent):
    for p, orbiters in orbiters_parent_map.items():
        if parent in orbiters:
            return (True, p)
    return (False, -5)


if __name__ == '__main__':

    with open('day_5.txt', 'r') as f:
        content = f.readlines()
    # print(content)
    result = []
    for line in content:
        result.append(line.strip())

    orbiters_parent_map = {}

    for orbit in result:
        parent = orbit.split(")")[0]
        child = orbit.split(")")[1]
        if parent in orbiters_parent_map:
            print("np")
            # orbiters_parent_map[parent].append(child)
            orbiters_parent_map[child] = [parent]
            orbiters_parent_map[child].append(*orbiters_parent_map[parent])
        elif parent_in_sub(orbiters_parent_map, parent)[0] == True:
            orbiters_parent_map[parent_in_sub(orbiters_parent_map, parent)[1]].append(child)
        else:
            print("yes")
            orbiters_parent_map[parent] = []
            orbiters_parent_map[child] = [parent]

    print(orbiters_parent_map)
