from math import log,e
from random import randint

'''
Numbers: 9998
Prime numbers: 1254

Prime test with pseudo prime test:

Prime numbers (5 iterations): 1231
Prime numbers (10 iterations): 1229
Prime numbers (50 iterations): 1229
Prime numbers (100 iterations): 1229

'''
def pseudo(a,n):
    '''
    check if number n is pseudo prime behind the base a
    :param a: base
    :param n: number
    :return: true if a^(n-1) = 1 (mod n) else false
    '''

    # initialize m and res. we can just consider numbers by module n
    m = a%n
    res = m

    # erect to power of n-1 step by step. power of 1 is already inited, so there is left just n-2 operations
    for i in range(n-2):
        res = res * m % n

    if res == 1:
        return True
    return False

def if_prime(n,s):
    for j in range(s):
        a = randint(1,n-1)

        if not pseudo(a,n):
            return False
    return True

def straight_check_prime(n):
    i = 2
    sqrt = n**0.5
    while i<sqrt:
        if n % i == 0:
            return False
        i+=1
    return True

if __name__ == '__main__':
    numbers = 0

    primes  = 0

    primes_5 = 0
    primes_10 = 0
    primes_50 = 0
    primes_100 = 0

    for i in range(2, 10000):
        numbers+=1
        if straight_check_prime(i):
            primes+=1
        if if_prime(i,5):
            primes_5 += 1
        if if_prime(i,10):
            primes_10 += 1
        if if_prime(i,50):
            primes_50 += 1
        if if_prime(i,100):
            primes_100 += 1

    print('Numbers:',numbers)
    print('Prime numbers:',primes)

    print('\nPrime test with pseudo prime test:\n')
    print('Prime numbers (5 iterations):',primes_5)
    print('Prime numbers (10 iterations):',primes_10)
    print('Prime numbers (50 iterations):',primes_50)
    print('Prime numbers (100 iterations):',primes_100)
