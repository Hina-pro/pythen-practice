# Problem # 1
'''prices = [850, 1200, 400]

print(prices[-1])
print(sum(prices))

product = {
    "name": "Wireless Mouse",
    "price": 2499,
    "in_stock": True
}
product["in_stock"] = False

print(product["name"])'''

# Problem # 2


'''sales = [18500, 22300, 19800, 25400, 31200, 42800, 38600]

weekly_total = sum(sales)
daily_average = weekly_total / len(sales)

best_sales = max(sales)
worst_sales = min(sales)

print(f"Monday's sales: Rs {sales[0]:,}")
print(f"Sunday's sales: Rs {sales[6]:,}")
print(f"Weekly total: Rs {weekly_total:,}")
print(f"Daily average: Rs {daily_average:,.0f}")
print(f"Best day's sales: Rs {best_sales:,}")
print(f"Worst day's sales: Rs {worst_sales:,}")'''

# Problem # 3


'''stock = {
    "pens": 120,
    "notebooks": 45,
    "staplers": 8
}

stock["notebooks"] -= 30

stock["markers"] = 60

print(len(stock))
print(stock)'''

# Problem # 4

'''orders = [
    {"id": "A101", "customer": "Ali", "total": 2000},
    {"id": "A102", "customer": "Sara", "total": 3500},
    {"id": "A103", "customer": "Ahmed", "total": 5000}
]

# 1. Print the second order's customer
print(orders[1]["customer"])

# 2. Give the third order a Rs 500 discount
orders[2]["total"] -= 500

# 3. Add a fourth order
orders.append({
    "id": "A104",
    "customer": "Hina",
    "total": 2500
})

# 4. Print the order count, first ID and last ID
print(
    f"{len(orders)} orders. "
    f"The first is {orders[0]['id']} "
    f"and the last is {orders[-1]['id']}."
)'''

# Problem # 4

'''orders = [
    {"id": "A101", "customer": "Ali", "total": 2000},
    {"id": "A102", "customer": "Sara", "total": 3500},
    {"id": "A103", "customer": "Ahmed", "total": 5000}
]
print(orders[1]["customer"])
print(orders[2]["total"])
orders.append({
    "id": "A104",
    "customer": "Hina",
    "total": 2500
})
print(
    f"{len(orders)} orders. "
    f"The first is {orders[0]['id']} "
    f"and the last is {orders[-1]['id']}."
)'''

# Problem # 5


customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "order_totals": [4500, 12800, 2300],
}

print(customer["address"]["city"])
print(len(customer["order_totals"]))
print(sum(customer["order_totals"]))
customer["order_totals"].append(6100)
print(sum(customer["order_totals"]))
print(customer.get("phone", "No phone number"))
