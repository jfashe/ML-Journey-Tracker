# List Comprehension!
# "Show you can build a new list in one concise expression using Python’s list-comprehension syntax—optionally transforming and/or filtering items from an existing iterable instead of using an explicit loop."
# https://www.youtube.com/watch?v=l8mWvDUwOt4 (boo1)
# 
# Joshua Fashe
# 6/21/2025 4:20am
# List Comprehension.py

nums,evens = [24, 13, 51, 64, 68, 111, 14, 560, 85 ], []

for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)