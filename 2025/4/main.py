table = []
dirs = (
    (1, 1),
    (1, 0),
    (0, 1),
    (1, -1),
    (0, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1)
)
for line in open('inputs.txt', 'r'):
    table.append(list(line))

def count_neighbours(i,j,table):
    neighbours = 0
    for dx, dy in dirs:
        k = i + dx
        l = j + dy
        if (k >= 0 and k <= len(table) - 1 and l >= 0 and l <= len(table[0]) - 1) and (table[k][l] == '@'):
            neighbours += 1
    return neighbours

dont_have_accessible = False

res = 0
while True:
    
    to_remove = []
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == '@' and count_neighbours(i, j, table) < 4:
                to_remove.append((i, j))

    if not to_remove:
        break
 
    for i, j in to_remove:
        table[i][j] = '.'
    
    res += len(to_remove)
print(res)