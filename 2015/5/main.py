disallowed_substring = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'

strs = []

for line in open('inputs.txt', 'r'):
    strs.append(line)

good_words = []
# for s in strs:
#     vowels_count = 0
#     contains_disallowd = False
#     contains_3_vowels = False
#     contains_duplicated = False
#     for i in range(len(s) - 1):
#         substring = s[i:i+2]
#         if len(set(substring)) == 1:
#             contains_duplicated = True
#         if substring in disallowed_substring:
#             contains_disallowd = True
#         if s[i] in vowels:
#             vowels_count += 1
#             if vowels_count == 3:
#                 contains_3_vowels = True

#     if not contains_disallowd and contains_3_vowels and contains_duplicated:
#         print(f"{s} - good has {vowels_count} {contains_duplicated} {contains_disallowd}")
#         good_words.append(s)

for s in strs:
    duplicated_pairs_count = 0
    contains_overlapped = False
    obj = dict()
    
    for i in range(len(s) - 1):
        substring = s[i:i+2]
        if i <= len(s) - 4:
            overlapped = s[i:i+3]
            if overlapped[0] == overlapped[2]:
                contains_overlapped = True

        if not substring in obj:
            obj[substring] = 1
        else:
            obj[substring] += 1
            if obj[substring] == 2:
                duplicated_pairs_count += 1

        if contains_overlapped and duplicated_pairs_count >= 1:
            good_words.append(s)

print(len(good_words))