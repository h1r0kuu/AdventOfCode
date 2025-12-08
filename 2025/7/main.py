data: list[str] = []
for line in open('inputs.txt', 'r'):
    data.append(line)

beams = [0] * len(data[0])
beams[data[0].index('S')] = 1

splits = 0
for line in data[1:]:
    for i, char in enumerate(line):
        if char == '^' and beams[i] > 0:
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            splits += 1
            beams[i] = 0
print(splits)
print(sum(beams))