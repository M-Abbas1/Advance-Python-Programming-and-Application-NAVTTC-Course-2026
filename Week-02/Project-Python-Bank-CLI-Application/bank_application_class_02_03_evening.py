

print("*"*40)
print(f"{'WELCOME TO PYTHON BANK':^40}")
print("*"*40)
print(f"{'login'.upper():^40}")


# data
actual_username = "python"
actual_password = "py123"
account_balance = 100000
total_transaction = 0


username = input("Enter Username : ")
password = input("Enter Password : ")


if username == actual_username and password == actual_password:
    print("-"*40)
    print(f"{'LOGIN SUCCESSFULL!':^40}")
    print(f"           WELCOME BACK {username}")
    print("-"*40)

    # main menu
    print(f"{'MAIN MENU':^40}")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfor Money")
    print("5. Account Information")
    print("6. Exit")
    print()
    choice = input("What do you want to perform (1-6): ") 

    print("*"*40)

    #check balance
    if choice == '1':
        print(f"{"ACCOUNT BALANCE":^40}")
        print("*"*40)
        print(f"Account Holder : {username}")
        print(f"Current Balance : ${account_balance}")
        print(f"Total Transcation : {total_transaction}")
        print("*"*40)

    #Deposit Money
    elif choice == '2':
        print(f"{"DEPOSIT MONEY":^40}")
        print("*"*40)

        print(f"Current Balance : ${account_balance}")
        print(f"Daily Deposit Limit : $10000")
        print()

        deposit_amount = input("Enter Amount to Deposit : $")
        deposit_amount = float(deposit_amount)

        if deposit_amount <= 0:
            print("Are you mad, how can you deposit negative amount into your account")
        elif deposit_amount > 10000:
            print("You are not bilinior, daily deposit limit is 10000")
        else:

            confirm = input(f"Do you want to deposit ${deposit_amount} y/n: ")
            if confirm == 'y' or confirm == 'Y':
                account_balance += deposit_amount
                total_transaction += 1  # total_transaction = total_transaction + 1

                print("Deposit Successful!")
                print(f"New Balance : ${account_balance}")
                print(f"Deposited amount ${deposit_amount}")
                print(f"Total Transactions : {total_transaction}")
                print("*"*40)
            else:
                print("Deposit Conaceled!")

    #Withdraw money
    elif choice == '3':
        print(f"{"WITHDRAW MONEY":^40}")
        print("*"*40)
        print(f"Current Balance : {account_balance}")
        print(f"Daily Withdrawal limit : $20000")
        print()

        withdraw_amount = input("Enter amount you want to withdraw : $")
        withdraw_amount = float(withdraw_amount)

        if withdraw_amount <= 0:
            print("Mujhy be waqoof banan raha hai")
        elif withdraw_amount >20000:
            print("Ap ne etny dollars ka keya kerna hai")
        elif withdraw_amount > account_balance:
            print("not possible, daily withdrawal 20000")
        else:

            confirm = input("ary sach main kerna chahta hai withdrawal y/n : ")
            if confirm == 'y' or confirm == 'Y':
                account_balance -= withdraw_amount
                total_transaction += 1

                print("Withdrawal Successfull")
                print(f"New Balance : {account_balance}")
                print(f"Withdraw Amount : {withdraw_amount}")
                print(f"Total Transaction: {total_transaction}")
                print("*"*40)
            else:
                print("withdrawal Conceled")

    elif choice == '4':
        print(f"{'TRANSFOR MONEY':^40}")
        print("*"*40)
        print(f"Current Balance : ${account_balance}")
        print(f"Daily Transfor Amount : $10000")
        print()

        receiver_name = input("Enter Account Name : ")
        receiver_account = input("Enter Account Number : ")
        print("Account Exits!")
        print()

        transfor_amount = input("Enter amount you want to transfor : $")
        transfor_amount = float(transfor_amount)

        if transfor_amount <= 0:
            print("ERROR: Transfor amount must be positive!")
        elif transfor_amount > 10000:
            print("ERROR: You need to pay extra tax for more than $10000 transfor")
        elif transfor_amount > account_balance:
            print("ERROR: Insufficient Balance")
        else:
            confirm = input(f"Do you want to transfor ${transfor_amount} y/n :")
            if confirm == 'y' or confirm == "Y":
                account_balance -= transfor_amount
                total_transaction += 1

                print()
                print(f"An amount of ${transfor_amount} has successfuly transfored to {receiver_name}.")
                print(f"Remaining Balance : {account_balance}")
                print(f"Total Transactions : {total_transaction}")
                print("*"*40)
            else:
                print("Transfor Canceled!")


    elif choice == '5':
        print(f"{'ACCOUNT INFORMATION':^40}")
        print("*"*40)
        print(f"Account Holder : {username}")
        print(f"Account Balance : ${account_balance}")
        print(f"Total Transactions : {total_transaction}")
        print()

        print("Daily Transfore limit : $10000")
        print("Daily Deposit limit : $10000")
        print("Daily Withdrawal limit : $20000")
        print("*"*40)


    elif choice == '6':
        print("THANK for banking with PYTHON BANK")
        print("Your Session ends here")
        print("Good Bye ", username)
        print("Application Closed")

    else:
        print("select a valid option")


else:
    if username != actual_username and password != actual_password:
        print("Error: Both Username and Password is incorrect!")
    elif username != actual_username:
        print("Error: Invalid Username")
    else:
        print("Error: Invalid Password")
        
