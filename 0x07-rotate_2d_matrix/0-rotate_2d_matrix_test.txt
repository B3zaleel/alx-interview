#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix
>>> test_cases = [
...     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
...     [[1, 2, 3, 15], [4, 5, 6, 13]],
... ]
>>> for matrix in test_cases:
...     rotate_2d_matrix(matrix)
...     print(matrix)
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
[[4, 1], [5, 2], [6, 3], [13, 15]]

"""
