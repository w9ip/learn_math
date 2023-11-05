from prime_factorization import factorization


def gcd(nums):
    """Greatest common divisor"""
    if len(nums) < 2:
        return 'Please, enter two or more nums'

    facts = [factorization(n) for n in nums]
    # Осталось реализловать:
    # Общие множители которые находятся во всех последовательностях.
    # Произведение общих множителей и будет являться НОД.

gcd([36, 48])
