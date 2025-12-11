# Rotate List by K Steps

nums = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = nums[-1]
    nums.insert(0, last)
    nums.pop()

print(f"Rotated list by {k} steps: {nums}")
