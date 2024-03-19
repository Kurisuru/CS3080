'''
PROGRAMMER:..Christopher Colbert
USERNAME:....ccolbert
PROGRAM:.....hw01_02.py

DESCRIPTION: Plots random points within a square region, and checks
if the points are inside of a circle centered in the square. The program
then estimates the value of pi, and calculates how far that value is from the
actual value.
'''
import random
import math

#recieve user input
print("DATA ENTRY")
runs = int(input("Enter how many runs to make: "))
successful_attempts=0

#for number of runs user inputs
for trial in range(runs):
    #generate a random point within the 2x2 square centered at the origin
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 <= 1:
        successful_attempts += 1
        
#estimate pi and find the percentage of difference between that and the real value of pi
pi = math.pi()
pi_estimate = float(4 * successful_attempts / runs)
percent_error = (abs(pi_estimate - pi) / pi) * 100

print("ESTIMATE OF PI")
print("Number of runs:..... %-10d" %runs)
print("Estimate of pi:..... %-2.8f" %pi_estimate)
print("Error:..............%%%1.8f" %percent_error)
