def add_numbers(x, y):
    """
    Calculate the sum of two numbers.

    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.

    Raises:
    TypeError: If either x or y is not an int or float.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be int or float.")
    return x + y

def subtract_numbers(x, y):
    """
    Calculate the difference between two numbers.

    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.

    Returns:
    int or float: The difference between the two numbers.

    Raises:
    TypeError: If either x or y is not an int or float.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be int or float.")
    return x - y

def multiply_numbers(x, y):
    """
    Calculate the product of two numbers.

    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.

    Returns:
    int or float: The product of the two numbers.

    Raises:
    TypeError: If either x or y is not an int or float.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be int or float.")
    return x * y

def divide_numbers(x, y):
    """
    Calculate the quotient of two numbers.

    Parameters:
    x (int or float): The numerator.
    y (int or float): The denominator.

    Returns:
    int or float: The quotient of the two numbers.

    Raises:
    TypeError: If either x or y is not an int or float.
    ValueError: If either x or y is zero, as division by zero is undefined.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both x and y must be int or float.")
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def mean_numbers(numbers):
    """
    Calculate the mean of a list of numbers.

    Parameters:
    numbers (list): A list of numbers (int or float).

    Returns:
    float: The mean of the numbers, or raises ValueError if the list is empty.

    Raises:
    ValueError: If the list of numbers is empty.
    TypeError: If any element in the list is not an int or float.
    """
    if len(numbers) == 0:
        raise ValueError("The list of numbers is empty. Mean is not defined.")
    if any(not isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be int or float.")
    return sum(numbers) / len(numbers)

def median_numbers(numbers):
    """
    Calculate the median of a list of numbers.

    Parameters:
    numbers (list): A list of numbers (int or float).

    Returns:
    float: The median of the numbers.

    Raises:
    ValueError: If the list of numbers is empty.
    TypeError: If any element in the list is not an int or float.
    """
    if len(numbers) == 0:
        raise ValueError("The list of numbers is empty. Median is not defined.")
    if any(not isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be int or float.")
    
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    
    if n % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2.0