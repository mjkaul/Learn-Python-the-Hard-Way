types_of_people = 10
# sets variable to equal 10
x = f"There are {types_of_people} types of people."
# sets a variable equal to the string including the types_of_people variable

binary = "binary"
# defines another variable
do_not = "don't"
# and again
y = f"Those who know {binary} and those who {do_not}."
# sets the value of the y variable. 
# string inside a string 1 

print(x)
# prints the x variable, which is equivalent to a string
print(y)
# prints the y variable, which is equivalent to a string

print(f"I said: {x}")
# prints another string
# string inside a string 2
print(f"I also said: '{y}'")
# prints another string, this time within single quotes as it should be.
# string inside a string 3

hilarious = False
# defines a variable
joke_evaluation = "Isn't that joke so funny?! {}"
# defines another variable, with a placeholder for an undefined variable inside it.

print(joke_evaluation.format(hilarious))
# prints the string that includes both of these variables
# string inside a string 4

w = "This is the left side of . . . "
# another variable
e = "a string with a right side."
# another variable

print(w+e)
# you can add variables!