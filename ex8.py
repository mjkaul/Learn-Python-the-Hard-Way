formatter = "{} {} {} {}"
# defines the variable as a set of empty placeholders for strings

print(formatter.format(1, 2, 3, 4))
# uses the .format function to define formatter 
print(formatter.format("one", "two", "three", "four"))
# same
print(formatter.format(True, False, False, True))
# same
print(formatter.format(formatter, formatter, formatter, formatter))
# same
print(formatter.format(
	"Glory be to God for dappled things", 
	"For skies of couple-colour as a brinded cow;",
	"For rose-moles all in stipple upon trout that swim;",
	"Fresh-firecoal chestnut-falls; finches' wings;"
))