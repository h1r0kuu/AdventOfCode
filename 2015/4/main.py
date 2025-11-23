from hashlib import md5

s = input()
i = 0
res = None
while True:
    new_s = s + str(i)
    hashed = md5(new_s.encode())
    print(i)
    if '000000' == hashed.hexdigest()[0:6]:
        res = i
        break
    i += 1
print(f"res {res}")