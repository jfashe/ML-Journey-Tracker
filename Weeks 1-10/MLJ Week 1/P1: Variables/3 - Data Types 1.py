# Data Types (ChatGPTutor)
"""
int (Integer)
    age = 25
float (Decimal)
    pi = 3.14159
    - anything with a . is a float
str (String)
    greeting = "Hello"
    name = 'Joshua'
    - triple quotes '''text''' for multi-line strings.
"""
def newline():
    print("------------------")
print("Data Types"),(newline())

name = 'Joshua'
print(name)
# Common String Operations:
oper_len = len(name) # returns length of a string
oper_upper = name.upper() # uppercases string (JOSHUA)
oper_lower = name.lower() # lowercases string (joshua)
oper_index = name[0] # indexing starts at 0 (J)
oper_index2 = name[3:] # number before colon starts index at value (Hua)
oper_index3 = name[:4] # number after colon begins index at value (Josh)
oper_in = "Josh" in name # 'in' searches an index for a certain string. Returns 'True' or 'False'.
fstring = f"Hello, {name}" # used to format expressions in strings
print(fstring)

"""
CHATGPT PROMPT:
"I am relearning python, and i havent touched it in years. Ive basically forgot everything. Give me a full, detailed lesson that follows the task:
"Learn basic Python syntax: variables, data types (int, float, str, list, dict)."

I want cheats to make it easier (if they are difficult) and notes aswell. Do not leave out any important information. This will help me with my machine learning journey."

From there on out I seperated it to four parts (This is part 3.1).
"""