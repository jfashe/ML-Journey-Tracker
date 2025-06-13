# for loops (bro code)
# https://www.youtube.com/watch?v=KWgYha0clzw
#
# For loops execute a block of code over a fixed numebr of times.
# can iterate over a range, string, sequence, etc.
example = int(input("Which example would you like to view? (enter 1-6)"))
match example:
    case 1:     # Iterating forward:
        for x in range(1, 11): # second value is non-inclusive
            print(x)

    case 2:     # Iterating backward:
        for x in reversed(range(1, 11)):
            print(x)
        print("Happy new year!")
    
    case 3:     # Step
        for x in range (2, 11, 2): # third value, iterates in steps of 2
            print(x)
    
    case 4:     # Iterating over strings:
        debit_card = "1234-5678-9010-9999"
        for x in debit_card:
            print(x)
    
    case 5:     # break
        for x in range(1, 21):
            if x == 13:
                continue # Skips the number 13 in the sequence
            else:
                print(x)
    
    case 6:     # break
        for x in range(1, 21):
            if x == 13:
                break # ends the program when it reaches 13
            else:
                print(x)