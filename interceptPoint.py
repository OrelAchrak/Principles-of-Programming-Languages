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

# Example usage:
a1 = float(input("insert x1 coefficient: "))
b1 = float(input("insert c1: "))
a2 = float(input("insert x2 coefficient: "))
b2 = float(input("insert c2: "))
line1 = (a1, b1)  # y = a1x + b1
line2 = (a2, b2)  # y = a2x + b2

result = interceptPoint(line1, line2)
print("Intercept Point:", result)
