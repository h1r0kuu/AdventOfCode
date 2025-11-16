s = input()
res = 0
counter = 0
for i in s:
    counter += 1
    if i == '(':
        res += 1
    else:
        res -= 1
    if res == -1:
        break

print(counter)