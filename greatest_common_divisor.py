from prime_factorization import factorization
from collections import Counter

def gcd(nums):
    if len(nums) < 2:
        raise Exception('Need two or more nums')
    
    facts = [factorization(n) for n in nums]
    for i in facts:
        print(Counter(i))
    # Осталось реализловать:
    # Общие множители которые находятся во всех последовательностях.
    # Произведение общих множителей и будет являться НОД.

gcd([36, 48])