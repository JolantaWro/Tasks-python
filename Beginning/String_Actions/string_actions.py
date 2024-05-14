def string_to_lower(x):
    if not isinstance(x, str):
        raise TypeError ("Your value must be string")
    return x.lower()

def string_to_upper(x):
    if not isinstance(x, str):
        raise TypeError ("Your value must be string")
    return x.upper()