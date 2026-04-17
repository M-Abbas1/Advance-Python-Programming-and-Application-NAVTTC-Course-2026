print("-----Calculator With History-----")

histories = []
running = True


while running:
    print("*"*40)
    print(f"{'Main Menu':^40}")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Shown Hisotry")
    print("6. Clear History")
    print("7. Exit")

    op = input("What Do You Want! : ")

    if op in "1234":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))

        cur_calculation = ""

        if op == '1':
            result = num1 + num2   # '23 + 27 = 50' 
            cur_calculation = f"{num1} + {num2} = {result}"
        elif op == '2':
            result = num1 - num2
            cur_calculation = f"{num1} - {num2} = {result}"
        elif op == '3':
            result = num1 * num2
            cur_calculation = f"{num1} * {num2} = {result}"
        else:
            if num2 != 0:
                result = num1/num2
                cur_calculation = f"{num1} / {num2} = {result}"
            else:
                print("Error: Can't Divide a Number by Zero 0!")
                continue

        print("Result : ", cur_calculation)
        histories.append(cur_calculation)
    else:
        if op == '5':
            print("*"*40)
            print("-----Calculation Hisotry-----")
            if histories:
                for ind, history in enumerate(histories):
                    print(f"{ind+1}. {history}")
            else:
                print("History not found")

        elif op == '6':
            histories.clear()
            print("History Cleared")
        elif op == '7':
            print("Thanks")
            running = False
        else:
            print("Enter a valid option")

    
        

