import re


def is_valid_ipv4(ip):
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]" \
            r"[0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, ip) is not None


def is_valid_ipv6(ip):
    pattern = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return re.match(pattern, ip) is not None


ipv4_address = "192.168.0.1"
ipv6_address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"

print("IPv4 Address:", ipv4_address)
print("Is valid IPv4:", is_valid_ipv4(ipv4_address))

print("IPv6 Address:", ipv6_address)
print("Is valid IPv6:", is_valid_ipv6(ipv6_address))
