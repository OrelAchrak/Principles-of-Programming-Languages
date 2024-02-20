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

if __name__ == '__main2__':
    # Example usage:
    start_value = 2
    end_value = -5
    ignore_value = -2

    print("Numbers from",start_value, "to", end_value, "excluding", ignore_value, "are:")
    printNumbers(start_value, end_value, ignore_value)