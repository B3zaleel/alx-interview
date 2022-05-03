#!/usr/bin/python3
"""UTF-8 validation module.
"""
import struct


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    valid_flags = []
    for c in data:
        if type(c) != int:
            return False
        if c >= 0x00 and c <= 0x7f:
            c_bytes = struct.pack(">B", c)
            valid_flags = [c_bytes[0] <= 0b01111111]
        if c >= 0x80 and c <= 0x7ff:
            c_bytes = struct.pack(">H", c)
            valid_flags = [
                c_bytes[0] <= 0b10111111,
                c_bytes[1] <= 0b11011111
            ]
        if c >= 0x800 and c <= 0xffff:
            c_bytes = struct.pack(">I", c)
            valid_flags = [
                (c_bytes[1] <= 0b10111111),
                (c_bytes[2] <= 0b10111111),
                (c_bytes[3] <= 0b11101111)
            ]
        if c >= 0x10000 and c <= 0x10FFFF:
            c_bytes = struct.pack(">I", c)
            valid_flags = [
                (c_bytes[0] <= 0b10111111),
                (c_bytes[1] <= 0b10111111),
                (c_bytes[2] <= 0b10111111),
                (c_bytes[3] <= 0b11110111)
            ]
        if not all(valid_flags) or len(valid_flags) == 0:
            return False
    return True
