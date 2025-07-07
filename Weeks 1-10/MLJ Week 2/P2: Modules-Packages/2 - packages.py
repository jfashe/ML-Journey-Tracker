#https://www.youtube.com/watch?v=9z7gGUbAj5U
#https://www.youtube.com/watch?v=JVQNywo4AbU
# Python pip? - Bro Code
# Request API data using Python - Bro Code
# 

# pip -   Pyhon's package manager for packages and modules
#           use 'import' to include a module (built in or your own)
#           useful to break up a large program reusable separate files

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Data Retrieved!")
        data = response.json()
        return(data)    # data is now a dictionary (key:value) of pokemon info. 
                        # and can be accessed by key.
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = input("Which pokemon would you like to know about? ")
pokemon_info = get_pokemon_info(pokemon_name)

# If the info exists basically.
if pokemon_info:
    print(pokemon_info["name"].capitalize())
    print(pokemon_info["height"])
    print(pokemon_info["weight"])

# to print just keys if you dont feel like reading the whole json
for key in pokemon_info:
    print(key)