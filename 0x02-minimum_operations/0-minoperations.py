#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if n <= 0:
        return 0
    prime_factors = (1, 2, 3)
    build_ops_count = (2, 3, 4)
    prime_freq = [1, 0, 0]
    i = len(prime_factors) - 1
    rem = n
    ops_count = 0
    clipboard = 0
    while rem > 0:
        if rem % prime_factors[i] == 0:
            if rem == rem / prime_factors[i]:
                break
            prime_freq[i] += 1
            rem -= prime_factors[i]
            if clipboard > prime_factors[i]:
                return 0
            if clipboard == prime_factors[i]:
                ops_count += 1
                continue
            ops_count += build_ops_count[i]
            clipboard = prime_factors[i]
        elif i >= 0:
            i -= 1
        else:
            return 0
    return ops_count
