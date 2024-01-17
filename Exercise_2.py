# Author: Madhushree 

# Exercise 2

# Function to get list of all non-prime numbers between two positive integers.
def getNonPrimeNumbersBetweenIntegers():
    """This program outputs an inclusive list of all non-prime numbers between two positive integers.

    argument(s):
        None

    returns:
        Outputs/Prints a list of all non-prime numbers with 10 numbers per line
    """
    while True:
        try:
            # Requesting two positive numbers from the user
            number1 = int(
                input("Please enter the first positive integer: ")
            )  # requesting the entry of the first positive integer
            number2 = int(
                input("Please enter the second positive integer: ")
            )  # requesting the entry of the second positive integer
        except ValueError:
            print("You have entered a non-numeric value.")
            continue

        # Verify the input is correct.
        if number1 <= 0 or number2 <= 0:  # if either number is not positive
            print("You have entered a non-positive value")  # print error message
        else:
            # Swap the numbers if the user enters the numbers in the "either" order
            if (
                number1 > number2
            ):  # if the first number is greater than the second number
                swappedNumber1 = number2  # set swappedNumber1 for number2's value.
                swappedNumber2 = number1  # set swappedNumber1 for number1's value.
            else:
                swappedNumber1 = number1  # set swappedNumber1 for number1's value.
                swappedNumber2 = number2  # set swappedNumber1 for number2's value.

            # Call the get_non_prime_numbers function and store the result in a list
            list_of_non_prime_numbers = getListOfNonPrimeNumbers(
                swappedNumber1, swappedNumber2
            )

            # Display the list of non-prime numbers with 10 numbers per line
            count = 0
            print(
                f"The list of non-prime between {swappedNumber1} and {swappedNumber2} are as below:"
            )
            print()  # print a new line
            for num in range(
                swappedNumber1, swappedNumber2 + 1
            ):  # loop through all numbers between the swapped values
                if num in list_of_non_prime_numbers:  # if the number is non-prime
                    print(num, end=" ")  # print the number
                    count += 1  # incrementing the count of printed numbers
                    if count % 10 == 0:  # if 10 numbers have been printed
                        print()  # print new line
            break

# Function to get list of all non-prime numbers
def getListOfNonPrimeNumbers(num1, num2):
    """This function outputs a list of non-prime numbers between two positive integers.

    argument(s):
        num1(int): first positive integer
        num2(int): second positive integer

    returns:
        A list of non-prime numbers between num1 and num2, inclusive.
    """
    non_primes_list = []  # To hold the non-prime numbers,create an empty list
    for num in range(
        num1, num2 + 1
    ):  # iterate over each number between the specified values.
        if num > 1:
            is_prime = True  # assuming the number is prime
            for i in range(
                2, int(num**0.5) + 1
            ):  # iterate over all factors up to the square root of the number.
                if (num % i) == 0:  # if the number is divisible by the factor
                    is_prime = False  # set the number as non-prime
                    break
            if not is_prime:
                non_primes_list.append(
                    num
                )  # include the number in the list of non-prime numbers,if the number is non-prime
    return non_primes_list  # returning a the list of non-prime numbers


# Call the function to begin the program
getNonPrimeNumbersBetweenIntegers()
