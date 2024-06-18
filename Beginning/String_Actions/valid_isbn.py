"""
The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. 

"""

def valid_ISBN(isbn):
    number_isbn = isbn.replace("-", "")

#   if re.match(r"^\d{9}[\dX]$", number_isbn):

#     total = 0
#     for i in range(9):
#         total += int(number_isbn[i]) * (10 - i)

#     last_char = number_isbn[9]
#     if last_char == 'X':
#         total += 10
#     else:
#         total += int(last_char)

#     if total % 11 == 0:
#         return "TAK"
#     else:
#         return "Check your number"
#   else:
#     return "Check your number"

    if len(number_isbn) != 10:
        return "Check your number"

    if not (number_isbn[:9].isdigit() and (number_isbn[9].isdigit() or number_isbn[9] == 'X')):
        return "Check your number"

    total = 0
    for i in range(9):
        total += int(number_isbn[i]) * (10 - i)

    if number_isbn[9] == 'X':
        total += 10
    else:
        total += int(number_isbn[9])

    if total % 11 == 0:
        return "TAK"
    else:
        return "Check your number"
    

