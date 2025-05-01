from math_utils import add, subtract
from string_utils import to_uppercase, reverse_string
from logger import log_message

if __name__ == "__main__":
    result1 = add(10, 5)
    result2 = reverse_string("hello")

    log_message(f"Add result: {result1}")
    log_message(f"Reversed string: {result2}")

    print("Done. Results logged.")
