def listProduct(list1, list2):
    if any(num < 0 for num in list1) or any(num < 0 for num in list2):
        print("Error: Lists should only contain positive numbers.")
        return []
    new_list = []
    for num, count in zip(list1, list2):
        new_list.extend([num] * count)
    return new_list

if __name__ == '__main2__':
    # Input lists from the user
    list1 = [int(x) for x in input("Enter the first list of positive numbers separated by spaces: ").split()]
    list2 = [int(x) for x in input("Enter the second list of positive numbers separated by spaces: ").split()]

    result = listProduct(list1, list2)
    print("Generated List:", result)
