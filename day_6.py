def find_parents_length(child, orbiters_parent_map):
    parents_length = 0
    while True:
        child = orbiters_parent_map.get(child, False)
        if not child:
            break
        else:
            parents_length = parents_length + 1
    return parents_length


def find_all_parents(parent_of_you, orbiters_parent_map):
    parents = []
    while True:
        parent_of_you = orbiters_parent_map.get(parent_of_you, False)
        if parent_of_you == False:
            break
        else:
            parents.append(parent_of_you)
    return parents


if __name__ == '__main__':
    with open('day_6.txt', 'r') as f:
        content = f.readlines()
    map_data = []
    for line in content:
        map_data.append(line.strip())

    orbiters_parent_map = {}
    all_orbits = set()
    for orbit in map_data:
        parent = orbit.split(")")[0]
        child = orbit.split(")")[1]
        orbiters_parent_map[child] = parent
        all_orbits.add(parent)
        all_orbits.add(child)
    checksum = 0
    for orbit in all_orbits:
        checksum = checksum + find_parents_length(orbit, orbiters_parent_map)
    print("PART-1 ->", str(checksum))
    parent_of_you = orbiters_parent_map.get("YOU")
    parent_of_san = orbiters_parent_map.get("SAN")
    parents_of_you = find_all_parents(parent_of_you, orbiters_parent_map)
    parents_of_san = find_all_parents(parent_of_san, orbiters_parent_map)
    common_parents = []
    for i in parents_of_you:
        if i in parents_of_san:
            current_index = parents_of_you.index(i)
            santa_index = parents_of_san.index(i)
            common_parents.append(current_index + santa_index)
    print("PART-2 ->", str(min(common_parents) + 2))
