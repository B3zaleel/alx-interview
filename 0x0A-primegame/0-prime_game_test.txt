#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> isWinner = __import__('0-prime_game').isWinner
>>> print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
Winner: Ben

>>> print("Winner: {}".format(isWinner(3, [4, 5, 1])))
Winner: Ben

>>> print("Winner: {}".format(isWinner(0, [4, 3])))
Winner: None

>>> print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
Winner: Ben

>>> print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
Winner: Maria

>>> print("Winner: {}".format(isWinner(4, [11, 30, 1, 7])))
Winner: Ben

>>> print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
Winner: Ben

>>> print("Winner: {}".format(isWinner(1, [1])))
Winner: Ben

>>> print("Winner: {}".format(isWinner(0, [0])))
Winner: None

>>> print("Winner: {}".format(isWinner(-1, [10])))
Winner: None

>>> nums = [0] * 100
>>> for i in range(100):
...     nums[i] = i * i
>>> print("Winner: {}".format(isWinner(100, nums)))
Winner: Ben

>>> nums = [0] * 10000
>>> for i in range(10000):
...     nums[i] = i
>>> print("Winner: {}".format(isWinner(10000, nums)))
Winner: Maria

"""
