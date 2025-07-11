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
def count_consonants(text):
    """Count the number of consonants in a string."""
    return sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')

def remove_punctuation(text):
    """Remove punctuation from the text."""
    import string
    return ''.join(c for c in text if c not in string.punctuation)

def word_frequency(text):
    """Return a dictionary of word frequencies."""
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))
