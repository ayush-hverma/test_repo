def to_uppercase(text):
    """Convert string to uppercase."""
    return text.upper()

def to_lowercase(text):
    """Convert string to lowercase."""
    return text.lower()

def reverse_string(text):
    """Reverse the given string."""
    return text[::-1]

def is_palindrome(text):
    """Check if a string is a palindrome (case-insensitive)."""
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]

def count_vowels(text):
    """Count the number of vowels in the given text."""
    return sum(1 for char in text.lower() if char in "aeiou")
