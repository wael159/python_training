"""
Meta Interview Format: is_valid_ip
============================================================
Main Question:
------------------------------------------------------------
Implement a function `is_valid_ipv4` that determines whether a given string is a valid IPv4 address.

An IPv4 address consists of exactly 4 integers (0–255) separated by dots. No extra characters are allowed.

Examples:
    is_valid_ipv4("192.168.1.1") -> True
    is_valid_ipv4("256.100.50.25") -> False
    is_valid_ipv4("192.abc.1.1") -> False
    is_valid_ipv4("192.168.1") -> False

Constraints:
- No use of third-party libraries.
- Ignore whitespace at start/end of string.
"""

def is_valid_ipv4(ip: str) -> bool:
    ip = ip.strip()
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if not (0 <= num <= 255):
            return False
    return True


# ------------------------------------------------------------
# Follow-up 1:
# ------------------------------------------------------------
"""
Add a new constraint: Disallow leading zeros in any segment.
That is, "01.2.3.4" is invalid. Only "0" itself is allowed.

Examples:
    is_valid_ipv4_strict("01.2.3.4") -> False
    is_valid_ipv4_strict("0.0.0.0") -> True
    is_valid_ipv4_strict("192.168.001.1") -> False
"""

def is_valid_ipv4_strict(ip: str) -> bool:
    ip = ip.strip()
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == "0":
            return False
        num = int(part)
        if not (0 <= num <= 255):
            return False
    return True


# ------------------------------------------------------------
# Follow-up 2:
# ------------------------------------------------------------
"""
Optimize for streaming large files line-by-line (e.g., log with 10M IPs).
Write a function that takes an iterable of strings (like a file), and
prints which ones are valid.

Constraints:
- Memory-efficient
- Reuse previously written logic
"""

def process_ip_stream(stream, strict=False):
    for line in stream:
        ip = line.strip()
        if (is_valid_ipv4_strict(ip) if strict else is_valid_ipv4(ip)):
            print(f"{ip} => VALID")
        else:
            print(f"{ip} => INVALID")


# ------------------------------------------------------------
# Discussion:
# ------------------------------------------------------------
"""
Time Complexity:
- O(1) per IP (constant work for 4 segments)

Space Complexity:
- O(1) – small fixed buffers per IP

Real-World Use Cases:
- Log file validation
- Preprocessing data for geolocation
- Firewall or IP whitelist configuration

Edge Cases:
- "192.168.1" (too few parts)
- "192.168.1.1.1" (too many parts)
- "192.168.abc.1" (non-digit)
- "256.100.100.100" (out of range)
- "01.2.3.4" (leading zero)

"""

# ------------------------------------------------------------
# Advanced Extension (Optional)
# ------------------------------------------------------------
"""
Extend to IPv6 support.
An IPv6 consists of 8 groups of 1-4 hex digits separated by colons.
Use regex or parsing. Skip shorthand formats for now (e.g., "::").

Example:
    is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334") -> True
    is_valid_ipv6("2001:db8::8a2e:370:7334") -> False (skip shorthand)
"""

import re
def is_valid_ipv6(ip: str) -> bool:
    pattern = re.compile(r"""
        ^(
            ([0-9a-fA-F]{1,4}:){7}
            [0-9a-fA-F]{1,4}
        )$
    """, re.VERBOSE)
    return bool(pattern.match(ip))


# ------------------------------------------------------------
# Sample Test Cases
# ------------------------------------------------------------

if __name__ == "__main__":
    print("Main Function:")
    print(is_valid_ipv4("192.168.1.1"))       # True
    print(is_valid_ipv4("256.100.50.25"))     # False
    print(is_valid_ipv4("192.abc.1.1"))       # False
    print(is_valid_ipv4("192.168.1"))         # False

    # print("\nFollow-up 1:")
    # print(is_valid_ipv4_strict("192.168.1.1"))     # True
    # print(is_valid_ipv4_strict("01.2.3.4"))        # False
    # print(is_valid_ipv4_strict("0.0.0.0"))         # True
    # print(is_valid_ipv4_strict("192.168.001.1"))   # False
    #
    # print("\nFollow-up 2 (Stream):")
    # test_ips = [
    #     "192.168.1.1",
    #     "255.255.255.255",
    #     "256.256.256.256",
    #     "abc.def.ghi.jkl",
    #     "123.045.067.089"
    # ]
    # process_ip_stream(test_ips, strict=True)
    #
    # print("\nAdvanced (IPv6):")
    # print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # True
    # print(is_valid_ipv6("2001:db8::8a2e:370:7334"))                  # False
