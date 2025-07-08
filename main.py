from math_utils import add, subtract, multiply, divide, power, modulo
from string_utils import to_uppercase, reverse_string, is_palindrome, count_vowels
from logger import log_message

if __name__ == "__main__":
    a, b = 10, 5
    text = "Madam"

    # Math operations
    log_message(f"Add result: {add(a, b)}")
    log_message(f"Subtract result: {subtract(a, b)}")
    log_message(f"Multiply result: {multiply(a, b)}")
    log_message(f"Divide result: {divide(a, b)}")
    log_message(f"Power result: {power(a, b)}")
    log_message(f"Modulo result: {modulo(a, b)}")

    # String operations
    log_message(f"Original text: {text}")
    log_message(f"Uppercase: {to_uppercase(text)}")
    log_message(f"Reversed: {reverse_string(text)}")
    log_message(f"Is Palindrome: {is_palindrome(text)}")
    log_message(f"Vowel Count: {count_vowels(text)}")

    print("All operations complete. Results logged.")
