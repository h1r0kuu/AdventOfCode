import sys
from collections import defaultdict

data: list[list[int, int, int]] = []
for line in open('inputs.txt', 'r'):
    data.append(list(map(int, line.strip().split(','))))

res = defaultdict()
def find_nearest(x,y,z,data):
    lowest_distance = sys.maxsize
    nearest_pos = []
    for x2, y2, z2 in data:
        distance = pow(x2 - x, 2) + pow(y2 - y, 2) + pow(z2 - z, 2)
        if distance < lowest_distance:
            nearest_pos = [x2, y2, z2]
    return nearest_pos
for x, y, z in data:
    res[str([x,y,z])] = [x, y, z]
    nearest_pos = find_nearest(x, y, z, data)
    for n_x, n_y, n_z in res.values():
        if n_x == nearest_pos[0] and n_y == nearest_pos[1] and n_z == nearest_pos[2]:
            res.get(str([n_x, n_y, n_z])).append(nearest_pos)
    # res.append([[x, y, z], nearest_pos])

print(res)