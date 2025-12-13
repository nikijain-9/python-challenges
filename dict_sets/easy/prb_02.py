# Check if Two Lists Have Common Elements
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 9]

is_common = False

# Lengthy approach
for i in list1:
    for j in list2:
        if i == j:
            is_common = True
            break
        
print(f"Is elements common in lis1 and list2 : {is_common}")

# Shorter approach

check_common_el = (True if set(list1) & set(list2) else False)
print(check_common_el)

# OR
print(bool(set(list1) & set(list2)))