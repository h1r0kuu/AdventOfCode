start_point = 50
password = 0
for line in open('inputs.txt', 'r'):
    direction, num = line[0], int(line.strip()[1:])

    if direction == 'R':
        start_point += num
    else:
        start_point -= num
    print(f"Rotation {direction} - {num}, new point {start_point}")
    old_point = start_point
    start_point //= 100
    print(f"After // {start_point}")

    password += abs(start_point)
    old_point %= 100
    print(f"After % {old_point}")
    start_point = old_point
    # if start_point == 0:
    #     password += 1
    
print(password)