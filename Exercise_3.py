# Author: Madhushree Somendyapnhalli Venkatesh Murthy
# PRID: SOMEN73309
# Registration number(s): 2214000
# University username: ms22749
# University email address: ms22749@essex.ac.uk
# Module: CE156 - An Approachable Introduction to Programming
# Module Supervisor: Dr Mike Sanderson

# Exercise 3

# Function to check if a given string is palindrome or not.
def isPalindrome(input_str):
    """This function determines if a given string is palindrome or not.

    argument(s):
        input_str (str): User's string input.

    returns:
        bool: True if the string s is a palindrome, False otherwise.
    """
    # Use the built-in "reversed" function to reverse the input string and rejoin the characters.
    reversed_str = "".join(reversed(input_str))

    # Check whether the reversed string matches the original input string and immediately return a boolean answer.
    return input_str == reversed_str


# Function to find the most frequent letter/digit
def getMostFrequentLetterOrDigit(input_str):
    """Returns the most frequent letter or digit in the input string (in uppercase).
       If both letters and digits are equally common, the one that occurs first is returned.
       Non-letter and non-digit characters are not taken into account.

    argument(s):
       input_str (str): User's input string

    returns:
       str: The most frequent letter or digit in the input string
    """
    # capitalise the input string
    converted_str = input_str.upper()

    counts_dict = {}

    # Loop over each character in the converted string
    for most_freq_value in converted_str:
        # exclude characters that are neither letters nor digits.
        if not most_freq_value.isalnum():
            continue
        # Add the character to the dictionary
        counts_dict[most_freq_value] = counts_dict.get(most_freq_value, 0) + 1

    # Find the max count among all characters
    max_count = max(counts_dict.values())

    # Any character that doesn't appear more than once is considered none.
    if max_count == 1:
        return None

    # The first character that appears most frequently is returned.
    for most_freq_value, count in counts_dict.items():
        if count == max_count:
            return most_freq_value


# Function that counts the number of letters,spaces and digits in the string
def getCountOfLetterSpacesDigits(input_str):
    """Count of letters, spaces, and digits in a given string input is calculated and returned in a dictionary.

    argument(s):
        input_str (str): String input to count the number of letters, spaces, and digits in.

    returns:
        dict: A dictionary containing the counts of letters, spaces, and digits.
    """

    # Initialize count variables
    letter_count = 0
    space_count = 0
    digit_count = 0

    for char in input_str:
        # if character is a letter and increment letter count
        if char.isalpha():
            letter_count += 1
        # if character is a space and increment space count
        elif char.isspace():
            space_count += 1
        # if character is a digit and increment digit count
        elif char.isdigit():
            digit_count += 1

    # Create a dictionary with the counts and return it
    return {
        "Number of letters": letter_count,
        "Number of spaces": space_count,
        "Number of digits": digit_count,
    }
