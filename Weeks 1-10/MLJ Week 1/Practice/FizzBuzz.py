# FizzBuzz! Rules located in: /Media/Fizzbuzz.png
# "Tech interviewers repurposed the same rules as a rapid test of basic control flow, arithmetic reasoning, and attention to detail. You’re usually asked to “print” or “return” the sequence for a given range (often 1–100) following those exact substitution rules—no more, no less."
#
# FizzBuzz.py
#
while True:
    range = int(input("Enter a number from 15-1000! "))
    
    for i in (15, range+1):
        print(i)