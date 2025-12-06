from collections import defaultdict

hashmap = defaultdict(list)

for line in open('inputs.txt', 'r'):
    nums = line.strip().split()
    for idx, val in enumerate(nums):
        hashmap[idx].append(val)

res = 0
for equation in hashmap.values():
    operator = equation[-1]
    numbers = [int(num) for num in equation[:-1]]    
    if operator == '+':
        local_res = sum(numbers)
    else:
        local_res = 1
        for num in numbers:
            local_res *= num
    
    res += local_res
print(res)