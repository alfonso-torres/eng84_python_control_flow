# Syntax to create a loop
# for is python keyword variable then data_collection

# shooping_list = ["bread", "eggs", "milk", "orange"]

# print(shooping_list)
# print(shooping_list[0])
# print(shooping_list[1])
# print(shooping_list[2])
# print(shooping_list[3])

# Let's for loop to iterate through out list

#for items in shooping_list:
#    print(items)

# Let's iterate through letter in a word
for letter in "fruits":
    print(letter)
# You can iterate in any type of data_collection

shooping_list = ["bread", "eggs", "milk", "orange"]

for items in shooping_list:
    print(items)
    if items == "milk": # when the condition is true the loops ends
        # break is a key work
        break
        # at this point when milk is found in the items iterating through the shooping_list the loop will stop

# Let's create a dict of our food bill so we can iterate through it using a for loop
food_bill = {
    1: {"name ": "James", "bill": "£1"},
    2: {"name ": "Bond", "bill": "£2"},
    3: {"name ": "Jose", "bill": "£3"}
}

# print(food_bill)
# Let's iterate through our dict
#for items in food_bill.values():
#    print(items)

# print the names and the bill amount for each person
for key in food_bill:
    value = food_bill[key]
    print("Name: " + value["name "] + ", and the bill is: " + value["bill"])

#for i in food_bill.values():
#    print("name", i["name "] + ",", "bill:", i["bill"])
