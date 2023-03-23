def calculator(x, y, operator):
    x, y = int(x), int(y)

    if operator == "*":
        result = x * y

    elif operator == "/":
        if y == 0:
            print("You can't division by 0.")
            return
        result = x / y

    elif operator == "+":
        result = x + y

    elif operator == "-":
        result = x - y

    else:
        print("There is not operator like this!")
        return

    print(f"{x} {operator} {y} = {result}")


calculator(input("x: "), input("y: "), input("Operator (*, /, +, -): "))
