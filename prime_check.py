def is_prime(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(n % i)
    return 2 == len(lst)


print(is_prime(2))
