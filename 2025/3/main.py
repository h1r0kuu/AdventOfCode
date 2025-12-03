def find_max_joltage(line, num_batteries):
    n = len(line)    
    result = []
    start_pos = 0
    
    for _ in range(num_batteries):
        remaining_to_select = num_batteries - len(result)
        end_pos = n - remaining_to_select + 1
        
        max_digit = -1
        max_pos = -1
        for i in range(start_pos, end_pos):
            if int(line[i]) > max_digit:
                max_digit = int(line[i])
                max_pos = i
        
        result.append(line[max_pos])
        start_pos = max_pos + 1
    
    return int(''.join(result))

res = 0
for line in open('inputs.txt', 'r'):
    line = line.strip()
    # part one
    # joltage = find_max_joltage(line, 2)
    
    # part two
    joltage = find_max_joltage(line, 12)
    res += joltage

print(res)