from prime_check import is_prime
from functools import reduce

def primes_generator(n):
    for i in range(1, n+1):
        if is_prime(i):
            yield i
        else:
            continue


def factorization(n) -> list:
    if is_prime(n):
        raise Exception(f'The num {n} is prime.')
    g = primes_generator(n)
    p = next(g)
    primes = []
    while n != 1:
        if n % p == 0:
            n = n / p
            primes.append(p)
        else:
            p = next(g)
    return primes

