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
"""



cus_name = input("Enter Name : ")
cus_age = int(input("Enter Age : "))
no_tickets = int(input("Enter Number of Tickets : "))
day = input("Enter day of the week : ")

base_price = 15

discounted_price = 0

if cus_age < 12:
    discounted_price = base_price * 0.5
elif cus_age > 65:
    discounted_price = base_price * (1-0.3)
else:
    discounted_price = base_price


weekend_charges = 0;
if day=='saturday' or day=='sunday':
    weekend_charges = 3 * no_tickets;


total_charges = discounted_price * no_tickets;
total_charges += weekend_charges;

print("--- TICKETS----")
print(f"Customer Name : {cus_name}")
print(f"Customer Age : {cus_age}")
print(f"Number of Tickets : {no_tickets}")
print(f"Price per ticket : {discounted_price}")
print(f"Weekend Charges : {weekend_charges}")
print('-'*20)
print(f"Total Charges : {total_charges}")


    
