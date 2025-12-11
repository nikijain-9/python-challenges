# Remove Duplicates from a List

nums = [1, 2, 2, 3, 4, 3, 5]

# Lengthy approach

unique_list = []

for num in nums:
    if num not in unique_list:
        unique_list.append(num)

print(f"Non repeating numbers list : {unique_list}")

# Shorter approach

new_unique_list = list(set(nums))
print(f"New non repeating numbers list : {new_unique_list}")