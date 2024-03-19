'''
PROGRAMMER: Christopher D Colbert
USERNAME: ccolbert
PROGRAM: pretty_number.py

DESCRIPTION: 
'''

def pretty_int(n, sep = ',', group = 3):
    num_str = str(n)
    #handle group size of 0, return original number as a string
    if group <= 0:
        return str(n)
    
    result = ''
    #step backwards through number by increment of -group
    for i in range(len(num_str), 0, -group):
        #if there are less numbers than group size, add numbers to beginning of string
        if i - group <= 0:
            result = num_str[:i] + result
        #otherwise, set 'result' string to seperator and remaining numbers in result
        else:
            result = sep + num_str[i - group:i] + result
    return result

def pretty_num(n, sep = ',', group = 3, places = 6, mark = '.'):
    #determine whether number is a float or not
    isFloat = False
    if '.' in str(n):
        isFloat = True
            
    #number is not a float
    if isFloat == False:
        #if number is positive
        if n >= 0:
            return pretty_int(n,sep, group)
        #if number is negative
        else:
            return '-' +  pretty_int(abs(n),sep, group)
    
    #number is a float
    else:
        n = round(n, places)
        num_float = pretty_num(int(str(n).split('.')[0]), sep, group) + mark + str(n).split('.')[1]
        return num_float


def pretty_sf(n, sigfigs = 3):
    str_num = ''
    #handle negative
    if n < 0:
        str_num += '-'
        n = abs(n)
    #handle 0
    if n == 0:
        return '0.' + '0' * (sigfigs)
    
    #remove leading 0s
    str_n = str(n).lstrip('0')
    
    #handle decimal values
    if '.' in str(n):
        length = len(str(n).split('.')[0]) + len(str(n).split('.')[1])
        str_num += str(round(n,sigfigs-1))
    #handle every other value
    else:
        length = len(str(n))
        if length < sigfigs:
            str_num += str(round(n,sigfigs))
            str_num += '.'
        else:
            str_num += str(round(n,sigfigs-length))
    while (length) < sigfigs:
        str_num += '0'
        length += 1
    
    return str_num

def pretty_si(n, si=False, sigfigs = 3):
    
    prefix_table = {30: "Q", 27: "R",
    24: "Y", 21: "Z", 18: "E",
    15: "P", 12: "T", 9: "G",
    6: "M", 3: "k", -3: "m",
    -6: "μ", -9: "n", -12: "p",
    -15: "f", -18: "a", -21: "z",
    -24: "y", -27: "r", -30: "q"
}
    
    power = 0
    str_num = ''
    
    if n < -1:
        str_num += '-'
        n = abs(n)
    
    if n == 0:
        return '0.' + '0' * (sigfigs - 1)
    
    if n >= 1:
        while n>=1000:
            n /= 1000
            power += 3
        while (power%3 != 0):
            n /= 10
            power += 1
    #handle decimals between -1 and 1
    else: 
        while n<1:
            n *= 1000
            power -= 3
        while (abs(power)%3 != 0):
            n *= 10
            power -= 1
        
    if power != 0:
        if power in range (-30,30):
            str_num += str(round(n, sigfigs - 1)) + prefix_table[power]
        else:
            str_num += str(round(n, sigfigs - 1)) + 'e' + str(power)
    else:
        str_num += str(round(n, sigfigs - 1))
    
    return str_num

def test_func():
    print('Pretty Int Test'.center(30, '-'))
    for n in (0, 1, 999, 1000, 2**16, 2**64):
        print(str(n) + " = " + pretty_int(n))
    for n in (1000, 2**16, 2**64):
        print(str(n) + " = " + pretty_int(n, sep = '-', group = 4))
    print('\n' + 'Pretty Num Test'.center(30, '-'))
    for n in (0, 999, 1000):
        print(str(n) + " = " + pretty_num(n))
    for n in (0, -1, -999, -1000, -(2**16), -(2**64)):
        print(str(n) + " = " + pretty_num(n))
    for n in (0.1234, 1000.0, (2**16)+(2**-4), -(2**16)+(2**-4)):
        print(str(n) + " = " + pretty_num(n, sep = ',', places = 3))
    print('\n' + 'Pretty SF Test'.center(30, '-'))
    for n in (0, 3.14159276535, 1, 999, 1000, 2**16, 2**64):
        print(str(n) + " = " + pretty_sf(n,5))
    print('\n' + 'Pretty SI Test'.center(30, '-'))
    for n in (0, 2**-5, 1, 999, 1000, 2**16, -(2**16), 2**64, 2**128):
        print(str(n) + ' = ' + pretty_si(n))
test_func()