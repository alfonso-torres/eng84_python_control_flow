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
A `for` loop is used for iterating over a sequence. We know the number of iterations beforehand.

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

### *While loops*
