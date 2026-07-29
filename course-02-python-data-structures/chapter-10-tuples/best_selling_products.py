# Best-Selling-Products


# Ask the user for the file name and open the file
name = input("Enter the file name: ")
if len(name) < 1:
    name = "sales.txt"

file_handle = open(name)

# Read through the file and build a dictionary of product sales
sales = dict()
for line in file_handle:
    product = line.strip()
    if product == "":
        continue

    sales[product] = sales.get(product, 0) + 1

products = list()
for product, quantity in sales.items():
    products.append((quantity, product))

products.sort(reverse=True)

# Print the products and their sales quantities in descending order
print("Sales report by product")
print("------------------------")

for quantity, product in products:
    print(f"{product}: {quantity} sold")