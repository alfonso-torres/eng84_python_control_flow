# Control flow
A program's control flow is the order in which the program's code executes. The control flow of a Python program is regulated by conditionals statements, loops, and functions calls. Let's see how each of them works.

### Conditional statements: *if, else if - elif and else*
Conditional Statement in Python perform different computations or actions depending on whether a specific Boolean constraint evaluates to true or false. <br/>
Syntax:<br/>
````python
if expression
 Statement
elif expression 
 Statement
else
 Statement
````
Let's see an example:
- We check if the number is positive, equal to 0 or negative.<br/>
````python
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
````
When variable `num` is positive, `Positive number` is printed. <br/>
If `num` is equal to 0, `Zero` is printed. <br/>
If `num` is negative, `Negative number` is printed.

## Loops:
Loops help to iterate through the data.

### *For loops*
A `for` loop is used for iterating over a sequence.

- Let's `for` loop to iterate through out list:
```` python
shooping_list = ["bread", "eggs", "milk", "orange"]
for items in shooping_list:
    print(items)
````
- Let's iterate through letter in a word:
```` python
for letter in "fruits":
    print(letter)
````
- With the `break` statement we can stop the loop before it has looped through all the items:
```` python
for items in shooping_list:
    print(items)
    if items == "milk": # when the condition is true the loops ends
        # break is a key work
        break
        # at this point when milk is found in the items iterating through the shooping_list the loop will stop
````
- Let's create a dict of our food bill so we can iterate through it using a `for` loop: <br/>
```` python
food_bill = {
    1: {"name ": "James", "bill": "£1"},
    2: {"name ": "Bond", "bill": "£2"},
    3: {"name ": "Jose", "bill": "£3"}
}
````
Print the names and the bill amount for each person:
```` python
for key in food_bill:
    value = food_bill[key]
    print("Name: " + value["name "] + ", and the bill is: " + value["bill"])
}
````
- Nested loop: you can use one or more loop inside any another `for` loop:
```` python
for item in food_bill.values():
    # Nested loop to iterate through the nested dictionary to get the value of bill by name
    for Name_bill in item.values():
        print(Name_bill)
````
### *While loops*
The `while` loop in Python is used to iterate over a block of code as long as the condition is true. We generally use this loop when we do not know the number of times to iterate beforehand.
- Let's see an example of `while` loop:
```` python
num = 0
while num < 10: # while true continue, if false stop
    print(f"it's working -> {num}")
    num += 1
````
- With the `break` statement we can stop the loop even if the while condition is true:
```` python
num = 0
while num < 10: # while true continue, if false stop
    print(f"it's working -> {num}")
    if num == 4: # if True the loop ends.
        break
    num += 1
````
- Use cases:
```` python
ADD code
````
