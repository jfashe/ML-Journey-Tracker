# control flow - if-else
# https://www.youtube.com/watch?v=FvMPfrgGeKs&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=6

age = int(input("Enter your age: "))
if age < 18:
    print ("MINOR ALERT!! MINOR ALERT!!")
elif age >= 18 and age < 21:
    print ("FAKE ADULT ALERT!! FAKE ADULT ALERT!!")
else:
    print ("OLD ASS UNC ALERT!! OLD ASS UNC ALERT!!")