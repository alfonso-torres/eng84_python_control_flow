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
- We check if the number is positive.<br/>
````python
if num > 0:
    print("Positive number")
````
- We check if the number is equal to 0. <br/>
````python
elif num == 0:
    print("Zero")
````
- Otherwise, the number is negative. <br/>
````python
else:
    print("Negative number")
````
When variable `num` is positive, `Positive number` is printed. <br/>
If `num` is equal to 0, `Zero` is printed. <br/>
If `num` is negative, `Negative number` is printed.
## For loops
## while loops
