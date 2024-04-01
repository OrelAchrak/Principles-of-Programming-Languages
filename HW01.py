def factorSum(num):
    if num <= 1:
        return None  # Invalid input, as the number should be greater than 1

    prime_factors = []
    for i in range(2, num + 1):
        while num % i == 0 and is_prime(i):
            prime_factors.append(i)
            num //= i
    return sum(set(prime_factors))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def onlyPositive(num):
    return f(num)


def f(x):
    return abs(x) + 1


def interceptPoint(line1, line2):
    a1, b1 = line1
    a2, b2 = line2

    # Check if the lines are parallel
    if a1 == a2:
        return None  # No intercept point

    # Calculate the intercept point
    x_intercept = (b2 - b1) / (a1 - a2)
    y_intercept = a1 * x_intercept + b1

    return (x_intercept, y_intercept)


def printNumbers(start, end, ignore):
    if start < end:
        if start != ignore:
            print(start, end=" ")
        printNumbers(start + 1, end, ignore)
    elif start > end:
        if start != ignore:
            print(start, end=" ")
        printNumbers(start - 1, end, ignore)
    else:
        print(start, end=" ")
        print()


def listProduct(list1, list2):
    if any(num < 0 for num in list1) or any(num < 0 for num in list2):
        print("Error: Lists should only contain positive numbers.")
        return []
    new_list = []
    for num, count in zip(list1, list2):
        new_list.extend([num] * count)
    return new_list


def analyze(grades_string):
    # Split the input string into a list of grades
    grades_list = [float(grade) for grade in grades_string.split(',')]

    # Count the number of students with average grade above 85
    above_85_count = sum(1 for grade in grades_list if grade > 85)

    return above_85_count


print(factorSum(2520))  # question 1
print(onlyPositive(-2))  # question 2
print(interceptPoint((2, 4), (5, -2)))  # question 3
printNumbers(2, -3, -1)  # question 4
print(listProduct([6, 7, 8], [2, 1, 3]))  # question 5
print(analyze("96 , 52.02 , 67.3 , 86.2 , 87.1 , 100"))  # question 6
