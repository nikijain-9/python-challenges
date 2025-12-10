# Check if a String is Palindrome

# A palindrome reads the same forward and backward.

# Examples: madam, level, radar

str = "madam"

# Lengthy approach
reversed_str = ""
for i in range(len(str) - 1, -1, -1):
    reversed_str += str[i]


if str == reversed_str:
    print(f"String `{str}` is a Palindrome")
else:
    print(f"String `{str}` is not a Palindrome")

# Shorter approach
print("Palindrome" if str == str[::-1] else "Not a Plaindrome")