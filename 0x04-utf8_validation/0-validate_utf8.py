#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See the Encoding section at <https://en.wikipedia.org/wiki/UTF-8>
    """
    if not isinstance(data, (list, tuple, set)):
        return False
    valid_flags = []
    for c in data:
        if type(c) != int:
            return False
        if c >= 0x00 and c <= 0x7f:
            valid_flags = [(c >> 7) & 0b1 == 0b0]
        if c >= 0x80 and c <= 0x7ff:
            valid_flags = [
                (c >> 6) & 0b10 == 0b10,
                (c >> 13) & 0b110 == 0b110
            ]
        if c >= 0x800 and c <= 0xffff:
            valid_flags = [
                (c >> 6) & 0b10 == 0b10,
                (c >> 14) & 0b10 == 0b10,
                (c >> 20) & 0b1110 == 0b1110
            ]
        if c >= 0x10000 and c <= 0x10FFFF:
            valid_flags = [
                (c >> 6) & 0b10 == 0b10,
                (c >> 14) & 0b10 == 0b10,
                (c >> 22) & 0b10 == 0b10,
                (c >> 27) & 0b11110 == 0b11110
            ]
        if not all(valid_flags) or len(valid_flags) == 0:
            return False
    return True
