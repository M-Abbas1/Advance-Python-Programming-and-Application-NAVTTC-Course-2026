# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print(f"{'Simple Calculator'.upper():^40}")
print("*"*40)
print("1. Addition +")
print("2. Subtraction -")
print("3. Multiplication *")
print("4. Division /")
print("5. Modulus %")
print("6. Floor Division //")
print("7. Power **")
print("8. Exit")

choice = input("Choose an Operation (1-8) : ")
print("*"*40)

if choice != '8':
    print(f"{'USER INPUT':^40}")
    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number : "))
    print("*"*40)

    op_result = None
    if choice == '1':
        op_result = num1 + num2
    elif choice == '2':
        op_result = num1 - num2
    elif choice == '3':
        op_result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            print("Can't Divide a number by zero")
        else:
            op_result = num1 / num2
    elif choice == '5':
        op_result = num1 % num2
    elif choice == '6':
        op_result = num1 // num2
    elif choice == '7':
        op_result = num1 ** num2
    else:
        print("Choose a valid operation")
    
    # if choice != '8':
    print(f"{'OUPUT':^40}")
    print(f"Result : {op_result}")
else:
    print("THANK YOU")
    print("Application Closed")
