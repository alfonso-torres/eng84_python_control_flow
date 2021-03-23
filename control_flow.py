# Control Flow
# if, else if/elif, else
# Conditional statements are used to control the flow of our program

age = 14
# if the user is above the age of 15 allow them to buy a ticket
if age >= 15: # If this condition is met/true the print statement will execute
    print("Thank you, please proceed to your purchase.")

# if the user is under 15 years of age do not allow to buy a ticket
elif age < 15:
    print("Sorry you are under age to watch this movie.")

# else block gets executed if non of the above conditions met
else:
    print("Oops something went wrong, please try later.")

print("--------------------------------------------------------------------------------")

# Exercise -
# As a user I would like to sell tickets according to the age of the user
# and category of the movie
# age = 12a, PG, U, 15 and 18
# user input to let us know the age to decide whether to sell the ticket or not
# casting implemented
# display the age back to the user with appropiate message

name = input("Please insert your name: ")
age = int(input("Please insert your age: "))

if age < 12:
    print("Hi " + name + ". Your age is " + str(age) + ", so you are in the category 12A. Those under 12 admitted, but only if accompanied by an adult(cinema only).")
    print("Advice is given regarding the content of the film and the adult must decide if it is appropriate for the accompanying under-12.")
    print("You are allowed to watch films with a 'U' certificate for everyone and 'PG' for anyone over the age of 8 years.")
elif age >= 12 and age < 15:
    print("Hi " + name + ". Your age is " + str(age) + ", so you are in the category 12. For the reason that you are in the range of 12 and 15 aged, you can watch the film unaccompanied.")
    print("A 12 rating is given to any film deemed to be suitable for those older than 12 years.")
    print("You are allowed to watch films with a 'U' and 'PG' certificates, but not with '15', '18' and 'R18' certificates.")
elif age >= 15 and age < 18:
    print("Hi " + name + ". Your age is " + str(age) + ", so you are in the category 15.")
    print("A 15 rated films are aimed at a 'more nature' audience, meaning specifically teenagers, and grown ups.")
    print("You are allowed to watch films with a 'U','PG' and '15' certificates, but not with '18' and 'R18' certificates.")
else:
    print("Hi " + name + ". Your age is " + str(age) + ", so you are in the category 18.")
    print("A 18 rated film is designed specifically for adults.")
    print("You are allowed to watch any film with any type of certificate, as long as you are 18 or older.")

print("--------------------------------------------------------------------------------")
# Ensure your git hub README documentation for todays lessons are up to date
