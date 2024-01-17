#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result in exactly n H
"""


def minOperations(n):
    if n <= 1:
        return 0

    def prime_factors(num):
        factors = []
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                factors.append(i)
                num //= i
        if num > 1:
            factors.append(num)
        return factors

    factors = prime_factors(n)
    return sum(factors)
