# Exercise 7: More Printing

print("Mary had a little lamb.")
# prints the string
print("Its fleece was white as {}.".format('snow'))
# prints the string, which includes a variable placeholder defined in the string as "snow"
print("And everywhere that Mary went ")
# prints the string
print(". " * 10) # what'd that do?
# prints the string . . . repeats it 10x

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# the "end=' '" variable seems to not only add a space, but also keeps the two strings (above and below) on the same line. This is unexpected. Why does it work this way?
print(end7 + end8 + end9 + end10 + end11 + end12)