from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth, fifth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
print("Your fifth variable is:", fifth)

favorite = input("Which of these is your favorite? ")

print(f"Yes, the greatest Victorian poet is {favorite}.")