# Move All Zeros to the End
from collections import Counter

nums = [0, 1, 0, 3, 12]
zero_count = 0
result = []

for num in nums:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1

for _ in range(zero_count):
    result.append(0)

print(result)

# Alternate approach

count_0 = 0

for num in nums:
    if num == 0:
        zero_index = nums.index(num)
        del nums[zero_index]
        count_0 += 1

for _ in range(count_0):
    nums.append(0)
print(nums)

# Shorter approach
numbers = [0, 1, 0, 3, 12]
pos = 0

for num in numbers:
    if num != 0:
        numbers[pos] = num
        pos += 1

while pos < len(numbers):
    numbers[pos] = 0
    pos += 1

print(numbers)