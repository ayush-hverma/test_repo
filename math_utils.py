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
def average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def factorial(n):
    """Return the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
