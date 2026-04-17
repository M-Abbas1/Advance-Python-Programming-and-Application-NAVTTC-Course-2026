"""
TASK 1: SIMPLE CALCULATOR WITH VALIDATION
==========================================
Create a calculator that takes two numbers and an operator from the user,
then performs the calculation with proper validation.

Requirements:
- Take two numbers as input
- Take operator (+, -, *, /) as input
- Validate that the operator is valid
- Handle division by zero
- Display the result with proper formatting
- Show appropriate error messages
"""



print("A Simple Calculator")

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
op = input("Enter Operator : ")


if op == '+':
    print(f"{num1} {op} {num2} : {num1+num2}")
elif op == '-':
    print(f"{num1} {op} {num2} : {num1-num2}")
elif op == "*":
    print(f"{num1} {op} {num2} : {num1*num2}")
elif op == "/":
    if num2 == 0:
        print("This will cause an error and my program will crash")
    else:
        print(f"{num1} {op} {num2} : {num1/num2}")
else:
    print("Invalid Operator!")