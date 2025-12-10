# First Non-Repeating Character

s = "swiss"

from collections import Counter

freq = Counter(s)
for ch in s:
    if freq[ch] == 1:
        print(f"First non repeating charater is : {ch}")
        break