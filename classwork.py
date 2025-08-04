'''
#Task 1

score = int(input("Enter the score of the student: "))

if score >= 70 and score <= 100:
    print("The grade is A")
elif score >= 50 and score <= 69.9:
    print("The grade is B")
elif score >= 40 and score <= 49.9:
    print("The grade is C")
elif score >= 30 and score <= 49.9:
    print("The grade is D")
elif score >= 0 and score <= 30:
    print("The grade is F")
else:
    print("This is an invalid range")

'''

'''
Task 2: Smart Restaurant Discount System

You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
1. Customers with a loyalty card get a 10% discount.
2. If the customer's order amount is above 20,000 NGN:
    - Loyalty card holders get an additional 5% discount.
    - Non-loyalty card holders get a free soft drink instead.
3. Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
1. Calculates the final discount or freebie for the customer.
2. Stores the result in a dictionary called `order_summary`.
3. Prints out a summary for the cashier.
'''

customer = {
"name": "Godiya",
"order_amount": 25000,
"loyalty_card": True,
"is_student": False,
}

order_summary = {}
discount_percentage = 0
freebie = None

if customer["loyalty_card"]:
    discount_percentage += 10
    if customer["order_amount"] > 20000:
        discount_percentage += 5
    else:
        freebie = "Free soft drink"

if customer["is_student"]:
    discount_percentage +=5


final_discount_amount = customer["order_amount"] * (discount_percentage / 100)
final_amount_after_discount = customer["order_amount"] - final_discount_amount

order_summary = {
"customer_name": customer["name"],
"original_amount": customer["order_amount"],
"discount_percentage": discount_percentage,
"final_discount_amount": final_discount_amount,
"final_amount_after_discount": final_amount_after_discount,
"freebie": freebie
}

print(f"Order Summary for {order_summary['customer_name']}")
print(f"Original Order Amount: {order_summary['original_amount']}")
print(f"Discount Applied: {order_summary['discount_percentage']}%")
print(f"Final Amount: {order_summary['final_amount_after_discount']:.2f}")
if order_summary["freebie"]:
    print(f"Freebie: {order_summary['freebie']}")





