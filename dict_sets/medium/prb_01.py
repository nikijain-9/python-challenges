# Group People by First Letter of Their Name

names = ["Alice", "Bob", "Ankit", "Brian", "Cindy"]

groups = {}

for name in names:
    first_char = name[0]

    if first_char not in groups:
        groups[first_char] = [name]
    else:
        groups[first_char].append(name)

print(groups)


# Shorter approach

from collections import defaultdict

result = defaultdict(list)

for name in names:
    result[name[0]].append(name)

print(dict(result))