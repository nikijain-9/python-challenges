# Longest Common Prefix Among Strings

# We reduce the prefix step by step until it matches all strings.
strs = ["flower", "flow", "flight"]

prefix = strs[0]
for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(f"Longest common prefix is : {prefix}")