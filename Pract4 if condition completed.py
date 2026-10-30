
'''total = 6200
city = "Lahore"
if total >= 5000 and city = "Lahore":
print("free delivery")
else: 
    print("Delivery charge: Rs 350")'''

# Problem # 1
total = 6200
city = "Lahore"

if total >= 5000 and city == "Lahore":
    print("Free delivery")
else:
    print("Delivery charge: Rs 350")'''

# Problem # 2


'''test_marks = [80, 79, 50, 49]

for marks in test_marks:
    if marks >= 80:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Marks: {marks}, Grade: {grade}")

# Problem # 3

'''stock = 12
quantity = 5

if quantity <= 0:
    print("Invalid quantity")

elif quantity > stock:
    print(f"Only {stock} left in stock")

else:
    remaining = stock - quantity
    print(f"Confirmed. {remaining} left after this order")'''

# Problem # 4


'''test_orders = [
    {"weight_kg": 5, "order_total": 6200, "city": " karachi "},
    {"weight_kg": 6, "order_total": 6200, "city": "Lahore"},
    {"weight_kg": 5, "order_total": 6200, "city": "Peshawar"},
    {"weight_kg": 6, "order_total": 6200, "city": "Peshawar"},
    {"weight_kg": 8, "order_total": 12000, "city": "Quetta"},
]

for order in test_orders:
    weight_kg = order["weight_kg"]
    order_total = order["order_total"]
    city = order["city"].strip().title()

    if order_total > 10000:
        shipping = 0
    elif city in ["Karachi", "Lahore", "Islamabad"]:
        if weight_kg <= 5:
            shipping = 200
        else:
            shipping = 400
    else:
        if weight_kg <= 5:
            shipping = 350
        else:
            shipping = 700

    print(f"Shipping to {city}: Rs {shipping}")'''


# Problem # 5


tickets = [
    {
        "plan": "enterprise",
        "hours_open": 6,
        "message": "Login is broken",
        "expected": "Urgent"
    },
    {
        "plan": "free",
        "hours_open": 1,
        "message": "I want a REFUND",
        "expected": "High"
    },
    {
        "plan": "pro",
        "hours_open": 30,
        "message": "Dashboard is slow",
        "expected": "High"
    },
    {
        "plan": "enterprise",
        "hours_open": 2,
        "message": "Question about invoices",
        "expected": "Normal"
    },
    {
        "plan": "enterprise",
        "hours_open": 6,
        "message": "I want a refund",
        "expected": "Urgent"
    }
]

for ticket in tickets:
    plan = ticket["plan"]
    hours_open = ticket["hours_open"]
    message_lower = ticket["message"].lower()

    # Check Urgent first so it overrides High for eligible enterprise tickets.
    if plan == "enterprise" and hours_open > 4:
        priority = "Urgent"
    elif "refund" in message_lower or "charged twice" in message_lower:
        priority = "High"
    elif plan == "pro" and hours_open > 24:
        priority = "High"
    else:
        priority = "Normal"

    print(
        f"Plan: {plan}, Priority: {priority}, "
        f"Expected: {ticket['expected']}, "
        f"Pass: {priority == ticket['expected']}"
    )
