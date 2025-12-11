# Count Occurrences of Each Element

nums = [1, 2, 2, 3, 3, 3, 4]

# Lengthy approach
num_occ = {}

for num in nums:
    if num in num_occ:
        num_occ[num] += 1
    else:
        num_occ[num] = 1

print(num_occ)

# Shorter approach

from collections import Counter

number_occurences = Counter(nums)
print(f"Each number occurences : {number_occurences}")
