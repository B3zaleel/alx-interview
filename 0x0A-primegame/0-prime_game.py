#!/usr/bin/python3
"""Prime game module.
"""


def is_prime(num):
    num_sqrt = int(num ** 0.5 + 1)
    for i in range(2, num_sqrt):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if not nums or x < 1:
        return None
    players = ('Maria', 'Ben')
    winners = []
    nums_len = len(nums)
    for i in range(x):
        n = nums[i] if i < nums_len else 0
        n_nums = list(range(1, n + 1, 1))
        prime, turns = 2, 0
        while True:
            removal_ocurred = False
            for multiple in range(prime, n + 1, prime):
                if multiple in n_nums:
                    n_nums.remove(multiple)
                    removal_ocurred = True
            turns += 1
            if removal_ocurred:
                next_prime_chosen = False
                for val in n_nums:
                    if val > prime and is_prime(val):
                        prime = val
                        next_prime_chosen = True
                        break
                if not next_prime_chosen:
                    break
            else:
                break
        winners.append(players[turns % 2])
    marias_wins = winners.count(players[0])
    bens_wins = winners.count(players[1])
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
