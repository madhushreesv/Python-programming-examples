# Author: Madhushree 

# Exercise 5

# Import the required modules.
import numpy as np


def getUniversityModuleMarks():
    """This function outputs a sorted list of students data based on their grades into a file and also
        outputs the count the number of students in each grade category and
        the registration numbers of students who failed on the screen

        argument(s):
            None.

        returns:
            output sorted array to an output file
    .
    """
    # Getting the input filename from user
    inputFileName = input("Enter file name:")

    # Read the file's first line after opening it.
    with open(inputFileName, "r") as f:
        n, coursework_weighting = map(
            float, f.readline().split()
        )  # n is the number of students.
        n = int(n)

        # Create a  2-dimensional numpy array to store the data
        array1 = np.array([[0, 0.0, 0.0, 0.0]] * n, dtype=np.float64)
        # Iterate through the input file and read each line to get the data.Each row has 4 elements.
        for i in range(n):
            regno, exam, coursework = map(float, f.readline().split())
            # Calculate the overall score and round it to the nearest integer
            overall = round(
                exam * (1 - coursework_weighting / 100)
                + coursework * (coursework_weighting / 100)
            )
            # Add the data to the numpy array
            array1[i] = [regno, exam, coursework, overall]

    # Named data type whose fields are 4 integers and one fixed-length string.
    studType = np.dtype(
        [
            ("regno", "int32"),
            ("exam", "int32"),
            ("coursework", "int32"),
            ("overall", "int32"),
            ("grade", "U2"),
        ]
    )
    # Creating a 1-dimensional numpy array with n elements, using the above named type
    array2 = np.array([(0, 0, 0, 0, "")] * n, dtype=studType)

    # Loop over the data and calculate the grade for each student
    for i in range(n):
        regno, exam, coursework, overall = map(int, array1[i])
        # Determine the grade based on the overall marks
        if exam < 30 or coursework < 30:
            grade = "F"
        elif overall >= 70:
            grade = "1"
        elif overall >= 50:
            grade = "2"
        elif overall >= 40:
            grade = "3"
        else:
            grade = "F"

        # Add the student data with the grade to the final output numpy array
        array2[i] = (regno, exam, coursework, overall, grade)

    # Sort the final output numpy array in descending order of overall marks
    array2 = np.sort(array2, order="overall")[::-1]

    # Request user to enter the name of the output file
    outputFileName = input("Output filename, please: ")
    # Open the output file in write mode
    with open(outputFileName, "w") as f:
        print(array2, file=f)  # output sorted array to an output file

    # Count the number of students in each grade category and store the registration numbers of students who failed in an array
    num_first = num_second = num_third = num_fail = 0
    failed_regnos = []
    for regno, exam, coursework, overall, grade in array2:
        if grade == "1":
            num_first += 1
        elif grade == "2":
            num_second += 1
        elif grade == "3":
            num_third += 1
        else:
            num_fail += 1
            failed_regnos.append(regno)

    print()  # print a new line

    # Output the below results to the screen/console
    table = []
    table.append(["Grades", "Number of students"])
    table.append(["-" * 15, "-" * 15])
    table.append(["First-class", num_first])
    table.append(["Second-class", num_second])
    table.append(["Third-class", num_third])
    table.append(["Failed", num_fail])
    for row in table:
        print("{:<15} {:<15}".format(*row))
    if failed_regnos:
        print()  # print a new line
        print("The registration numbers of students that failed are listed below:")
        print(*failed_regnos, sep="\n")
    else:
        print("All students have passed!")


# Call the function to begin the program
getUniversityModuleMarks()
