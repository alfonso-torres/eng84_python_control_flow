# Syntax to create a loop
# for is python keyword variable then data_collection

print("--------------------------------FOR--------------------------------")
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
#for letter in "fruits":
#    print(letter)
# You can iterate in any type of data_collection

#shooping_list = ["bread", "eggs", "milk", "orange"]

#for items in shooping_list:
#    print(items)
#    if items == "milk": # when the condition is true the loops ends
        # break is a key work
#        break
        # at this point when milk is found in the items iterating through the shooping_list the loop will stop

# Let's create a dict of our food bill so we can iterate through it using a for loop
food_bill = {
    1: {"name ": "James", "bill": "£1"},
    2: {"name ": "Bond", "bill": "£2"},
    3: {"name ": "Jose", "bill": "£3"}
}

# Standard form for iterating through a dictionary
# for key, value in food_bill.items():
#   print(key, value)

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

for item in food_bill.values():
    # Nested loop to iterate through the nested dictionary to get the value of bill by name
    for Name_bill in item.values():
        print(Name_bill)
print("--------------------------------FOR--------------------------------")

print("--------------------------------WHILE--------------------------------")
# Syntax while - condition - value:
#num = 0
#while num < 10: # while true continue, if false stop
#    print(f"it's working -> {num}")
#    num += 1

# Second iterations
#num = 0
#while num < 10: # while true continue, if false stop
#    print(f"it's working -> {num}")
#    if num == 4: # if True the loop ends.
#        break
#    num += 1

# Use case as the 3rd Iteration

# age = input("please enter your age?")
# print(f"your age is {age} ")

user_prompt = True
while user_prompt:
    age = input(" Please enter your age: ")
    if age.isdigit(): # isdigit() is ensures to the user input is in digits
        user_prompt = False
    else:
        print("Please enter your age in Digits ")
# This line of code only gets executed if the user enters age in digits
print(f" Your age is {age}")

# Ensure the loop conditions are in your control to avoid going into the infinite loop
print("--------------------------------WHILE--------------------------------")
