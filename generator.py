

r = range(0, 100, 2)

print(r[42])

#
def nn():
    current = 1
    while True:
        yield current
        current += 1
        
print('------------------------------------------')

for n in nn():
    print(n)
    if n >= 100:
        break;
    
print('------------------------------------------')
#exit()

def reverse(n):
    
    n = int(abs(n))
    
    rev = 0
    while n > 0:
        d = n % 10
        n //=10
        rev *= 10
        rev += d
        
    return rev

def is_numeric_palindrome(n):
    
    return n == reverse(n)

for n in range(0, 1000):
    if is_numeric_palindrome(n):
        print(n)
        
print('------------------------------------------')

p_lc = [n for n in range(0, 100) if is_numeric_palindrome(n)]
print(p_lc)
print(p_lc[14])
#print(p_lc[20])
print(list(p_lc))

print('------------------------------------------')

p_gc = (n for n in range(0, 100) if is_numeric_palindrome(n))
print(p_gc)
#print(p_gc[14])
#print(p_gc[20])
p_list_gc =  list(p_gc)
print(p_list_gc)
#print(p_list_gc[14])
#print(p_list_gc[20])

print('------------------------------------------')

p_gc_nn = (n for n in nn() if is_numeric_palindrome(n))
print(p_gc_nn)

for n in p_gc_nn:
    if n < 200:
        print(n, end= '  ')
    else:
        break;
    
for n in p_gc_nn:
    if n < 400:
        print(n, end= '  ')
    else:
        break;