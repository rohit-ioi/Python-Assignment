num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

operator = input("Enter the operator: ")

match operator:
    case "+":
        print("The sum is", num1 + num2)
    case "-":
        print("The difference is:", num1 - num2)
    case "*":
        print("The product is:",num1 * num2)
    case "/":
        print("The Division is:", num1 / num2)
    case _:
        print("Enter a valid operator")
       
