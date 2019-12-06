with open("day_6.txt") as f:
    data = [l.strip() for l in f.readlines()]

orbits = {}
r_orbits = {}
planets = set()
for orbit in data:
    a = orbit.split(")")
    orbits[a[1]] = a[0]
    if a[0] in r_orbits:
        r_orbits[a[0]].append(a[1])
    else:
        r_orbits[a[0]] = [a[1]]
    for p in a:
        planets.add(p)


def orbit_walker(planet, nr=0):
    if planet == "COM":
        return nr
    parent = orbits[planet]
    return orbit_walker(parent, nr + 1)


p1_checksum = sum(list(map(orbit_walker, planets)))
print(f"PART 1: {p1_checksum}")

visited = set()
nodes = [("YOU", 0)]
distances = set()
while len(visited) < len(planets) - 1:  # -1 to ignore the COM root node
    node = nodes.pop()
    if node[0] == "SAN":
        distances.add(node[1] - 2)
    else:
        visited.add(node[0])
        if node[0] in orbits:
            child_node = orbits[node[0]]
            if child_node not in visited:
                nodes.append((child_node, node[1] + 1))
        if node[0] in r_orbits:
            child_nodes = r_orbits[node[0]]
            for child_node in child_nodes:
                if child_node not in visited:
                    nodes.append((child_node, node[1] + 1))

print(f"PART 2: {min(list(distances))}")