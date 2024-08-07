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

