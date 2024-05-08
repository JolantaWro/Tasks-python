def check_logical_values(x, operator, y):
    if operator == "==":
        return x == y
    elif operator == "!=":
        return x != y
    elif operator == "!=":
        return x != y
    elif operator == "<":
        return x < y
    else: 
        raise ValueError("Invalid operator")