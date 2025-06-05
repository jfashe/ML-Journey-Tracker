# Data Types (ChatGPTutor)
"""
list (Ordered Collection)
    grades = [95, 88, 76, 100]
    - Can hold mixed types
    random = [1, "apple", 3.14
dict (Dictionary/Key-Value Pair)
    person = {
    "name": "Josh",
    "age": 19,
    "is_student": True,
    }
    - Seperated by commas
    - accessed by key (key:value)
"""
def newline():
    print("------------------")

print("List and Dicts"),newline()
grades = [95, 83, 75, 100]
print(grades)

# Common List Methods
print(".append():")
grades.append(85) # adds 85 to end of list
print(grades)

print(".pop():")
grades.pop() # removes last lisst item
print(grades)

print("index accessing [x]:")
print(grades[1]) # accesses second list item

print ("Index slicing [:x]")
print(grades[:2]) # slices and returns first two list items

# Common Dict Methods
person = {
    "name": "Josh",
    "age": 19,
    "is_student": True,
    }
newline()

print("index access ['key']:")
print(person['name']) # acccesses a value by its key ('Joshua')

print("accessing using .get():")
print(person.get('age')) # 'gets' a value from its key (19)

"""
CHATGPT PROMPT:
"I am relearning python, and i havent touched it in years. Ive basically forgot everything. Give me a full, detailed lesson that follows the task:
"Learn basic Python syntax: variables, data types (int, float, str, list, dict)."

I want cheats to make it easier (if they are difficult) and notes aswell. Do not leave out any important information. This will help me with my machine learning journey."

From there on out I seperated it to four parts (This is part 3.2).
"""