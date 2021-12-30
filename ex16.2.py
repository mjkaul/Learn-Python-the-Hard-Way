from sys import argv

script = argv

print("Type filename again:")
filename = input("> ") 

txt = open(filename)
print(f"Here's your file, {filename}:")
print(txt.read())

txt.close()