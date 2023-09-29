from prime_check import is_prime


def gcd(nums: list[int]) -> int:
    if len(nums) < 2:
        return 'Need two or more nums'
    
    all_divisors = []
    for num in nums:
        num_divisors = []
        i = 2
        while num != 1 and num % i == 0:
            print(num)
            num = num / i

print(gcd([26, 48]))