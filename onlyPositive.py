def onlyPositive(num):
    return f(num)


def f(x):
    return abs(x) + 1


if __name__ == '__main2__':
    g = onlyPositive(f)
    print(g(int(input("Enter a number: "))))
