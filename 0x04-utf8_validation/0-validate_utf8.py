#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    if data is None:
        return False
    try:
        _ = bytes(data).decode("utf-8")
    except Exception:
        return False
    return True
