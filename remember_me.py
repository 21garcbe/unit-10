"""10-14
The final listing for remember_me.py assumes either that the user has already
entered their username or that program is running for the first time.
MOOdify it in case the current user is not the person that last used the program
before printing a welcome message in the greet_user in the greet_user function,
ask the user if it is the correct username. if its not call get_username() to get the correct username
"""

from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name, and remember their name in a file."""
    path = Path('username.json')
    username = get_stored_username(path)

    if username is None:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
    else:
        valid_answer = False
        while not valid_answer:
            answer = input(f"Is your name {username}? (y/n) ").strip().lower()
            if answer == 'y':
                print(f"Welcome back, {username}!")
                valid_answer = True
            elif answer == 'n':
                username = get_new_username(path)
                print(f"We'll remember you when you come back, {username}!")
                valid_answer = True
            else:
                print("Please enter 'y' or 'n'.")



greet_user()
