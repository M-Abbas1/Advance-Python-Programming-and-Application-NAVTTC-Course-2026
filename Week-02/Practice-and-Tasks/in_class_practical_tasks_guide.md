# PRACTICAL TASKS - STUDENT GUIDE

## Overview

This document provides guidance for completing the practical tasks.
These tasks integrate all concepts learned so far: print statements,
variables, data types, operators, and conditional statements.

---

## In-Class Tasks (With Instructor)

### Task 1: Simple Calculator
**Difficulty:** Easy
**Concepts:** Input, type conversion, if-elif-else, operators
**Time:** 15-20 minutes

### Task 2: Movie Ticket Booking
**Difficulty:** Medium
**Concepts:** Multiple inputs, nested conditions, logical operators
**Time:** 20-25 minutes

### Task 3: Student Grade Report
**Difficulty:** Medium
**Concepts:** Weighted calculations, nested if-elif-else, formatting
**Time:** 25-30 minutes

### Task 4: Electricity Bill Calculator
**Difficulty:** Hard
**Concepts:** Complex nested conditions, slab calculations
**Time:** 30-35 minutes

### Task 5: Restaurant Billing
**Difficulty:** Hard
**Concepts:** Multiple items, conditional item input, complex calculations
**Time:** 30-40 minutes

---

## Assessment Tasks (Independent Work)

### Task 1: Hotel Room Booking System
**Focus:** Nested conditionals, percentage calculations, discount logic
**Expected Code:** 18-22 lines
**Time Limit:** 60 minutes

### Task 2: Car Rental Service
**Focus:** Multiple condition checks, age-based logic, cumulative discounts
**Expected Code:** 18-22 lines
**Time Limit:** 60 minutes

### Task 3: Shopping Cart with Membership
**Focus:** Membership tiers, promotional offers, shipping calculations
**Expected Code:** 18-25 lines
**Time Limit:** 60 minutes

### Task 4: Exam Qualification System
**Focus:** Multiple criteria checking, weighted averages, status determination
**Expected Code:** 20-25 lines
**Time Limit:** 70 minutes

---

## Common Patterns to Remember

### Pattern 1: Getting and Validating Input
```python
# Get input
value = input("Enter value: ")

# Convert to appropriate type
value = int(value)  # or float(value)

# Validate
if value < 0:
    print("Error: Value must be positive")
else:
    # Process value
    pass
```

### Pattern 2: Category-Based Calculation
```python
# Determine category
if score >= 90:
    grade = "A"
    multiplier = 1.0
elif score >= 80:
    grade = "B"
    multiplier = 0.9
else:
    grade = "C"
    multiplier = 0.8

# Use category for calculation
final_value = base_value * multiplier
```

### Pattern 3: Accumulating Costs
```python
# Start with base
total = base_price

# Add items conditionally
if condition1:
    total = total + extra1

if condition2:
    total = total + extra2

# Apply percentage charges
tax = total * 0.10
total = total + tax
```

### Pattern 4: Discount Tiers
```python
# Check discount eligibility
if amount > 1000:
    discount = 0.20  # 20% off
elif amount > 500:
    discount = 0.15  # 15% off
elif amount > 200:
    discount = 0.10  # 10% off
else:
    discount = 0.0   # No discount

# Apply discount
discount_amount = amount * discount
final_amount = amount - discount_amount
```

### Pattern 5: Multiple Criteria Check
```python
# Check all criteria
criteria1_met = score >= 60
criteria2_met = attendance >= 75
criteria3_met = assignment_done

# Determine result
if criteria1_met and criteria2_met and criteria3_met:
    result = "Qualified"
else:
    result = "Not Qualified"
    # Show which failed
    if not criteria1_met:
        print("Score too low")
    if not criteria2_met:
        print("Attendance too low")
```

### Pattern 6: Slab-Based Calculation
```python
# Example: Electricity bill with slabs
if units <= 100:
    cost = units * 0.50
elif units <= 200:
    cost = (100 * 0.50) + ((units - 100) * 0.75)
elif units <= 300:
    cost = (100 * 0.50) + (100 * 0.75) + ((units - 200) * 1.20)
else:
    cost = (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)
```

---

## Tips for Success

### 1. Plan Before Coding
- Read the requirements carefully
- List all inputs needed
- List all calculations required
- Identify all conditions to check
- Plan the output format

### 2. Code Step by Step
```
Step 1: Get all inputs
Step 2: Convert types
Step 3: Perform basic calculations
Step 4: Apply conditions
Step 5: Calculate final values
Step 6: Display output
```

### 3. Test Thoroughly
Test with:
- Normal values (typical use case)
- Boundary values (minimums and maximums)
- Edge cases (zero, negative, very large)
- Different option combinations

### 4. Format Output Nicely
```python
# Use separators
print("=" * 40)
print("      TITLE")
print("=" * 40)

# Align currency values
print(f"Item:        ${amount:>10.2f}")
print(f"Tax:         ${tax:>10.2f}")

# Use consistent spacing
print("-" * 40)
```

### 5. Common Mistakes to Avoid
- Forgetting to convert input strings to numbers
- Using `=` instead of `==` in conditions
- Incorrect operator precedence
- Not handling division by zero
- Forgetting to validate negative values
- Poor indentation

---

## Testing Checklist

Before submitting, verify:

- [ ] All inputs are properly converted (int/float)
- [ ] All conditions work correctly
- [ ] Calculations are accurate
- [ ] Output is formatted nicely
- [ ] Currency shows 2 decimal places
- [ ] Edge cases are handled
- [ ] No syntax errors
- [ ] Variable names are meaningful
- [ ] Code is properly indented
- [ ] Tested with 3+ different inputs

---

## Sample Test Cases

### For Calculator Programs:
- Test Case 1: Normal values (10, 5, +)
- Test Case 2: Division by zero (10, 0, /)
- Test Case 3: Negative numbers (-5, -3, *)
- Test Case 4: Invalid operator (10, 5, @)

### For Billing Programs:
- Test Case 1: Minimum purchase
- Test Case 2: Purchase qualifying for discount
- Test Case 3: Purchase with all extras
- Test Case 4: Boundary value (just at discount threshold)

### For Qualification Programs:
- Test Case 1: All criteria met (excellent)
- Test Case 2: Barely qualified
- Test Case 3: One criterion failed
- Test Case 4: Multiple criteria failed

---

## Debugging Tips

### If you get wrong output:
1. Print intermediate values
   ```python
   print(f"Debug: subtotal = {subtotal}")
   ```
2. Check calculation order
3. Verify condition logic
4. Check if-elif-else structure

### If you get an error:
1. Read the error message carefully
2. Check the line number mentioned
3. Look for:
   - Missing colons (:)
   - Wrong indentation
   - Unclosed parentheses or quotes
   - Type mismatch (adding string to number)

### Common Error Messages:
- `NameError`: Variable not defined or misspelled
- `TypeError`: Wrong data type (e.g., string + int)
- `IndentationError`: Incorrect spacing
- `SyntaxError`: Missing colon, parenthesis, or quote
- `ValueError`: Cannot convert string to number

---

## Time Management

### For 60-minute tasks:
- Minutes 0-10: Understand requirements, plan approach
- Minutes 10-40: Write code
- Minutes 40-50: Test with different inputs
- Minutes 50-60: Fix bugs, format output, final check

### For 70-minute tasks:
- Minutes 0-10: Understand requirements, plan approach
- Minutes 10-50: Write code
- Minutes 50-60: Test with different inputs
- Minutes 60-70: Fix bugs, format output, final check

---

## Code Organization Template

```python
# ===============================================
# TASK: [Task Name]
# Student: [Your Name]
# ID: [Your ID]
# Date: [Date]
# ===============================================

# Display header
print("=" * 40)
print("      [PROGRAM TITLE]")
print("=" * 40)

# Section 1: Get all inputs
# [Your input code here]

# Section 2: Convert data types
# [Your conversion code here]

# Section 3: Perform calculations
# [Your calculation code here]

# Section 4: Apply conditions and discounts
# [Your conditional code here]

# Section 5: Display results
# [Your output code here]
```

---

## Resources

### Quick Reference:
- Print formatting: `f"{variable:.2f}"`
- User input: `input("Prompt: ")`
- Type conversion: `int()`, `float()`, `str()`
- Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical: `and`, `or`, `not`

### Getting Help:
1. Review course notebooks
2. Check in-class task solutions
3. Ask instructor during designated time
4. Review documentation provided

---

## Final Reminder

**The goal is not just to complete the task, but to:**
- Understand the logic
- Write clean code
- Handle edge cases
- Format output professionally
- Learn problem-solving skills

**Good luck with your tasks!** 🚀

---

## Submission Format

```
File Name: firstname_lastname_task1.py

First few lines of code:
# ===============================================
# Student Name: [Your Full Name]
# Student ID: [Your ID]
# Task: Assessment Task 1 - Hotel Booking System
# Date: [Submission Date]
# ===============================================
```

Remember: Quality over speed. A well-tested, properly formatted program
is better than a rushed one with errors!
