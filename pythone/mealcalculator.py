print()
print()
price1 = float(input("What is the price of a child's meal? "))
price2 = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

subtotal = (price1 * children) + (price2 * adults)
total_tax = subtotal * (tax_rate / 100)
total_cost = subtotal + total_tax

print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total tax: ${total_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")
