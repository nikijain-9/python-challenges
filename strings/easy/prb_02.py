# Count Vowels in a String

s = "Education"
vowels = "aeiou"

count = 0

# Lengthy approach
for ch in s:
    if ch.lower() in vowels:
        count += 1

print(f"Count of vowels in string `{s}` is : {count}")

# Easy approach
vow_count = sum(1 for ch in s if ch.lower() in vowels)
print(f"Count of vowels in string `{s}` is : {vow_count}")


