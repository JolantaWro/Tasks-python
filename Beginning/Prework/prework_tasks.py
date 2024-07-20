"""
    1. Get the information from the user and display it
    2. Display the list by adding spaces
    3. Incrementation and decrementation
"""

def display_sentence():
    user_name = input("What is you name? ")
    user_surname = input(f"{user_name}, what's your surname ")
    print(f"Witaj {user_name} {user_surname}")


def display_list():
    list_letters = ['a', 'b', 'c', 'd', 'e', 'f']
    print(" ".join(list_letters))


def counter_add_value(user_number):
    user_number += 1
    return user_number

def counter_subtract_value(user_number):
    user_number -= 1
    return user_number

def difference_age():
    age_father = int(input("Enter year of birth father: "))
    age_child = int(input("Enter year of birth child: "))
    result = f"Father is {age_child - age_father} years older than child"

    return result

def fizzbuzz():
    for element in range(1, 101):
        if (element % 3 == 0 and element % 5 == 0):
            print("FizzBuzz")
        elif(element % 3 == 0):
            print("Fizz")
        elif(element % 5 == 0):
            print("Buzz")
        else:
            print(element)
