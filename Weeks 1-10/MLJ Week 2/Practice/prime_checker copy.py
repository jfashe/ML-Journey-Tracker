# Prime Checker! 
# Checks to see if numbers are prime. plain n simlple.
# 
# Joshua Fashe
# 7/6/2025 11:20pm
# prime_checker.py

# If x % i = 0, the number is NOT prime!!!!
# If x % i != 0, the number ISS prime.

#variable = value_if_true if condition else value_if_false


x,l,mylist = 100,0,[]
#x,l,mylist = int(input("enter a number: ")),0,[]
while x <= 1 :
    x = int(input("try again. enter a number: "))
for i in range(2,x):
    if (x % i != 0):
        print("prime")
        break
    elif ((x % i == 0) & (i == x)):
        print("composite")
        break
    



"""
if (x % i == 0) & (x != i):
        print("prime")
"""