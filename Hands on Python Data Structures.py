#Task 1 - Working with Lists
Original_Fav_Fruits = ["strawberry", "orange", "lychee", "mango", "watermelon"]
print("Original Favorite Fruits:", Original_Fav_Fruits)
New_Fruit = Original_Fav_Fruits.append("blueberries")
print("After adding a fruit:", Original_Fav_Fruits)
Minus_Fruit = Original_Fav_Fruits.remove("watermelon")
print("After removing a fruit:", Original_Fav_Fruits)
Reversed_list = Original_Fav_Fruits[::-1]
print(Reversed_list)

#Task 2 - Exploring Dictionaries
myself = {
    "name": "Maggie Kuo",
    "age": 21,
    "city": "Los Angeles"
}
#Add a new key - favorite color
myself["favorite color"] = "Green"
#Updating the city
myself["city"] = "New York"

#Making lists to collect the keys and values to be used in a loop
keys_list = []
values_list = []

for key, value in myself.items():
    keys_list.append(key)
    values_list.append(str(value))

print("Keys:", ", ".join(keys_list))
print("Values:", ", ".join(values_list))

#Task 3 - Using Tuples
favorite_things = ("Spider-Man: Into the Spider-Verse", "Nobody Compares To You", "Handmaid's Tale")
print("Favorite things:", favorite_things)
try:
    favorite_things[0] = "10 Things I Hate About you"
except TypeError:
    print("Oops! Tuples cannot be changed.")
print("Length of tuple:", len(favorite_things))