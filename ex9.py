# Here's some new strange stuff. Remember: type it exactly.
# a comment

days = "Mon Tue Wed Thu Fri Sat Sun"
# a variable defined as a string of days
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# another way to define a variable as a set of words. Clearly the \n separates the words in the series, just like a space did previously.

print("Here are the days: ", days)
# prints a list of the days, without line breaks. Just in order as presented in the variable definition.
print("Here are the months: ", months)
# prints a list of the months. the \n must add a line break between each.

print("""
There's something going on here. 
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# The triple-quotes clearly allow open-ended typing across multiple lines. It also respects linebreaks, and will add or remove them depending on whether or not they're present here.