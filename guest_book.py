"""
10-5 Guest Book:
write a while loop that prompts users for their name.
collects all the names that are entered, and then writes
these names to a file called guest_book.txt. 
Each name should be on a new line.

Q: Why do we have to batch up all of the names and then write to the file?
    If we didnt batch up the file and kept the existing of the structure of the code we would be overwriting the file each time a new name is entered.
    This would result in only the last name being saved in the file. 
    By batching up all of the names and then writing to the file we can ensure that all of the names are saved without overwriting anything


Q:Could we write to the file one name at a time using path.write_text?
    Using path.write_text would overwrite the file each time so we would lose all previously entered names. 
    To write one name at a time without losing data we would need to open the file in append mode and 
    write each name to it as it is entered.


Q:Why would we want to write one name at a time instead of batching them up? 
    There could be a scenario where a program like this crashes before it can collect all of the names
    If we wrote one name at a time we would be able to preserve the names before the crash.

"""
from os import path
from pathlib import Path

path = Path('guest_book.txt')
guest_list = []
while True:
    name = input("Please enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    guest_list.append(name)

path.write_text('\n'.join(guest_list))