#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    byte_parts = []
    for c in data:
        if c >= 0x00 and c <= 0x7f:
            byte_parts.append(c)
        elif c >= 0x80 and c <= 0x7ff:
            byte_parts.append((c >> 6) | 0b11000000)
            byte_parts.append(c - (1 << 6))
        else:
            return False
    try:
        _ = bytes(byte_parts).decode("utf-8", "strict")
    except Exception:
        return False
    return True
