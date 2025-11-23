res = 0

for line in open('inputs.txt', 'r'):
    # 1
    # res += len(line[:-1]) - len(eval(line))
    # 2
    res += line.count('"') + line.count('\\') + 2
print(res + 1)