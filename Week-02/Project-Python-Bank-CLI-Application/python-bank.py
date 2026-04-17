print("*"*40)
print(f"{'WELCOME TO PYTHON BANK':^40}")
print("*"*40)
print(f"{'LOGIN':^40}")

# Default Login Credentials
username = "john"
password = "pass123"
account_balance = 1000.00
transaction_count = 0

# Get user credentials
input_username = input("Enter Your Name \t: ")
input_password = input("Enter Your Password \t: ")


# check user credentials with actual data
if username == input_username and password == input_password:
    print("*" * 40)
    print(f"{'Login Successful!':^40}")
    print(f"           WELCOME BACK {username.upper()}!")

    print("-"*40)
    print(f"{'MAIN MENU':^40}")
    print("-"*40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfor Money")
    print("5. Account Information")
    print("6. Exit")
    print("*"*40)

    choice = input("Enter Your Choice (1-6) : ")


    if choice == "1":
        print("*"*40)
        print(f"{'ACCOUNT BALANCE':^40}")
        print("*"*40)
        print(f"Account Holder \t: {username.upper()}")
        print(f"Current Balance \t: ${account_balance:.2f}")
        print(f"Total Transactions \t: {transaction_count} ")
        print("*"*40)
    

    elif choice == "2":
        print("*"*40)
        print(f"{'DEPOSIT MONEY':^40}")
        print("*"*40)
        print(f"Current Balance : ${account_balance:.2f}")

        deposit_amount = input("Enter the amount to deposit : $")

        deposit_amount = float(deposit_amount)

        if deposit_amount <= 0:
            print("ERROR: Deposit amount must be positive!")
        elif deposit_amount > 10000:
            print("ERROR: You Can't deposit more than $10,000 at once!")
        else:
            account_balance += deposit_amount
            transaction_count += 1

            print("Deposit Successful!")
            print("*"*40)
            print(f"Deposit Amount : {deposit_amount}")
            print(f"New Balance : {account_balance:.2f}")
            print(f"Total Transactions : {transaction_count}")
        print("*"*40)


    
    elif choice == "3":
        print("Withdrawal will happen here")



    elif choice == "4":
        print("Here we will transfor money to another account")



    elif choice == "5":
        print("The account informations will be shown here")


    
    elif choice == "6":
        print("*"*40)
        print(f"{'THANK YOU!':^40}")
        print("*"*40)

        print(f"Goodbye {username.upper()}!")
        print("Your session has ended.")
        print(f"Final Balance: ${account_balance:.2f}")
        print("Thank you for banking with PYTHON bank!")
        print("have a greate day")
        print("*"*40)




else:
    print("✗ Login Failed")
    print("-"*40)

    if username != input_username:
        print("ERROR: Username is incorrect!")
    elif password != input_password:
        print("ERROR: Password is incorrect!")
    else:
        print("ERROR: Both Username and Password is incorrect!")

    print("Please try again.")
    print("="*40)



want_close = input("Do you want to close the application! (y/n)")
if want_close == 'y' or want_close == 'Y':
    print(f"{'THANK YOU':^40}")
    print(f"{'Application Closed!':^40}")
else:
    input()



    





