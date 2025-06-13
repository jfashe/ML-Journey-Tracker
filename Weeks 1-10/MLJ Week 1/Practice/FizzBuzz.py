# FizzBuzz! Rules located in: /Media/Fizzbuzz.png
# "Tech interviewers repurposed the same rules as a rapid test of basic control flow, arithmetic reasoning, and attention to detail. You’re usually asked to “print” or “return” the sequence for a given range (often 1–100) following those exact substitution rules—no more, no less."
#
# FizzBuzz.py
#
while True:
    x = int(input("Enter a number from 1-1000! "))
    if not 1 <= x <= 1000:
        pass
    else:
        for i in range(1, x+1):
            if i%15 == 0:
                print("FizzBuzz")
            elif i%3 == 0:
                print("Fizz")
            elif i%5 == 0:
                print("Buzz")
            else:
                print(i)
        break