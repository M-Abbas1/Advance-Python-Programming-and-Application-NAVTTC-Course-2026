# ===============================================
# PRACTICAL TASKS - IN-CLASS PRACTICE
# ===============================================
# These tasks should be completed during class
# with instructor guidance
# Each task is 15-20 lines of code
# ===============================================

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

Expected Output Example:
========================
--- Simple Calculator ---
Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +
------------------------
10.0 + 5.0 = 15.0
========================
"""

# SOLUTION - TASK 1
print("--- Simple Calculator ---")

# Get inputs
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")

# Convert to float
num1 = float(num1)
num2 = float(num2)

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
    print("-" * 24)
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print("-" * 24)
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print("-" * 24)
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("-" * 24)
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print("-" * 24)
        print(f"{num1} / {num2} = {result:.2f}")
else:
    print("-" * 24)
    print("Error: Invalid operator!")

print("=" * 24)


print("\n" * 3)


"""
TASK 2: MOVIE TICKET BOOKING SYSTEM
====================================
Create a ticket booking system that calculates the total cost based on
age, day of week, and number of tickets.

Requirements:
- Take customer name, age, number of tickets, and day as input
- Base ticket price: $15
- Child (under 12): 50% discount
- Senior (65+): 30% discount
- Weekend (Saturday/Sunday): $3 extra per ticket
- Show itemized bill with all calculations

Expected Output Example:
========================
--- Movie Ticket Booking ---
Enter your name: John
Enter your age: 25
Enter number of tickets: 2
Enter day (e.g., Monday, Saturday): Saturday

--- TICKET RECEIPT ---
Customer: JOHN
Age Category: Adult
Number of Tickets: 2
Base Price: $15.00 per ticket
Weekend Surcharge: $3.00 per ticket
------------------------
Subtotal: $36.00
Total Amount: $36.00
========================
"""

# SOLUTION - TASK 2
print("--- Movie Ticket Booking ---")

# Get customer information
name = input("Enter your name: ")
age = input("Enter your age: ")
tickets = input("Enter number of tickets: ")
day = input("Enter day (e.g., Monday, Saturday): ")

# Convert to appropriate types
age = int(age)
tickets = int(tickets)

# Base price
base_price = 15.00
discount = 0.0
weekend_surcharge = 0.0

# Determine age category and discount
if age < 12:
    age_category = "Child"
    discount = 0.50  # 50% discount
elif age >= 65:
    age_category = "Senior"
    discount = 0.30  # 30% discount
else:
    age_category = "Adult"
    discount = 0.0

# Check if weekend
if day.lower() == "saturday" or day.lower() == "sunday":
    weekend_surcharge = 3.00
    day_type = "Weekend"
else:
    day_type = "Weekday"

# Calculate costs
ticket_price = base_price * (1 - discount)
per_ticket_cost = ticket_price + weekend_surcharge
subtotal = per_ticket_cost * tickets

# Display receipt
print()
print("--- TICKET RECEIPT ---")
print(f"Customer: {name.upper()}")
print(f"Age Category: {age_category}")
print(f"Day Type: {day_type}")
print(f"Number of Tickets: {tickets}")
print(f"Base Price: ${base_price:.2f} per ticket")
if discount > 0:
    print(f"Discount: {discount * 100:.0f}%")
    print(f"Discounted Price: ${ticket_price:.2f} per ticket")
if weekend_surcharge > 0:
    print(f"Weekend Surcharge: ${weekend_surcharge:.2f} per ticket")
print("-" * 24)
print(f"Total Amount: ${subtotal:.2f}")
print("=" * 24)


print("\n" * 3)


"""
TASK 3: STUDENT GRADE REPORT GENERATOR
=======================================
Create a program that calculates a student's grade based on multiple
components and provides detailed feedback.

Requirements:
- Take student name, midterm score, final score, and assignment score
- Calculate total percentage (Midterm: 30%, Final: 40%, Assignments: 30%)
- Determine letter grade and GPA
- Check if student qualifies for Dean's List (GPA >= 3.5 and all scores >= 80)
- Provide detailed feedback

Expected Output Example:
========================
--- Student Grade Calculator ---
Student Name: Alice Smith
Midterm Score (out of 100): 85
Final Exam Score (out of 100): 90
Assignment Score (out of 100): 88

========== GRADE REPORT ==========
Student: ALICE SMITH
-----------------------------------
Score Breakdown:
  Midterm (30%):     85 → 25.50
  Final (40%):       90 → 36.00
  Assignments (30%): 88 → 26.40
-----------------------------------
Total Percentage: 87.90%
Letter Grade: B+
GPA: 3.3
Status: PASS
Dean's List: No
-----------------------------------
Performance: Excellent work! Keep it up!
===================================
"""

# SOLUTION - TASK 3
print("--- Student Grade Calculator ---")

# Get student information
name = input("Student Name: ")
midterm = input("Midterm Score (out of 100): ")
final = input("Final Exam Score (out of 100): ")
assignment = input("Assignment Score (out of 100): ")

# Convert to float
midterm = float(midterm)
final = float(final)
assignment = float(assignment)

# Calculate weighted scores
midterm_weight = midterm * 0.30
final_weight = final * 0.40
assignment_weight = assignment * 0.30

# Calculate total percentage
total_percentage = midterm_weight + final_weight + assignment_weight

# Determine letter grade and GPA
if total_percentage >= 90:
    letter_grade = "A"
    gpa = 4.0
elif total_percentage >= 85:
    letter_grade = "A-"
    gpa = 3.7
elif total_percentage >= 80:
    letter_grade = "B+"
    gpa = 3.3
elif total_percentage >= 75:
    letter_grade = "B"
    gpa = 3.0
elif total_percentage >= 70:
    letter_grade = "B-"
    gpa = 2.7
elif total_percentage >= 65:
    letter_grade = "C+"
    gpa = 2.3
elif total_percentage >= 60:
    letter_grade = "C"
    gpa = 2.0
else:
    letter_grade = "F"
    gpa = 0.0

# Determine pass/fail
if total_percentage >= 60:
    status = "PASS"
else:
    status = "FAIL"

# Check Dean's List eligibility
if gpa >= 3.5 and midterm >= 80 and final >= 80 and assignment >= 80:
    deans_list = "Yes"
else:
    deans_list = "No"

# Performance feedback
if total_percentage >= 90:
    feedback = "Outstanding performance! Excellent work!"
elif total_percentage >= 80:
    feedback = "Excellent work! Keep it up!"
elif total_percentage >= 70:
    feedback = "Good job! There's room for improvement."
elif total_percentage >= 60:
    feedback = "You passed, but consider studying more."
else:
    feedback = "Need to work harder. Seek help if needed."

# Display report
print()
print("=" * 35)
print("       GRADE REPORT")
print("=" * 35)
print(f"Student: {name.upper()}")
print("-" * 35)
print("Score Breakdown:")
print(f"  Midterm (30%):     {midterm:.0f} → {midterm_weight:.2f}")
print(f"  Final (40%):       {final:.0f} → {final_weight:.2f}")
print(f"  Assignments (30%): {assignment:.0f} → {assignment_weight:.2f}")
print("-" * 35)
print(f"Total Percentage: {total_percentage:.2f}%")
print(f"Letter Grade: {letter_grade}")
print(f"GPA: {gpa}")
print(f"Status: {status}")
print(f"Dean's List: {deans_list}")
print("-" * 35)
print(f"Feedback: {feedback}")
print("=" * 35)


print("\n" * 3)


"""
TASK 4: ELECTRICITY BILL CALCULATOR
====================================
Create a program that calculates electricity bill based on units consumed
with slab rates and additional charges.

Requirements:
- Take customer name, account number, and units consumed
- Calculate bill using slab rates:
  * First 100 units: $0.50 per unit
  * Next 100 units (101-200): $0.75 per unit
  * Next 100 units (201-300): $1.20 per unit
  * Above 300: $1.50 per unit
- Add fixed charge: $5.00
- Add service tax: 10% of total
- Show detailed breakdown

Expected Output Example:
========================
--- Electricity Bill Calculator ---
Customer Name: John Doe
Account Number: ACC123
Units Consumed: 250

============ ELECTRICITY BILL ============
Customer: JOHN DOE
Account Number: ACC123
Billing Period: Current Month
-----------------------------------------
Units Breakdown:
  First 100 units    @ $0.50 = $50.00
  Next 100 units     @ $0.75 = $75.00
  Next 50 units      @ $1.20 = $60.00
-----------------------------------------
Energy Charges:              $185.00
Fixed Charges:               $5.00
Subtotal:                    $190.00
Service Tax (10%):           $19.00
-----------------------------------------
TOTAL AMOUNT DUE:            $209.00
==========================================
"""

# SOLUTION - TASK 4
print("--- Electricity Bill Calculator ---")

# Get customer information
name = input("Customer Name: ")
account = input("Account Number: ")
units = input("Units Consumed: ")

# Convert to int
units = int(units)

# Fixed charges
fixed_charge = 5.00
tax_rate = 0.10

# Calculate bill based on slabs
if units <= 100:
    # All units in first slab
    slab1_units = units
    slab2_units = 0
    slab3_units = 0
    slab4_units = 0
    
    slab1_cost = slab1_units * 0.50
    slab2_cost = 0
    slab3_cost = 0
    slab4_cost = 0
elif units <= 200:
    # Units in first and second slab
    slab1_units = 100
    slab2_units = units - 100
    slab3_units = 0
    slab4_units = 0
    
    slab1_cost = slab1_units * 0.50
    slab2_cost = slab2_units * 0.75
    slab3_cost = 0
    slab4_cost = 0
elif units <= 300:
    # Units in first, second, and third slab
    slab1_units = 100
    slab2_units = 100
    slab3_units = units - 200
    slab4_units = 0
    
    slab1_cost = slab1_units * 0.50
    slab2_cost = slab2_units * 0.75
    slab3_cost = slab3_units * 1.20
    slab4_cost = 0
else:
    # Units in all slabs
    slab1_units = 100
    slab2_units = 100
    slab3_units = 100
    slab4_units = units - 300
    
    slab1_cost = slab1_units * 0.50
    slab2_cost = slab2_units * 0.75
    slab3_cost = slab3_units * 1.20
    slab4_cost = slab4_units * 1.50

# Calculate totals
energy_charges = slab1_cost + slab2_cost + slab3_cost + slab4_cost
subtotal = energy_charges + fixed_charge
tax_amount = subtotal * tax_rate
total_amount = subtotal + tax_amount

# Display bill
print()
print("=" * 42)
print("         ELECTRICITY BILL")
print("=" * 42)
print(f"Customer: {name.upper()}")
print(f"Account Number: {account}")
print(f"Total Units Consumed: {units}")
print("-" * 42)
print("Units Breakdown:")
if slab1_units > 0:
    print(f"  First {slab1_units} units    @ $0.50 = ${slab1_cost:.2f}")
if slab2_units > 0:
    print(f"  Next {slab2_units} units     @ $0.75 = ${slab2_cost:.2f}")
if slab3_units > 0:
    print(f"  Next {slab3_units} units     @ $1.20 = ${slab3_cost:.2f}")
if slab4_units > 0:
    print(f"  Next {slab4_units} units     @ $1.50 = ${slab4_cost:.2f}")
print("-" * 42)
print(f"Energy Charges:              ${energy_charges:.2f}")
print(f"Fixed Charges:               ${fixed_charge:.2f}")
print(f"Subtotal:                    ${subtotal:.2f}")
print(f"Service Tax (10%):           ${tax_amount:.2f}")
print("-" * 42)
print(f"TOTAL AMOUNT DUE:            ${total_amount:.2f}")
print("=" * 42)


print("\n" * 3)


"""
TASK 5: RESTAURANT BILLING SYSTEM
==================================
Create a billing system for a restaurant that calculates the total bill
with items, quantities, discounts, and tips.

Requirements:
- Take customer name and number of items (1-3 items for simplicity)
- For each item: name, quantity, and price
- Calculate subtotal
- Apply discount based on subtotal (>$50: 10%, >$100: 15%)
- Add service charge: 5% of subtotal
- Calculate tax: 8% of (subtotal + service charge - discount)
- Ask if customer wants to add tip (10%, 15%, 20%, or custom)
- Show detailed itemized bill

Expected Output Example:
========================
--- Restaurant Billing System ---
Customer Name: Alice
How many items (1-3)?: 2

Item 1 Name: Burger
Quantity: 2
Price per item: 12.50

Item 2 Name: Fries
Quantity: 1
Price per item: 5.00

Would you like to add a tip? (yes/no): yes
Tip percentage (10/15/20): 15

=========== RESTAURANT BILL ===========
Customer: ALICE
---------------------------------------
Items Ordered:
  Burger              x2   $25.00
  Fries               x1   $5.00
---------------------------------------
Subtotal:                  $30.00
Service Charge (5%):       $1.50
Discount (0%):             $0.00
Tax (8%):                  $2.52
Tip (15%):                 $5.13
---------------------------------------
TOTAL AMOUNT:              $39.15
=======================================
"""

# SOLUTION - TASK 5
print("--- Restaurant Billing System ---")

# Get customer information
customer = input("Customer Name: ")
item_count = input("How many items (1-3)?: ")
item_count = int(item_count)

# Initialize totals
subtotal = 0.0

# Get item details based on count
if item_count >= 1:
    print()
    item1_name = input("Item 1 Name: ")
    item1_qty = int(input("Quantity: "))
    item1_price = float(input("Price per item: "))
    item1_total = item1_qty * item1_price
    subtotal = subtotal + item1_total

if item_count >= 2:
    print()
    item2_name = input("Item 2 Name: ")
    item2_qty = int(input("Quantity: "))
    item2_price = float(input("Price per item: "))
    item2_total = item2_qty * item2_price
    subtotal = subtotal + item2_total

if item_count >= 3:
    print()
    item3_name = input("Item 3 Name: ")
    item3_qty = int(input("Quantity: "))
    item3_price = float(input("Price per item: "))
    item3_total = item3_qty * item3_price
    subtotal = subtotal + item3_total

# Service charge
service_charge = subtotal * 0.05

# Calculate discount based on subtotal
if subtotal > 100:
    discount_rate = 0.15
elif subtotal > 50:
    discount_rate = 0.10
else:
    discount_rate = 0.0

discount_amount = subtotal * discount_rate

# Calculate tax
taxable_amount = subtotal + service_charge - discount_amount
tax_amount = taxable_amount * 0.08

# Ask for tip
print()
tip_choice = input("Would you like to add a tip? (yes/no): ")

if tip_choice.lower() == "yes":
    tip_percentage = input("Tip percentage (10/15/20): ")
    tip_rate = int(tip_percentage) / 100
    tip_amount = taxable_amount * tip_rate
else:
    tip_rate = 0
    tip_amount = 0

# Calculate total
total_amount = subtotal + service_charge - discount_amount + tax_amount + tip_amount

# Display bill
print()
print("=" * 39)
print("        RESTAURANT BILL")
print("=" * 39)
print(f"Customer: {customer.upper()}")
print("-" * 39)
print("Items Ordered:")
if item_count >= 1:
    print(f"  {item1_name:<18} x{item1_qty}   ${item1_total:.2f}")
if item_count >= 2:
    print(f"  {item2_name:<18} x{item2_qty}   ${item2_total:.2f}")
if item_count >= 3:
    print(f"  {item3_name:<18} x{item3_qty}   ${item3_total:.2f}")
print("-" * 39)
print(f"Subtotal:                  ${subtotal:.2f}")
print(f"Service Charge (5%):       ${service_charge:.2f}")
print(f"Discount ({discount_rate*100:.0f}%):             ${discount_amount:.2f}")
print(f"Tax (8%):                  ${tax_amount:.2f}")
print(f"Tip ({tip_rate*100:.0f}%):                 ${tip_amount:.2f}")
print("-" * 39)
print(f"TOTAL AMOUNT:              ${total_amount:.2f}")
print("=" * 39)
