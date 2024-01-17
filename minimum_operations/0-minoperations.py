#!/usr/bin/python3
"""
calculates the fewest number of operations needed 
to result in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage
if __name__ == "__main__":
    n1 = 4
    print("Min number of operations to reach {} char: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min number of operations to reach {} char: {}".format(n2, minOperations(n2)))
