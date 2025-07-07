# https://www.youtube.com/watch?v=XcfxkHrHTVE
# What are Python modules? - Bro Code
# 

# module -  a file containing code you want to include in your program
#           use 'import' to include a module (built in or your own)
#           useful to break up a large program reusable separate files

# help("modules") gives you a detailed list of python modules

#help("math")

import math # or "import math as m"
print(math.e)

from math import pi # personally not recommended 
                    # unless using ONLY one variable from a module
print(pi)

a, b, c, d = 1, 2, 3, 4
print(math.e)
print(math.e**a)
print(math.e**b)
print(math.e**c)
print(math.e**d)
