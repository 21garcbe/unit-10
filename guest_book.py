"""
write a while loop that prompts users for their name.
collects all the names that are entered, and then writes
these names to a file called guest_book.txt. 
Each name should be on a new line.

Q:why do we have to batch up all of the names and then write to the file?

Q:COuld we write to the file one name at a time using path.write_text?

Q:Why would we want to write one name at a time instead of batching them up?

"""
from os import path
from pathlib import Path

path = Path('guest_book.txt')
guest_list = []
while response != 'q':
    print("Please add your name to the guest book")
    response = input("Enter your name (or 'q' to quit): ")
    if response != 'q':
        guest_list.append(response)

path.write_text('\n'.join(guest_list))