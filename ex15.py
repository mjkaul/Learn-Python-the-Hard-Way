from sys import argv

script = argv
# Lines 1-3 use argv to get the script name and a filename.

print("Type filename again:") # prints the command for user input
filename = input("> ") # provides a prompt; defines a variable to store the input value.


txt = open(filename) # new command, open, opens the file listed initially. defines the variable txt as equal to opening the file.
print(f"Here's your file, {filename}:") # returns the filename
print(txt.read()) # uses the txt variable to open, read, then print out the file.

print("Type the filename again:") # prints the command for user input
file_again = input("> ") # provides a prompt; defines a variable to store the input value.

txt_again = open(file_again) # same as line 5

print(txt_again.read()) # same as line 7

txt.close()
txt_again.close()

# Study Drills
# 5. The more often you have to enter the filename, the more likely to introduce human error. Better to import it once, whether through argv or input, and reuse it. To use argv, however, you have to know what to do before starting the script, so overall input is better—you can explain to the user what's required.
# 6. tried but can't figure it out
# 7. see above
