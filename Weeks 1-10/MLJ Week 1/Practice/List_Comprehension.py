# List Comprehension!
# "Show you can build a new list in one concise expression using Python’s list-comprehension syntax—optionally transforming and/or filtering items from an existing iterable instead of using an explicit loop."
# https://www.youtube.com/watch?v=l8mWvDUwOt4
# Joshua Fashe
# 6/21/2025 4:20am
# Sum_A_List.py


mylist,sum = [4, 3, 3, -2], 0

for i in range(len(mylist)):
    sum = (sum + int(mylist[i]))

print(sum)