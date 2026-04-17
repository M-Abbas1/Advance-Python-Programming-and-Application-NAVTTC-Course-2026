## Command Line Bank Application

print("*"*40)
print(f"{'WELCOME TO PYTHON BANK':^40}")
print("*"*40)

# Actual Data of the user
username = "john"
password = "pass123"
account_balance = 10000.00
transaction_count = 0



print(f"{'LOGIN':^40}")

input_username = input("Enter Username : ")
input_password = input("Enter Password : ")

running = True

if username == input_username and password == input_password:
    print("-"*40)
    print(f"{'Login Successful!':^40}")
    print(f"           WELCOME BACK {username.upper()}!")
    print("-"*40)

    while running:
        print(f"{'MAIN MENU':^40}")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfor Money")
        print("5. Account Information")
        print("6. Exit")

        print()
        choice = input("Enter an option to proceed (1-6): ")
        print("*"*40)

        # Account Balance 
        if choice == '1':
            print(f"{"ACCOUNT BALANCE":^40}")
            print("*"*40)
            print(f"Account Holder : {username}")
            print(f"Current Balance : {account_balance:.2f}")
            print(f"Total Transaction : {transaction_count}")
            print("*"*40)

        # Deposit Money
        elif choice == '2':
            print(f"{'DEPOSIT MONEY':^40}")
            print("*"*40)
            print(f"Current Balance {account_balance}")
            print("Daily Deposit Limit : $10,000")
            print()

            deposit_money = input("Enter Amount To Deposit : ")
            deposit_money = float(deposit_money)

            if deposit_money <= 0:
                print("ERROR: Deposit Amount must be Positive")
            elif deposit_money >10000:
                print("ERROR: You Can't deposit more than 10000 at once!")
            else:

                confirm = input(f"Do You want to Deposit {deposit_money}  y/n : ")

                if confirm=='y' or confirm=='Y':
                    account_balance += deposit_money
                    transaction_count += 1

                    print("-"*40)
                    print("Deposit Successful!")
                    print("-"*40)
                    print(f"Deposit Amount :  {deposit_money}")
                    print(f"New Balance : {account_balance:.2f}")
                    print(f"Total Transactions :  ${transaction_count}")
                    print("*"*40)
                else:
                    print("Transaction Conceled!")

        # withdraw money
        elif choice == '3':
            print(f"{'WITHDRAW MONEY':^40}")
            print(f"*"*40)
            print(f"Current Balance : ${account_balance}")
            print(f"Daily Withdrawal limit : $500")
            print()

            withdraw_amount = input("Enter amount to withdraw : $")
            withdraw_amount = float(withdraw_amount)

            if withdraw_amount <= 0:
                print("ERROR: Withdrawal amount must be positive!")
            elif withdraw_amount > account_balance:
                print("ERROR: Insufficient Balance")
            elif withdraw_amount > 500:
                print("ERROR: Daily withdrawal limit is $500")
            else:
                confirm = input(f"Do you want to withdraw ${withdraw_amount} y/n : ")

                if confirm == 'y' or confirm == "Y":

                    account_balance -= withdraw_amount
                    transaction_count += 1

                    print("Withdrawal Successfull!")
                    print("-"*40)
                    print(f"Remaining Balance ${account_balance}")
                    print(f"Withdraw Amount ${withdraw_amount}")
                    print(f"Total Transactions : {transaction_count}")
                    print("*"*40)
                else:
                    print("Withdrawal Conceled!")



        elif choice == '4':
            print(f"{'TRANSFOR MONEY':^40}")
            print("*"*40)
            print(f"Current Balance ${account_balance}")
            print("Daily Transfor Limit is $1000")
            print()

            rec_account_holder = input("Enter name of the Recipent : ")
            rec_account_number = input("Enter Accout Number : ")

            print("*"*40)

            transfor_amount = input("Enter Amount to Transfor  : $")
            transfor_amount = float(transfor_amount)

            if transfor_amount <= 0:
                print("ERROR: Transfor amount must be positive!")
            elif transfor_amount >= account_balance:
                print("ERROR: Insufficient Balance!")
            elif transfor_amount > 1000:
                print("ERROR: Your daily transfor limit is $1000")
            else:
                confirm = input(f"Do You Want to Transfor ${transfor_amount} y/n : ")

                if confirm == 'y' or confirm == 'Y':
                    
                    account_balance -= transfor_amount
                    transaction_count += 1

                    print(f"${transfor_amount} is successfully transfored to {rec_account_holder}")
                    print("-"*40)

                    print(f"Recipint Name : {rec_account_holder}")
                    print(f"Recipent Account Number : {rec_account_number}")
                    print(f"Transfored Amount : ${transfor_amount}")
                    print(f"Remaining Balance : $ {account_balance}")
                    print(f"Total Transactions : {transaction_count}")
                    print("*"*40)
                else:
                    print("Money Transfored canceled!")
            
        
        # Account Information
        elif choice == '5':
            print(f"{'ACCOUNT INFORMATION':^40}")
            print("*"*40)
            print(f"Account Holder Name : {username}")
            print(f"Current Balance : ${account_balance}")
            print(f"Total Transactions : {transaction_count}")
            print()

            print("-"*40)
            print("Daily Transfor Limit : $1000")
            print("Daily Withdrawal Limit : $500")
            print("Daily Deposit Limit : $10,000")
            print("*"*40)

        elif choice == '6':
            print(f"{'THANK YOU':^40}")
            print(f"Goodbye {username}")
            print("Your session ended here.")
            print("Thank you for banking with PYTHON Bank!")
            print("Have a good day!")
            print("Application Closed")
            print("*"*40)
            
            running = False

        else:
            print(f"{'ERROR':^40}")
            print("Please Enter a valid option")
            print("try again")
    

else:
    print("*"*40)
    print(f"{'Login Failed!':^40}")
    print("-"*40)
    if username != input_username and password != input_password:
        print("ERROR: Both username and password are incorrect!")
    elif username != input_username:
        print("ERROR: invalid username")
    else:
        print("ERROR: invalid password")

    print("Please try again")
    print("Application closed")
