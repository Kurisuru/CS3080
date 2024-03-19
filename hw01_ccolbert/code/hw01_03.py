'''
PROGRAMMER:..Christopher Colbert
USERNAME:....ccolbert
PROGRAM:.....hw01_03.py

DESCRIPTION: Simulate the average seek time of a hard drive
'''
import random

print("DATA ENTRY")
tracks = int(input("Enter number of tracks:........"))
runs = int(input("Enter number of runs to make:.."))
total_distance = 0

#for amount of runs user inputs
for trials in range(runs):
    #pick random start and end track to determine number of tracks moved
    start_track = random.randint(0, tracks - 1)
    end_track = random.randint(0, tracks - 1)
    
    distance_moved = abs(end_track - start_track)
    total_distance += distance_moved
    
#calculate average distance moved between all runs
average_distance = float(total_distance / runs)

print("SIMULATION RESULTS")
print("Number of tracks:.... %-6d" %tracks)
print("Number of runs:...... %-6d" %runs)
print("Average distance:.... %-4.2f tracks" %average_distance)