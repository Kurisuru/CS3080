'''
PROGRAMMER: Christopher D Colbert
USERNAME: ccolbert
PROGRAM: discrete_math.py

DESCRIPTION: Functions to factor prime numbers and display them in a comma seperated format
'''

import time
import threading

def pretty_int(n):
    return f'{n:,}'
    
    
def prime_factor(n):
    start = time.time()
    
    for i in range(2, int(n ** 0.5) + 1):
        if (time.time() - start) >= 1200:
            return (1, n)
        if n % i == 0:
            return (i, n // i)
    
    return (n, 1)
             
def factor_thread(number, result_list, lock):
    global time_expired
    factor = prime_factor(number)
    lock.acquire()
    try:
        result_list.append((number, factor))
    finally:
        lock.release()

def factor_list(rsa_list, time_limit):
    global time_expired
    threads = []
    results = []
    lock = threading.Lock()
    start_time = time.time()
    
    #create threads for each RSA number
    for number in rsa_list:
        thread = threading.Thread(target=factor_thread, args=(number, results, lock))
        threads.append(thread)
        thread.start()
    
    #factor numbers until time limit is reached
    while time.time() - start_time < time_limit:
        if threading.active_count() == 1:
            break
        time.sleep(0.1)
    
    time_expired = True
    
    for thread in threads:
        thread.join()
    
    print("Factoring a list of RSA numbers")
    print("List length:", len(rsa_list), "numbers")
    print("Time limit :", time_limit, "seconds")
    
    for number, factor in results:
        print("{} = ({}*{}) --- ( {:.3f} sec )".format(number, factor[0], factor[1], time.time() - start_time))
    
    success_count = sum(1 for _, factor in results if factor[0] != 1)
    print("\nSuccessfully factored {} numbers.".format(success_count))
    
    for thread in threads:
        if thread.is_alive():
            thread.join(timeout=0.1)
    
    print("Terminating", threading.active_count() - 1, "child threads.")
    print("Clean up complete, exiting program.")

if __name__ == "__main__":
    
    print("discrete_math.py : pretty_int() test")
    print()
    try:
        pretty_int
    except NameError:
        print("    Function pretty_int() not implemented")
        print()
    else:
        n_list = [0, 1, 999, 1000, 2**16, 2**64]
        for n in n_list:
            print("  ", n, "=", pretty_int(n))
    print()
    
    print("discrete_math.py : prime_factor() test")
    print()
    try:
        prime_factor
    except NameError:
        print("    Function pretty_factor() not implemented")
        print()
    else:
    
        for n in [0, 1, 2, 3, 12, 97]:
            start_time = time.time()
            result = prime_factor(n)
            end_time = time.time()
            print("    %s = (%s)*(%s) ( %.3f seconds)" \
                  % (pretty_int(n), pretty_int(result[0]),
                     pretty_int(result[1]), end_time - start_time))
        for n in [69_151*83_621, 1264447*3715967, 12957929*19528517, 320019647*57000000011, 61256847931289*612671]:
            start_time = time.time()
            result = prime_factor(n)
            end_time = time.time()
            print("    %s = (%s)*(%s) ( %.3f seconds)" \
                  % (pretty_int(n), pretty_int(result[0]),
                     pretty_int(result[1]), end_time - start_time))

    print("discrete_math.py : factor_list() test")
    print()
    try:
        factor_list
    except NameError:
        print("   Function factor_list() not implemented")
        print()
    else:
    
        rsa_p1 = [6186493,42598097,6186503,6186527,42598099,42597899,6186611,42597917,6186619,42597871]
        rsa_p2 = [42597871,42597889,42597899,42597911,42597917,42597923,6186527,42597979,42598097,42598099]
        rsa_list = []
        for p1, p2 in zip(rsa_p1, rsa_p2):
            rsa_list.append(p1 * p2)
        factor_list(rsa_list, 8)

    