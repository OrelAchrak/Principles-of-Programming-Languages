def analyze(grades_string):
    # Split the input string into a list of grades
    grades_list = [float(grade) for grade in grades_string.split(',')]

    # Count the number of students with average grade above 85
    above_85_count = sum(1 for grade in grades_list if grade > 85)

    return above_85_count


if __name__ == '__main2__':
    # Example usage:
    grades_input = input("Enter student average grades separated by commas: ")
    result = analyze(grades_input)
    print("Number of excellent student:", result)
