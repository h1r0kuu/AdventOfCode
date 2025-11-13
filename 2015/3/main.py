s = input()
delivered_presents = 1
santa_pos = (0, 0)
robo_pos = (0, 0)
all_position = [santa_pos]

def pos(ch: str, santa_pos):
    if ch == '>':
        santa_pos = (santa_pos[0] + 1, santa_pos[1])
    elif ch == '<':
        santa_pos = (santa_pos[0] - 1, santa_pos[1])
    elif ch == '^':
        santa_pos = (santa_pos[0], santa_pos[1] + 1)
    elif ch == 'v':
        santa_pos = (santa_pos[0], santa_pos[1] - 1)
    return santa_pos
counter = 1
for ch in s:
    if counter % 2 == 0:
        robo_pos = pos(ch, robo_pos)
    else:
        santa_pos = pos(ch, santa_pos)
    counter += 1
    print(santa_pos)
    if santa_pos not in all_position:
        all_position.append(santa_pos)
    if robo_pos not in all_position:
        all_position.append(robo_pos)

print(all_position)
print(len(all_position))