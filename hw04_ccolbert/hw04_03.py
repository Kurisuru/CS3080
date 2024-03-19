'''
PROGRAMMER: William L. Bahn
USERNAME: wbahn
PROGRAM: hw04_03.py

DESCRIPTION: Multithreaded RSA Factoring program
'''

import discrete_math as dm

rsa_list = []
with open("rsa_numbers.txt", "rt") as fp:
    strings = fp.readlines()

for s in strings:
    rsa_list.append(int(s))

dm.factor_list(rsa_list, 1200)

