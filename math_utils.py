def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the result of subtracting b from a."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the result of dividing a by b. Raise error on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def modulo(a, b):
    """Return the remainder when a is divided by b."""
    return a % b
