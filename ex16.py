# imports the argument variable
from sys import argv

# defines the argument variable
script, filename = argv

# prints some text
print(f"We're going to erase {filename}.")
print("If you don't want this, hit CRTRL-C (^C).")
print("If you do want this, hit RETURN.")

# how does it know what to do with "RETURN"? CTRL-C just quits the program.
input("?")

print("Opening the file...")
# opens the file
target = open(filename, 'w')

# print("Truncating the file. Goodbye!")
# truncates the file
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# adds a line
target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")
# closes the file
target.close()

# Study drills 5: no, it's not needed