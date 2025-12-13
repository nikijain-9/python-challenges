# Find Top 2 Most Frequent Elements

nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]

from collections import Counter

freq = Counter(nums)

print([num for num, _ in freq.most_common(2)])





