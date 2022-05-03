#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if data[i] < 0 or data[i] > 0xff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        elif (data[i] >> 3) & 0b11111 == 0b11110:
            # 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x >> 6 == 0b10,
                    data[i + 1: span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif (data[i] >> 4) & 0b1111 == 0b1110:
            # 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x >> 6 == 0b10,
                    data[i + 1: span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif (data[i] >> 5) & 0b111 == 0b110:
            # 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x >> 6 == 0b10,
                    data[i + 1: span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
    return skip == 0
