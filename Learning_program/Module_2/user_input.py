#!/usr/bin/env python3

print('Welcome to the age calculator.')
answer = input('Would you like to know how old you will be in a particular year? (y/n)')

while not (answer == 'y' or answer == 'n'):
    print("The value of answer is", answer)
    print("I'm sorry, I didn't understand. Please try again.")
    answer = input('Would you like to know how old you will be in a particular year? (y/n)')

if answer == 'n':
    print("I'm sorry you're not interested. Goodbye!")
else:
    year = input('What year were you born? ')
    month = input('In what month were you born? ')
    day = input('On what day? ')
    
    futureYear = input('What year did you want to know about? ')
    futureMonth = input('What month did you want to know about? ')
    futureDay = input('What day? ')

    jan = ['jan', 'january', 'Jan', 'January']
    feb = ['feb', 'february', 'Feb', 'February']
    mar = ['mar', 'march', 'Mar', 'March']
    apr = ['apr', 'april', 'Apr', 'April']
    may = ['may', 'May']
    jun = ['jun', 'june', 'Jun', 'June']
    jul = ['jul', 'july', 'Jul', 'July']
    aug = ['aug', 'august', 'Aug', 'August']
    sep = ['sep', 'september', 'Sep', 'September']
    oct = ['oct', 'october', 'Oct', 'October']
    nov = ['nov', 'november', 'Nov', 'November']
    dec = ['dec', 'december', 'Dec', 'December']

    for i in jan:
        if month == i:
            month = 1
        if futureMonth == i:
            futureMonth = 1

    for i in feb:
        if month == i:
            month = 2
        if futureMonth == i:
            futureMonth = 2

    for i in mar:
        if month == i:
            month = 3
        if futureMonth == i:
            futureMonth = 3

    for i in apr:
        if month == i:
            month = 4
        if futureMonth == i:
            futureMonth = 4

    for i in may:
        if month == i:
            month = 5
        if futureMonth == i:
            futureMonth = 5

    for i in jun:
        if month == i:
            month = 6
        if futureMonth == i:
            futureMonth = 6

    for i in jul:
        if month == i:
            month = 7
        if futureMonth == i:
            futureMonth = 7

    for i in aug:
        if month == i:
            month = 8
        if futureMonth == i:
            futureMonth = 8

    for i in sep:
        if month == i:
            month = 9
        if futureMonth == i:
            futureMonth = 9

    for i in oct:
        if month == i:
            month = 10
        if futureMonth == i:
            futureMonth = 10

    for i in nov:
        if month == i:
            month = 11
        if futureMonth == i:
            futureMonth = 11

    for i in dec:
        if month == i:
            month = 12
        if futureMonth == i:
            futureMonth = 12


    month = int(month)
    futureMonth = int(futureMonth)
    
    age = int(futureYear) - int(year)
    day = int(day)
    futureDay = int(futureDay)
    if futureMonth <= month:
        age = age - 1
        if futureMonth == month:
            if futureDay >= day:
                age = age + 1

    print('On '+str(futureMonth)+'/'+str(futureDay)+'/'+str(futureYear)+' you will be '+str(age)+' years old.')
    print('Goodbye!') 