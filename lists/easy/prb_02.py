# Find Max and Min from a List

nums = [10, 25, 3, 99, 56]

# Lengthy approach
max_num = nums[0]
min_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num

print(f"Maximum number is : {max_num}")
print(f"Minimum number is : {min_num}")

# Shorter approach
print(f"Maximum number is list is : {max(nums)}")
print(f"Minimum number is list is : {min(nums)}")
