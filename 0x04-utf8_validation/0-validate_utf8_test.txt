#!/usr/bin/env fish
python3 -m doctest -v (basename (status -f))
exit
"""
>>> validUTF8 = __import__('0-validate_utf8').validUTF8
>>> print(validUTF8([65]))
True

>>> print(validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]))
True

>>> print(validUTF8([229, 65, 127, 256]))
False

"""
