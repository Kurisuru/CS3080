'''
PROGRAMMER: Christopher Colbert
USERNAME: ccolbert
PROGRAM: hw03_01.py

DESCRIPTION: Mortgage Amortization Table
'''

import finance

# Get input from user:
print("DATA ENTRY")
loan_amount = float(input("Enter loan amount ($):...... "))
apr         = float(input("Enter loan APR (%):......... "))
term_years  =   int(input("Enter loan term (yr):....... "))
filename    =   str(input("Filename (w/o ext):......... "))

print()

# Generate full and abbreviated Amortization Schedules

with open(filename + ".txt", "wt") as fp:
    for s in finance.mortgage_amortization(loan_amount, apr, term_years):
        fp.write(s)
    
for s in finance.mortgage_amortization(loan_amount, apr, term_years, increment=12):
    print(s)


