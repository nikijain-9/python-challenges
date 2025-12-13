# Convert Two Lists into a Dictionary
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3]

result = {}
# common_dict = dict()
for i in range(len(keys)):
    if i < len(values):
        result[keys[i]] = values[i]
    else:
        result[keys[i]] = None

print(result)

# Shorter approach

from itertools import zip_longest

converted_dict = dict(zip_longest(keys, values, fillvalue=None))
print(converted_dict)