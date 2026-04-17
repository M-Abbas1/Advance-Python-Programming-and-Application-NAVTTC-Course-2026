# PYTHON BANK APPLICATION - DOCUMENTATION

## Project Overview
This is a command-line bank application that demonstrates practical use of Python fundamentals including print statements, variables, operators, and conditional statements.

## Default Login Credentials
- **Username:** john
- **Password:** pass123
- **Initial Balance:** $1000.00

## Application Features

### 1. Login System
- Validates username and password
- Provides specific error messages for incorrect credentials
- Denies access if login fails

### 2. Main Menu Options

#### Option 1: Check Balance
- Displays current account balance
- Shows total number of transactions
- Shows account holder name

#### Option 2: Deposit Money
- Allows depositing money into account
- **Validations:**
  - Amount must be positive
  - Maximum deposit: $10,000 per transaction
- Updates balance and transaction count

#### Option 3: Withdraw Money
- Allows withdrawing money from account
- **Validations:**
  - Amount must be positive
  - Daily withdrawal limit: $500
  - Must have sufficient funds
  - Minimum balance of $100 must be maintained
- Updates balance and transaction count

#### Option 4: Transfer Money
- Transfer money to another account
- **Validations:**
  - Amount must be positive
  - Maximum transfer: $1,000 per transaction
  - Must have sufficient funds
  - Minimum balance of $100 must be maintained
  - 1% transfer fee (minimum $1.00)
- Updates balance and transaction count

#### Option 5: Account Information
- Displays complete account details
- Shows account features and limits
- Displays account status based on balance:
  - Below $100: Below Minimum Balance
  - $100-$999: Active (Standard)
  - $1,000-$4,999: Active (Good Standing)
  - $5,000+: Active (Premium)

#### Option 6: Exit
- Shows goodbye message
- Displays final balance
- Ends the session

## Concepts Used

### 1. Print Function
- Basic printing with `print()`
- String formatting with f-strings: `f"Balance: ${balance:.2f}"`
- String repetition for decorative lines: `"=" * 50`
- Formatted output with `.2f` for currency display

### 2. Variables and Data Types
- **Strings:** username, password, account_number
- **Floats:** account_balance, deposit_amount, withdrawal_amount
- **Integers:** transaction_count, choice
- Variable reassignment for updating values

### 3. Operators

#### Arithmetic Operators:
- Addition: `account_balance + deposit_amount`
- Subtraction: `account_balance - withdrawal_amount`
- Multiplication: `transfer_amount * 0.01` (for fee calculation)
- String multiplication: `"=" * 50`

#### Comparison Operators:
- Equal to: `username == correct_username`
- Not equal to: `choice != "6"`
- Greater than: `amount > 1000`
- Less than: `remaining_balance < 100`
- Greater than or equal: `account_balance >= 5000`
- Less than or equal: `withdrawal_amount <= 500`

#### Logical Operators:
- AND: `username == correct_username and password == correct_password`
- OR: `amount <= 0 or amount > 10000`
- NOT: `not (balance > 100)`

#### Assignment Operators:
- Basic: `balance = 1000`
- Compound: `balance = balance + deposit_amount`

### 4. Conditional Statements

#### if-else:
```python
if username == correct_username:
    print("Login successful")
else:
    print("Login failed")
```

#### if-elif-else (Menu selection):
```python
if choice == "1":
    # Check balance
elif choice == "2":
    # Deposit money
elif choice == "3":
    # Withdraw money
else:
    # Invalid choice
```

#### Nested conditionals:
```python
if login_successful:
    if choice == "2":
        if amount > 0:
            if amount <= 10000:
                # Process deposit
```

#### Multiple conditions:
```python
if amount > 0 and amount <= 1000 and balance >= amount:
    # Process transaction
```

## Account Rules and Limits

| Feature | Limit |
|---------|-------|
| Minimum Balance | $100.00 |
| Maximum Deposit | $10,000.00 per transaction |
| Maximum Withdrawal | $500.00 per day |
| Maximum Transfer | $1,000.00 per transaction |
| Transfer Fee | 1% (minimum $1.00) |

## Sample Test Cases

### Test Case 1: Successful Login and Balance Check
1. Username: john
2. Password: pass123
3. Choice: 1
4. **Expected Result:** Shows balance of $1000.00

### Test Case 2: Deposit Money
1. Login successfully
2. Choice: 2
3. Amount: $500
4. **Expected Result:** New balance $1500.00, transaction count increases

### Test Case 3: Invalid Deposit (Too Large)
1. Login successfully
2. Choice: 2
3. Amount: $15000
4. **Expected Result:** Error message about maximum deposit limit

### Test Case 4: Withdrawal with Minimum Balance Check
1. Login successfully
2. Choice: 3
3. Amount: $950
4. **Expected Result:** Error - cannot maintain minimum balance of $100

### Test Case 5: Transfer with Fee
1. Login successfully
2. Choice: 4
3. Recipient: Alice
4. Account: 123456
5. Amount: $100
6. **Expected Result:** Balance reduced by $101 ($100 transfer + $1 fee)

### Test Case 6: Failed Login
1. Username: wrong
2. Password: wrong
3. **Expected Result:** Error message, application ends

## Learning Objectives

By studying this application, students will learn:

1. **Real-world problem solving** using programming fundamentals
2. **Input validation** techniques
3. **Nested decision making** for complex logic
4. **State management** using variables
5. **User interaction** through input/output
6. **Business logic** implementation (fees, limits, validations)
7. **Error handling** with meaningful messages
8. **Code organization** and comments

## Extension Ideas for Future Lessons

Once students learn loops and functions, they can enhance this application with:

1. **Loops:** Allow multiple transactions without restarting
2. **Functions:** Break code into reusable pieces (check_balance, deposit, withdraw)
3. **Lists:** Store transaction history
4. **Dictionaries:** Manage multiple user accounts
5. **File I/O:** Save and load account data
6. **Exception Handling:** Better error management

## How to Run

1. Save the file as `bank_application.py`
2. Open terminal/command prompt
3. Navigate to the file location
4. Run: `python bank_application.py`
5. Follow the on-screen prompts



## Conclusion

This application demonstrates that even with basic programming concepts, we can build practical, real-world applications. It's a foundation that will be greatly enhanced as we learn more advanced concepts!
