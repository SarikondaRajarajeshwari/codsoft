def calculator():
    choice=1
    while(True):
        # Prompt the user for two numbers
        
        if choice==1:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("Choose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            
            operation = input("Enter the number corresponding to the operation: ")

            # Perform the calculation based on the chosen operation
            if operation == '1':
                result = num1 + num2
                operation_symbol = '+'
            elif operation == '2':
                result = num1 - num2
                operation_symbol = '-'
            elif operation == '3':
                result = num1 * num2
                operation_symbol = '*'
            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                    operation_symbol = '/'
                else:
                    print("Error: Division by zero is not allowed.")
                    return
            else:
                print("Invalid operation choice.")
                return
             # Display the result
            print(f"The result of {num1} {operation_symbol} {num2} is {result}")
            choice=int(input("enter 1 to continue 0 to exit"))
        else:
            break
       

# Call the calculator function
calculator()