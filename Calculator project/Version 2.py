def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


def calculator():
    x = input("x: ")
    if not x.isdigit():
        print("Please input a number!")
        return

    y = input("y: ")
    if not y.isdigit():
        print("Please input a number!")
        return

    x = int(x)
    y = int(y)
    operator = input("Operator (+, -, /, *): ")

    if operator == "*":
        result = multiply(x, y)

    elif operator == "/":
        if y == 0:
            print("You can't divide by 0.")
            return
        result = divide(x, y)

    elif operator == "+":
        result = add(x, y)

    elif operator == "-":
        result = subtract(x, y)

    else:
        print("There is not operator like this!")
        return

    print(f"{x} {operator} {y} = {result}")


calculator()
