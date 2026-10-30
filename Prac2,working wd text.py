'''name = " aMNA rAZA "
name = name.strip().title()
print(f"Welcome, {name}! Your name has {len(name)}characters")

prices = [850, 1200, 400]
print(prices[-1])'''

# Problem # 2


'''email = " Ali.Khan@GMAIL.com 
email = email.strip()
email = email.lower()
count = len(email)
print(f"Email: {email} ({count} characters)")'''

# Problem # 3

'''item = " wireless MOUSE "
price = 2499
quantity = 3

item = item.strip().title()
total = price * quantity

print(f"{item} x{quantity} = Rs {total:,}")'''

# Problem # 4


'''raw_code = " ord-2024-0042 "
order_code = raw_code.strip().replace("-", "").upper()

print(f"Order {order_code} has {len(order_code)} characters")'''

# Problem #5


first = " bilal "
last = "QURESHI "
city = "lahore"

first = first.strip().lower()
last = last.strip().lower()
city = city.strip().lower()

username = first + "." + last + "_" + city[0:3]

print(username)

