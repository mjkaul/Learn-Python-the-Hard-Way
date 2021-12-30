from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# We could do these two lines on one line. How?
indata = open(from_file, 'r')
# indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long.")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready? Hit RETURN to continue or CTRL-C to abort.")
# input()

out_file = open(to_file, 'w')
# out_file.write(indata)
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()