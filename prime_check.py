def is_prime(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
        if c > 2: return False
    return 2 == c

