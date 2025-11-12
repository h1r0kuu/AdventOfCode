res = 0
while i := input():
    l, w, h = sorted(map(int, i.split('x')))
    res += 2 * (l + w) + l * w * h
print(res)