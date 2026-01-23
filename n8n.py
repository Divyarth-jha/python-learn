```python
nums = [1, 2, 2, 3, 1, 4, 3]

unique_nums = []
seen = set()

for x in nums:
    if x not in seen:
        unique_nums.append(x)
        seen.add(x)

print("Original:", nums)
print("Without duplicates:", unique_nums)
```

