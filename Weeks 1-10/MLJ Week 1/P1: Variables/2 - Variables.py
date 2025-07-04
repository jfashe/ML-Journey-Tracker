# Variables (ChatGPTutor)
"""
Variables store data. Variable/data types do not need to be declared.
    - They can be reassigned to a different type, but isnt recommended.
    - variables must start with a letter or underscore
    - no spaces or special characters (except _)
    - are case sensitive; (myVar ≠ MyVar)

"""
def newline():
    print("------------------")

newline()
x = 5 # integer
name = "joshua" # string
gpa = 2.77 # float
print(x)

newline()

x = "joshua" # reassigned
print (x)

newline()

x = 5
print(name, "has a", gpa, "GPA") #concantation by comma
print(name + "'s favorite number is 5") #concantation by commas. not recommended since you can only concatenate strings.

"""
CHATGPT PROMPT:
"I am relearning python, and i havent touched it in years. Ive basically forgot everything. Give me a full, detailed lesson that follows the task:
"Learn basic Python syntax: variables, data types (int, float, str, list, dict)."

I want cheats to make it easier (if they are difficult) and notes aswell. Do not leave out any important information. This will help me with my machine learning journey."

From there on out I seperated it to four parts (This is part 2).
"""