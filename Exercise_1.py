# Author: Madhushree Somendyapnhalli Venkatesh Murthy
# PRID: SOMEN73309
# Registration number(s): 2214000
# University username: ms22749
# University email address: ms22749@essex.ac.uk
# Module: CE156 - An Approachable Introduction to Programming
# Module Supervisor: Dr Mike Sanderson

# Exercise 1

# Import the required modules.
from datetime import datetime, date
import re
import calendar


def getAgeAndDateOfBirthInEuropeanFormat():
    """When a user enters their birthdate in the required format, his or her age and birthdate are displayed in European format.
    argument(s):
        None

    Returns:
        Displays user's age and birthdate in European format, or message if the date entered is invalid.
    """
    while True:
        # Request the user's birthdate
        birth_date_str = input(
            "Please enter your date of birth in the valid format of mm/dd/yyyy: "
        )
        try:
            # birth_date_str string to date object conversion
            dob = datetime.strptime(birth_date_str, "%m/%d/%Y").date()
            # Verify the birthdate to see if it is recent.
            if dob > date.today():
                print("Invalid date. Dates from the past should be entered.")
            else:
                # Determine the age and provide the results if the birthdate is in the past.
                age = getAge(dob)
                if age == 0:
                    print(
                        "You are born this year! Enjoy your first steps on this wonderful green planet earth!"
                    )
                    break
                else:
                    # Display the age and birthdate in European format
                    print(f"Your age: {age}")
                    print(f"Birth date (European format): {dob.strftime('%d/%m/%Y')}")
                    break
        except ValueError:
            print("Invalid date format entered.")
        except:
            print("An error occurred. Please try again.")


# Function to calculate user's age
def getAge(dob):
    """Determines a user's age.

    argument(s):
        dob(str) : Birthdate of the user

    returns:
        Provides an integer age for the user.
    """
    # Get today's date
    today = date.today()
    # Age calculation using the birthdate and the current date
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


# Call the function to begin the program
getAgeAndDateOfBirthInEuropeanFormat()
