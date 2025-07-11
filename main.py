from math_utils import *
from string_utils import *
from logger import Logger
from date_utils import current_datetime, days_between
from file_utils import write_file, read_file
from data_utils import flatten_list

if __name__ == "__main__":
    logger = Logger()

    # Math ops
    logger.info(f"Add: {add(10, 5)}")
    logger.info(f"Is 7 prime? {is_prime(7)}")
    logger.info(f"Factorial of 5: {factorial(5)}")

    # String ops
    text = "Madam, in Eden I'm Adam."
    logger.info(f"Original: {text}")
    logger.info(f"No punctuation: {remove_punctuation(text)}")
    logger.info(f"Is Palindrome: {is_palindrome(text)}")
    logger.info(f"Consonant Count: {count_consonants(text)}")

    # Date ops
    logger.info(f"Now: {current_datetime()}")
    logger.info(f"Days between 2025-01-01 and 2025-07-11: {days_between('2025-01-01', '2025-07-11')}")

    # File ops
    write_file("sample.txt", "This is a test.")
    content = read_file("sample.txt")
    logger.info(f"Read from file: {content}")

    # Data ops
    logger.info(f"Flattened list: {flatten_list([[1,2], [3,4]])}")

    print("All extended operations complete.")
