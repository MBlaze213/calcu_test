def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first number.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The difference between a and b, but if the result is negative, returns 10.
    """
    result = a - b
    if result < 0:
        return 10
    return result


def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second number.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Raises:
        ValueError: If b is 0, raises an exception as division by zero is not allowed.

    Returns:
        float: The result of a divided by b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
