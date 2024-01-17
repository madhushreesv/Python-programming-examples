# Author: Madhushree Somendyapnhalli Venkatesh Murthy
# PRID: SOMEN73309
# Registration number(s): 2214000
# University username: ms22749
# University email address: ms22749@essex.ac.uk
# Module: CE156 - An Approachable Introduction to Programming
# Module Supervisor: Dr Mike Sanderson

# Exercise 4

# Import the required modules.
import pandas as pd

# Function should output the names and job titles of all employees in the list in a well formatted table.
def getEmployeeeData(employee_list, salary1, salary2):
    """Filters a list of tuples containing employee names, job titles, and salaries to only include those whose salaries fall within a certain range,
    sorts the list by salary (biggest first),and outputs the names and job titles of those individuals in a well organised table.

    argument(s):
        employee_list (list of tuples): A list of tuples containing employee names (string), job titles (string), and salaries (integer)
        salary1 (int): Employee's starting wage to filter
        salary2 (int): Employee's highest possible pay to filter

    returns:
        str: A formatted table string with the name, job title, and salary of each employee in the filtered list,
             sorted by salary in descending order, or a message indicating there were no matches.
    """
    # filter employees based on the salary range
    filtered_list = [
        (name, job_title, int(salary))
        for name, job_title, salary in employee_list
        if salary1 <= int(salary) <= salary2
    ]

    # sort the filtered list in descending order
    sorted_list_desc = sorted(filtered_list, key=lambda x: x[2], reverse=True)

    # if no employees found in the specified salary range, return an error message
    if len(sorted_list_desc) == 0:
        print("There were no employees within the desired pay range.")
        return

    # Format the table
    table = []
    table.append(["Name", "Job Title", "Salary"])
    table.append(["-" * 15, "-" * 15, "-" * 10])

    # add the employee information to the table
    for name, job_title, salary in sorted_list_desc:
        table.append([name, job_title, "{:,.2f}".format(salary)])

    # Print a neatly formatted table
    print()  # print a new line
    print("The following are the List of Employees between the supplied salary range:")
    # calculate the max width of each column based on the content in that column
    column_widths = [
        max(len(row[i]) for row in table) + 2 for i in range(len(table[0]))
    ]
    # format the table as a string
    for row in table:
        print("|".join(word.ljust(column_widths[i]) for i, word in enumerate(row)))


# Main program that  program that asks the user to supply a file name and attempts to open the file for reading and calls the
# get_employees_by_salary() function internally to output the names and job titles of those individuals in a nicely designed table.
def getEmployeeListByDesiredSalaryRange():
    """A pandas dataframe containing the named columns "Name," "Job Title," and "Salary" is read from a csv file that the user has typed.
    To ensure that the data was correctly read, it shows the dataframe's contents.
    After asking the user for a salary range, it enters a loop where it runs the get_employees_by_salary function to list any employees that match.
    The user is also asked if they wish to quit or select a different pay range.

    argument(s):
        None

    returns:
         str: A neatly formatted table displaying one employee per line, sorted by salary(largest first)
    """


while True: #process continues until a file has been opened successfully.
    fileName = input("Enter file name: ")
    try:
        # read the csv file
        employees = pd.read_csv(
            fileName, skiprows=1, names=["Name", "Job Title", "Salary"]
        )
        # convert the 'Salary' column from object to integer
        employees["Salary"] = employees["Salary"].astype(int)
        employee_list = list(employees.to_records(index=False))
        # print the employee list to verify that the tuples have been created correctly so no formatting is required
        print(employee_list)
        while True:
            try:
                # get the minimum and maximum salary values from the user
                salary1 = int(input("Enter the starting wage:"))
                salary2 = int(input("Enter the highest pay possible:"))

            except ValueError:
                print("You have entered a non-numeric value.")

            # Verify the input is correct.
            if salary1 <= 0 or salary2 <= 0:  # if either number is not positive
                print("You have entered a non-positive value")  # print error message
            else:
                # Swap the salaries if the user enters the numbers in the "either" order
                if (
                    salary1 > salary2
                ):  # if the first number is greater than the second number
                    getEmployeeeData(employee_list, salary2, salary1)
                else:
                    getEmployeeeData(employee_list, salary1, salary2)
                    # Ask user if he/she wishes to quit or to supply another salary range.
                    choice = input("Do you wish to enter a different wage range? (y/n)")
                    if choice.lower() != "y":
                        break
        break
    except FileNotFoundError:
        # if the file is not found, ask the user to enter a valid file name
        print("Unable to find the file. Please enter a valid file name.")

# Call the function to begin the program
getEmployeeListByDesiredSalaryRange()
