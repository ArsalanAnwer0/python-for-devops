def printOptions():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def Calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            result = num1 + num2
            print(result)
        case 2:
            result = num1 - num2
            print(result)
        case 3:
            result = num1 * num2
            print(result)
        case 4:
            result = num1 / num2
            print(int(result))
        case _: # Default Case 
            print("Enter valid input")


print("Simple Calculator")
printOptions()
Calculator()
while True:
    choice_two = input("Again? ").strip().lower()
    if choice_two == "yes":
        Calculator()
    elif choice_two == "no":
        break












