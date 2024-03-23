'''
PROGRAMMER: Christopher D Colbert
USERNAME: ccolbert
PROGRAM: hw06_01.py

DESCRIPTION: Given a folder containing subfolders and files within those subfolders,
find 5 digit long numbers and sum total. Prints total files, total subfolders, total
number of 5 digit numbers, and sum of numbers.
'''
import re, pathlib
total = 0
subfolders = 0
files = 0
num_total = 0

regex = '\$([0-9]{5})\$'
p = pathlib.Path('data')

#for subfolders in main file
for folder in p.iterdir():
    subfolders += 1
    
    #for files in each subfolder
    for file in folder.iterdir():
        files +=1
        
        #open file
        with file.open() as f:
            #for each line find regex
            for line in f:
                numbers = re.findall(regex, line)
                
                #extract number from list returned from findall
                for number in numbers:
                    num_total += 1
                    total += int(number)

print(f"Number of subfolders: {subfolders}")
print(f"Number of files: {files}")
print(f"Number of 5 digit numbers: {num_total}")
print(f"Sum of numbers: {total}")