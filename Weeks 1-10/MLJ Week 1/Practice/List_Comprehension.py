# List Comprehension!
# "Show you can build a new list in one concise expression using Python’s list-comprehension syntax—optionally transforming and/or filtering items from an existing iterable instead of using an explicit loop."
# https://www.youtube.com/watch?v=l8mWvDUwOt4 (boo1)
# https://www.youtube.com/watch?v=YlY2g2xrl6Q
# Joshua Fashe
# 6/21/2025 4:20am
# List Comprehension.py

nums = [24, 13, 51, 64, 68, 111, 14, 560, 85 ]
evens = [num for num in nums if num %2 == 0]
# [expression for value in iterable if condition]
# 'num' for num: 'num' is blank expression
print(evens)

squares = [i*i for i in range(1,11)]
# [expression for value in (creates iterable)]
print(squares)


"""
nums,evens = [24, 13, 51, 64, 68, 111, 14, 560, 85 ], []

for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)
"""