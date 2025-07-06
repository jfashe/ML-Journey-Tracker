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
    print(response)

    if response.status_code == 200:
        print("Data Retrieved!")
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = input("Which pokemon would you like to know about? ")

get_pokemon_info(pokemon_name)