'''
PROGRAMMER:..Christopher Colbert
USERNAME:....ccolbert
PROGRAM:.....hw02_03.py

DESCRIPTION: Obtains file name (without extension) from user containing lines of:
machine_code		assembly_code
Then creates a file just the assembly code on each line. File output is echoed to the console
'''
import re

print("DATA ENTRY")
file_name = (input("Enter file name (Without extension): "))
fp = open(file_name + ".dis", "rt")
data = fp.read()
fp.close()

#takes expressions of any number of digits, any number of whitespace, and then captures any remaining
#characters on the line (excluding '\n')
regex = re.compile(r'\d+\s+(.*)')

results = regex.findall(data)

fp = open(file_name + ".asm", "wt")
for item in results:
    print(item)
    fp.write(item + "\n")
fp.close()