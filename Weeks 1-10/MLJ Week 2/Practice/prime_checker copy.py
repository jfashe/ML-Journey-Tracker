# Prime Checker! 
# Checks to see if numbers are prime. plain n simlple.
# 
# Joshua Fashe
# 7/6/2025 11:20pm
# prime_checker.py

# If x % i = 0, the number is NOT prime!!!!
# If x % i != 0, the number ISS prime.

x,l,mylist = int(input("enter a number: ")),0,[]
while x <= 2 :
    x = int(input("try again. enter a number: "))
for i in range(2,x):
    mylist.append(x % i)
if 0 in mylist:
    print("composite")
else:
    print("prime")