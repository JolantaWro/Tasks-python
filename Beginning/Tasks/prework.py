"""
    1. Get the information from the user and display it
    2. Display the list by adding spaces
"""

def display_sentence():
    user_name = input("What is you name? ")
    user_surname = input(f"{user_name}, what's your surname ")
    print(f"Witaj {user_name} {user_surname}")


def display_list():
    list_letters = ['a', 'b', 'c', 'd', 'e', 'f']
    print(" ".join(list_letters))

display_list()