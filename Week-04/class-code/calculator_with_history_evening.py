print("=----=Calculator With History=----=")

counter = 0
histories = []
running = True

while running:
    print("*"*35)
    print(f"{'Main Menu':^35}")
    print("*"*35)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show Hisotry")
    print("6. Clear History")
    print("7. Exit")

    op = input("\nChoose an Option : ")
    print("="*35)

    if op in "1234":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))
        if op == '1':
            calculation = f"{num1} + {num2} = {num1 + num2}"
        elif op == '2':
            calculation = f"{num1} - {num2} = {num1 - num2}"
        elif op == '3':
            calculation = f"{num1} * {num2} = {num1 * num2}"
        else:
            if num2 == 0:
                print("Error: Can't divide by zero")
            else:
                calculation = f"{num1} / {num2} = {num1 / num2}"
        
        if num2 != 0:
            print(calculation)
            histories.append(calculation)
            counter += 1

    elif op == '5':
        print("------Calculation History------")
        if histories:
            for ind in range(len(histories)):
                print(f"{ind+1} {histories[ind]}")
        else:
            print("Hisoty Not Found!")
    elif op == '6':
        print("---------Clear Hisotry---------")
        histories.clear()
        print("History Cleared!")
    elif op == '7':
        running = False
        print(f"You Performed {counter} Operations")
        print("Good Bye!")
    else:
        print("Invalid option, try again")