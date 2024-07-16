"""
A simple number guessing game
"""

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)