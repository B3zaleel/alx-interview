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
        if type(c) != int:
            return False
        if c >= 0x00 and c <= 0x7f:
            valid_flags = [bin_len(c) <= 7]
        if c >= 0x80 and c <= 0x7ff:
            valid_flags = [bin_len(c) <= 11]
        if c >= 0x800 and c <= 0xffff:
            valid_flags = [bin_len(c) <= 16]
        if c >= 0x10000 and c <= 0x10FFFF:
            valid_flags = [bin_len(c) <= 21]
        if not all(valid_flags) or len(valid_flags) == 0:
            return False
    return True
