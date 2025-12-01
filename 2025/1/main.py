start_point = 50
password = 0
# PART 1
# for line in open('inputs.txt', 'r'):
#     direction, num = line[0], int(line.strip()[1:])

#     if direction == 'R':
#         start_point += num
#     else:
#         start_point -= num

#     start_point %= 100

#     if start_point == 0:
#         password += 1
# print(password)

# PART 2
start_point = 50
password = 0
for line in open('inputs.txt', 'r'):
    direction, num = line[0], int(line.strip()[1:])
    print(f"Before rotation point is {start_point}")

    for _ in range(num):
        if direction == 'R':
            start_point = (start_point - 1 + 100) % 100
        else:
            start_point = (start_point + 1) % 100
        if start_point == 0:
            password += 1
print(password)