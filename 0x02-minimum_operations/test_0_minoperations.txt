'''
Run the command below to execute these test cases.
python3 -m doctest -v test_0_minoperations.txt

Operations path format:
Character in file: H
operations: copy all (bit 1) or paste (bit 0),
    e.g.; copy all and paste -> 11
    e.g.; paste only -> 01

>>> minOperations = __import__('0-minoperations').minOperations
>>> minOperations(0)
0
>>> minOperations(-1)
0
>>> minOperations(1.4)
0
>>> minOperations('1')
0

# H
>>> minOperations(1)
0

# H-(11)->HH
>>> minOperations(2)
2

# H-(11)->HH-(11)->HHHH
# H-(11)->HH-(01)->HHH-(01)->HHHH
>>> minOperations(4)
4

# H-(11)->HH-(01)->HHH-(01)->HHHH-(01)->HHHHH
>>> minOperations(5)
5

# H-(11)->HH-(01)->HHH-(01)->HHHH-(01)->HHHHH-(01)->HHHHHH-(01)->HHHHHHH
>>> minOperations(7)
7

# H-(11)->HH-(01)->HHH-(01)->HHHH-(01)->HHHHH-(01)->HHHHHH-(01)->HHHHHHH-(01)->HHHHHHHH-(01)->HHHHHHHHH-(01)->HHHHHHHHHH-(01)->HHHHHHHHHHH
>>> minOperations(11)
11

# H-(11)->HH-(01)->HHH-(11)->HHHHHH-(01)->HHHHHHHHH
>>> minOperations(9)
6

# H-(11)->HH-(01)->HHH-(11)->HHHHHH-(11)->HHHHHHHHHHHH
>>> minOperations(12)
7

# H-(11)->HH-(01)->HHH-(11)->HHHHHH-(01)->HHHHHHHHH
>>> minOperations(15)
8

'''
