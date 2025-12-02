result = 0

# part1
def is_invalid_id(id_str: str) -> bool:
    n = len(id_str)
    
    if n % 2 != 0:
        return False
    
    half = n // 2
    first_half = id_str[:half]
    second_half = id_str[half:]
    
    return first_half == second_half

# part2
def is_invalid_id2(id_str: str) -> bool:
    n = len(id_str)
    
    for pattern_length in range(1, n // 2 + 1):
        pattern = id_str[:pattern_length]
        
        repeated = ""
        while len(repeated) < n:
            repeated += pattern
        
        if repeated == id_str:
            return True
    
    return False

for line in open('inputs.txt', 'r'):
    ids = line.split(',')
    for id in ids: 
        id_from, id_to = id.split('-')
        for num in range(int(id_from), int(id_to) + 1):
           if is_invalid_id2(str(num)):
                result += num
print(result)