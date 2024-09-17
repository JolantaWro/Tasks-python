COLOR_CODES = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def color_code(color):
    """
    Zwraca wartość liczbową odpowiadającą danemu kolorowi.
    
    Argument:
    color (str): Nazwa koloru.

    Zwraca:
    int: Wartość liczbowa dla danego koloru.
    """
    return COLOR_CODES.index(color)

def colors():
    """
    Zwraca listę wszystkich dostępnych kolorów.

    Zwraca:
    list: Lista kolorów w odpowiedniej kolejności.
    """
    return COLOR_CODES

print(color_code('red'))