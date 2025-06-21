# Sum-A-List!
# "Create a Python program that receives a collection of numeric values (e.g., a list) and produces their total sum as its output—nothing more, nothing less."
# 
# Joshua Fashe
# 6/21/2025 3:41am
# Sum_A_List.py


mylist,sum = [4, 3, 3, -2], 0

for i in range(len(mylist)):
    sum = (sum + int(mylist[i]))

print(sum)