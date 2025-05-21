#Create the Inventory
cafe_inventory = {
    "coffee bean bags": (30, 15),
    "sugar bags": (18, 5),
    "straws": (100, 20),
    "cups": (150, 25),
    "filters": (75, 10)
}

#Displaying the Inventory
print("Welcome to the Inventory Manager!")

print("Current inventory:")
for item, (quantity, price) in cafe_inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

#Adding an item
print("Adding a new item: hazlenut syrup")
cafe_inventory["hazlenut syrup"] = (5, 4)

#Removing an existing item
print("Removing an item: sugar bags")
del cafe_inventory["sugar bags"]

#Updating an exisiting item
print("Updating quantity of straws")
cafe_inventory["straws"] = (200, 40)

print("New inventory:")
for item,(quantity, price)in cafe_inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
total_value = 0
for item in cafe_inventory:
    quantity, price = cafe_inventory[item]
    total_value += quantity * price
print(f"Total value of inventory: ${total_value}")

