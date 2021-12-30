def cheese_and_crackers(cheese_count, boxes_of_crackers): # defines a function called "cheese_and_crackers" and gives it two variables: cheese_count and boxes_of_crackers:
	print(f"You have {cheese_count} cheese!") # Prints a line that includes the cheese_count variable, hence the 'f'
	print(f"You have {boxes_of_crackers} boxes of crackers!") # prints a line that includes the boxes_of_crackers variable, hence the 'f'
	print("Man, that's enough for a party!") # prints a regular line with no formatting
	print("Get a blanket.\n") # prints another regular line, with a line-break character escape that will make it easier to read the output
	
print("We can just give numbers directly to the function.") # prints a normal line
cheese_and_crackers(20, 30) # gives two inputs directly to the function

print("OR, we can use variables from our script:") # prints a line
amount_of_cheese = 10 # defines a new variable
amount_of_crackers = 50 # defines another new variable

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # gives the variables to the function, which then transmits the numbers

print("We can even do math inside, too:") # prints a line
cheese_and_crackers(10 + 20, 5 + 6) # uses math to give two inputs to the function

print("And we can combine the two, variables and math:") # prints a line
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # combines variables with math. uses the variables defined above in lines 11-12, then adds some numbers to them

# Now, try to get user input:

print("Now, YOU tell me how much cheese and crackers you have:")
print("How much cheese do you have? (Number only, please!)", end=' ')
user_cheese = input()
print("How many boxes of crackers do you have?", end=' ')
user_crackers = input()

# Now, convert the input to integers:

print(f"You have {user_cheese} cheese and {user_crackers} crackers!")



