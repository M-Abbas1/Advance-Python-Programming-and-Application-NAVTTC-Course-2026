# ===============================================
# COMMAND LINE BANK APPLICATION
# ===============================================
# Topics Used: Print, Variables, Operators, Conditionals
# No loops, no functions - pure sequential programming
# ===============================================

print("=" * 50)
print("      WELCOME TO PYTHON BANK")
print("=" * 50)
print()

# ===============================================
# PRE-DEFINED USER DATA
# ===============================================
# In a real application, this would come from a database
# For now, we have one predefined user account

correct_username = "john"
correct_password = "pass123"
account_balance = 1000.00
transaction_count = 0

# ===============================================
# LOGIN SYSTEM
# ===============================================
print("Please login to continue")
print("-" * 50)

# Get username
username = input("Enter username: ")

# Get password
password = input("Enter password: ")

print()

# Validate credentials
if username == correct_username and password == correct_password:
    print("✓ Login successful!")
    print(f"Welcome back, {username.upper()}!")
    print()
    
    # ===============================================
    # MAIN MENU
    # ===============================================
    print("=" * 50)
    print("           MAIN MENU")
    print("=" * 50)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Account Information")
    print("6. Exit")
    print("=" * 50)
    print()
    
    # Get user choice
    choice = input("Enter your choice (1-6): ")
    print()
    
    # ===============================================
    # OPTION 1: CHECK BALANCE
    # ===============================================
    if choice == "1":
        print("=" * 50)
        print("         ACCOUNT BALANCE")
        print("=" * 50)
        print(f"Account Holder: {username.upper()}")
        print(f"Current Balance: ${account_balance:.2f}")
        print(f"Total Transactions: {transaction_count}")
        print("=" * 50)
    
    # ===============================================
    # OPTION 2: DEPOSIT MONEY
    # ===============================================
    elif choice == "2":
        print("=" * 50)
        print("         DEPOSIT MONEY")
        print("=" * 50)
        print(f"Current Balance: ${account_balance:.2f}")
        print()
        
        # Get deposit amount
        deposit_amount = input("Enter amount to deposit: $")
        
        # Convert to float
        deposit_amount = float(deposit_amount)
        
        # Validate deposit amount
        if deposit_amount <= 0:
            print()
            print("✗ Error: Deposit amount must be positive!")
        elif deposit_amount > 10000:
            print()
            print("✗ Error: Cannot deposit more than $10,000 at once!")
        else:
            # Process deposit
            account_balance = account_balance + deposit_amount
            transaction_count = transaction_count + 1
            
            print()
            print("✓ Deposit successful!")
            print("-" * 50)
            print(f"Deposited Amount: ${deposit_amount:.2f}")
            print(f"New Balance: ${account_balance:.2f}")
            print(f"Transaction #: {transaction_count}")
        
        print("=" * 50)
    
    # ===============================================
    # OPTION 3: WITHDRAW MONEY
    # ===============================================
    elif choice == "3":
        print("=" * 50)
        print("         WITHDRAW MONEY")
        print("=" * 50)
        print(f"Current Balance: ${account_balance:.2f}")
        print(f"Daily Withdrawal Limit: $500.00")
        print()
        
        # Get withdrawal amount
        withdrawal_amount = input("Enter amount to withdraw: $")
        
        # Convert to float
        withdrawal_amount = float(withdrawal_amount)
        
        # Validate withdrawal
        if withdrawal_amount <= 0:
            print()
            print("✗ Error: Withdrawal amount must be positive!")
        elif withdrawal_amount > 500:
            print()
            print("✗ Error: Daily withdrawal limit is $500!")
        elif withdrawal_amount > account_balance:
            print()
            print("✗ Error: Insufficient funds!")
            print(f"Your balance: ${account_balance:.2f}")
        else:
            # Minimum balance check
            remaining_balance = account_balance - withdrawal_amount
            
            if remaining_balance < 100:
                print()
                print("✗ Error: Minimum balance of $100 must be maintained!")
                print(f"Maximum you can withdraw: ${account_balance - 100:.2f}")
            else:
                # Process withdrawal
                account_balance = account_balance - withdrawal_amount
                transaction_count = transaction_count + 1
                
                print()
                print("✓ Withdrawal successful!")
                print("-" * 50)
                print(f"Withdrawn Amount: ${withdrawal_amount:.2f}")
                print(f"New Balance: ${account_balance:.2f}")
                print(f"Transaction #: {transaction_count}")
        
        print("=" * 50)
    
    # ===============================================
    # OPTION 4: TRANSFER MONEY
    # ===============================================
    elif choice == "4":
        print("=" * 50)
        print("         TRANSFER MONEY")
        print("=" * 50)
        print(f"Current Balance: ${account_balance:.2f}")
        print()
        
        # Get recipient details
        recipient_name = input("Enter recipient name: ")
        recipient_account = input("Enter recipient account number: ")
        
        print()
        transfer_amount = input("Enter amount to transfer: $")
        
        # Convert to float
        transfer_amount = float(transfer_amount)
        
        # Validate transfer
        if transfer_amount <= 0:
            print()
            print("✗ Error: Transfer amount must be positive!")
        elif transfer_amount > 1000:
            print()
            print("✗ Error: Transfer limit is $1,000 per transaction!")
        elif transfer_amount > account_balance:
            print()
            print("✗ Error: Insufficient funds!")
            print(f"Your balance: ${account_balance:.2f}")
        else:
            # Check minimum balance after transfer
            remaining_balance = account_balance - transfer_amount
            
            if remaining_balance < 100:
                print()
                print("✗ Error: Minimum balance of $100 must be maintained!")
                print(f"Maximum you can transfer: ${account_balance - 100:.2f}")
            else:
                # Calculate transfer fee (1% of amount, minimum $1)
                transfer_fee = transfer_amount * 0.01
                if transfer_fee < 1:
                    transfer_fee = 1.00
                
                total_deduction = transfer_amount + transfer_fee
                
                # Check if total amount can be deducted
                if total_deduction > account_balance:
                    print()
                    print("✗ Error: Insufficient funds including transfer fee!")
                    print(f"Transfer Amount: ${transfer_amount:.2f}")
                    print(f"Transfer Fee: ${transfer_fee:.2f}")
                    print(f"Total Required: ${total_deduction:.2f}")
                    print(f"Your Balance: ${account_balance:.2f}")
                elif (account_balance - total_deduction) < 100:
                    print()
                    print("✗ Error: Cannot maintain minimum balance after transfer!")
                else:
                    # Process transfer
                    account_balance = account_balance - total_deduction
                    transaction_count = transaction_count + 1
                    
                    print()
                    print("✓ Transfer successful!")
                    print("-" * 50)
                    print(f"Recipient: {recipient_name}")
                    print(f"Account Number: {recipient_account}")
                    print(f"Transfer Amount: ${transfer_amount:.2f}")
                    print(f"Transfer Fee: ${transfer_fee:.2f}")
                    print(f"Total Deducted: ${total_deduction:.2f}")
                    print(f"New Balance: ${account_balance:.2f}")
                    print(f"Transaction #: {transaction_count}")
        
        print("=" * 50)
    
    # ===============================================
    # OPTION 5: ACCOUNT INFORMATION
    # ===============================================
    elif choice == "5":
        print("=" * 50)
        print("       ACCOUNT INFORMATION")
        print("=" * 50)
        print(f"Account Holder: {username.upper()}")
        print(f"Account Number: ACC-2024-{username.upper()}-001")
        print(f"Account Type: Savings Account")
        print(f"Current Balance: ${account_balance:.2f}")
        print(f"Total Transactions: {transaction_count}")
        print()
        print("Account Features:")
        print("  • Minimum Balance: $100.00")
        print("  • Daily Withdrawal Limit: $500.00")
        print("  • Transfer Limit: $1,000.00 per transaction")
        print("  • Deposit Limit: $10,000.00 per transaction")
        print("  • Transfer Fee: 1% (minimum $1.00)")
        print()
        
        # Account status based on balance
        if account_balance < 100:
            status = "⚠ Below Minimum Balance"
            status_color = "RED"
        elif account_balance >= 100 and account_balance < 1000:
            status = "✓ Active (Standard)"
            status_color = "YELLOW"
        elif account_balance >= 1000 and account_balance < 5000:
            status = "✓ Active (Good Standing)"
            status_color = "GREEN"
        else:
            status = "★ Active (Premium)"
            status_color = "GOLD"
        
        print(f"Account Status: {status}")
        print("=" * 50)
    
    # ===============================================
    # OPTION 6: EXIT
    # ===============================================
    elif choice == "6":
        print("=" * 50)
        print("         THANK YOU!")
        print("=" * 50)
        print(f"Goodbye, {username.upper()}!")
        print("Your session has ended.")
        print(f"Final Balance: ${account_balance:.2f}")
        print()
        print("Thank you for banking with Python Bank!")
        print("Have a great day!")
        print("=" * 50)
    
    # ===============================================
    # INVALID CHOICE
    # ===============================================
    else:
        print("=" * 50)
        print("✗ ERROR: Invalid choice!")
        print("=" * 50)
        print("Please enter a number between 1 and 6")
        print("Returning to main menu...")
        print("=" * 50)

# ===============================================
# LOGIN FAILED
# ===============================================
else:
    print("✗ Login failed!")
    print("-" * 50)
    
    # Check what went wrong
    if username != correct_username and password != correct_password:
        print("Error: Both username and password are incorrect")
    elif username != correct_username:
        print("Error: Username is incorrect")
    else:
        print("Error: Password is incorrect")
    
    print()
    print("Please try again.")
    print("=" * 50)

# ===============================================
# END OF APPLICATION
# ===============================================
print()
print("Application closed.")
