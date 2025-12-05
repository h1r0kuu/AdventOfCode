ranges = []
ingredients = []
for line in open('inputs.txt', 'r'):
    line = line.strip()
    if line != '':
        if '-' in line:
            ranges.append(list(map(int, line.split('-'))))
        else:
            ingredients.append(int(line))

# part 1
# res = sum(
#     1 for ingredient in ingredients
#     if any(start <= ingredient <= end for start, end in ranges)
# )

# part 2
def merge_ranges(ranges):
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return merged

merged_ranges = merge_ranges(ranges)

res = sum(end - start + 1 for start, end in merged_ranges)

print(res)