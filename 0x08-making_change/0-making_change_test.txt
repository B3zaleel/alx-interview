#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> makeChange = __import__('0-making_change').makeChange
>>> test_cases = [
...     ([1, 2, 25], 37),
...     ([1256, 54, 48, 16, 102], 1453),
... ]
>>> for coins, total in test_cases:
...     print(makeChange(coins, total))
7
-1

"""
