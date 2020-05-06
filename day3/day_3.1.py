# TODO: Given paths of two wires in right/left/up/down notation, find the intersection point nearest to the origin by "Taxicab Distance"

# TODO: Parse out each path so program can read it
with open(r'input.txt', 'r') as file:
    paths = file.readlines()
    path1 = paths[0].split(',')
    path2 = paths[1].split(',')

# TODO: Trace path of wire 1
# TODO: Record every point wire 1 touches
locs1 = [(0, 0)]
locs2 = [(0, 0)]
for run in path1:
    dir = run[:1]
    dist = int(run[1:])
    for step in range(dist):
        if dir == 'R':
            locs1.append((locs1[-1][0] + 1, locs1[-1][1]))
            step += 1
        elif dir == 'L':
            locs1.append((locs1[-1][0] - 1, locs1[-1][1]))
            step += 1
        elif dir == 'U':
            locs1.append((locs1[-1][0], locs1[-1][1] + 1))
            step += 1
        elif dir == 'D':
            locs1.append((locs1[-1][0], locs1[-1][1] - 1))
            step += 1

for run in path2:
    dir = run[:1]
    dist = int(run[1:])
    for step in range(dist):
        if dir == 'R':
            locs2.append((locs1[-1][0] + 1, locs1[-1][1]))
            step += 1
        elif dir == 'L':
            locs2.append((locs1[-1][0] - 1, locs1[-1][1]))
            step += 1
        elif dir == 'U':
            locs2.append((locs1[-1][0], locs1[-1][1] + 1))
            step += 1
        elif dir == 'D':
            locs2.append((locs1[-1][0], locs1[-1][1] - 1))
            step += 1

print(locs1)
print(locs2)

locs1 = set(locs1)
locs2 = set(locs2)
print(locs1)
intersections = locs1.intersection(locs2)
print(intersections)
print(len(intersections))

# TODO: Trace path of wire 2
# TODO: Record every point wire 2 touches

# TODO: Compare list of wire 1 points to wire 2 points
# TODO: For each intersection, find Manhattan distance from origin
# TODO: Return minimum distance
