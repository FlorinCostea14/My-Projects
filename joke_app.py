import sys
import requests
import random

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")
    jokes = response.json()

    if response.status_code == 200:
        joke = random.choice(jokes)
        return f"{joke['setup']}\n{joke['punchline']}"
    else:
        return "Failed to fetch jokes!"

if len(sys.argv) == 2 and sys.argv[1] == 'joke':
    print(get_joke())
else:
    print("Invalid command!")
