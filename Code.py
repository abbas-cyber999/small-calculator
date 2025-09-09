
def calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            print("Result:", num1 + num2)
        case '2':
            print("Result:", num1 - num2)
        case '3':
            print("Result:", num1 * num2)
        case '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")
        case _:
            print("Invalid input!")

calculator()