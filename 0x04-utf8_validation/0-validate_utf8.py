#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    valid_flags = []

    def bin_len(c_byte):
        return len(bin(c_byte)[2:])
    for c in data:
        if type(c) != int or c < 0:
            return False
        if c >= 0x00 and c <= 0x7f:
            valid_flags = [bin_len(c) <= 7]
        if not all(valid_flags) or len(valid_flags) == 0:
            return False
    return True
