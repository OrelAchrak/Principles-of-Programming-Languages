def onlyPositive(f):
    return f

def f (x):
    return abs(x)+1

g = onlyPositive(f)
print(g(int(input("Enter a number: "))))