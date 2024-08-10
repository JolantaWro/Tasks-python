"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    list_numbers = []
    for element in range(3):
        list_numbers.append(number + element)
    return list_numbers



def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    list_rounds = rounds_1 + rounds_2
    return list_rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    sum_card = sum(hand)
    len_card = len(hand)
    return sum_card / len_card


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    actual_average = sum(hand) / len(hand)
    
    first_last_average = (hand[0] + hand[-1]) / 2
    
    median_card = hand[len(hand) // 2]
    
    if first_last_average == actual_average or median_card == actual_average:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    if not hand:
        return True 
    
    even_values = [hand[i] for i in range(0, len(hand), 2)]
    odd_values = [hand[i] for i in range(1, len(hand), 2)]
    
    average_even = sum(even_values) / len(even_values) if even_values else 0
    average_odd = sum(odd_values) / len(odd_values) if odd_values else 0
    
    return average_even == average_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if len(hand) == 0:
        return hand
    
    if hand[-1] == 11:
        
        hand[-1] = 22
        
    return hand

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}

    value_one = card_values.get(card_one, int(card_one) if card_one.isdigit() else 0)

    value_two = card_values.get(card_two, int(card_two) if card_two.isdigit() else 0)
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one in ['J', 'Q', 'K']:
        value_one = 10
    elif card_one == 'A':
        value_one = 11
    else:
        value_one = int(card_one)
    
    if card_two in ['J', 'Q', 'K']:
        value_two = 10
    elif card_two == 'A':
        value_two = 11
    else:
        value_two = int(card_two)

    total_value = value_one + value_two

    
    if total_value + 11 <= 21:
        return 11
    else:
        return 1
    
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if (card_one == 'A' and card_two in ['10', 'K', 'Q', 'J']) or \
       (card_two == 'A' and card_one in ['10', 'K', 'Q', 'J']):
        return True
    else:
        return False