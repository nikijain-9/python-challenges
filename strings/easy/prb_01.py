# Reverse a string 

str = "Python"

# Lengthy approach

reversed_str = ""

for i in range(len(str) - 1, -1, -1):
    reversed_str += str[i]

print(f"Reversed string: {reversed_str}")

# Easy approach
s = "String"
print(f"Reversed string is : {s[::-1]}")