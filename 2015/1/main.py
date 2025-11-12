s = input()
res = 0
for i in s:
    if i == '(':
        res += 1
    else:
        res -= 1
print(res)