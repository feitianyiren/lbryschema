import hashlib
import lbryschema
from lbryschema.error import InvalidAddress
from lbryschema.schema import ADDRESS_LENGTH, ADDRESS_PREFIXES, B58_CHARS


def sha256(x):
    return hashlib.sha256(x).digest()


def double_sha(x):
    if type(x) is unicode:
        x = x.encode('utf-8')
    return sha256(sha256(x))


def validate_lbry_address_bytes(addr_bytes):
    if len(addr_bytes) != ADDRESS_LENGTH:
        raise InvalidAddress("Invalid address length: %i" % len(addr_bytes))
    if lbryschema.BLOCKCHAIN_NAME not in ADDRESS_PREFIXES:
        raise Exception("no prefixes configured for blockchain: %s" % lbryschema.BLOCKCHAIN_NAME)
    if ord(addr_bytes[0]) not in ADDRESS_PREFIXES[lbryschema.BLOCKCHAIN_NAME]:
        raise InvalidAddress("Invalid address prefix: %.2X" % ord(addr_bytes[0]))
    addr_without_checksum, addr_checksum = addr_bytes[:21], addr_bytes[21:]
    if double_sha(addr_without_checksum)[:4] != addr_checksum:
        raise InvalidAddress("Invalid address checksum")
    return addr_bytes


def decode_address(v):
    """decode and validate a b58 address"""
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += B58_CHARS.find(c) * (58**i)
    result = ''
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = chr(mod) + result
        long_value = div
    result = chr(long_value) + result
    nPad = 0
    for c in v:
        if c == B58_CHARS[0]:
            nPad += 1
        else:
            break
    result = chr(0)*nPad + result
    return validate_lbry_address_bytes(result)


def encode_address(addr_bytes):
    """validate and encode an address as b58"""
    v = validate_lbry_address_bytes(addr_bytes)
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * ord(c)
    result = ''
    while long_value >= 58:
        div, mod = divmod(long_value, 58)
        result = B58_CHARS[mod] + result
        long_value = div
    result = B58_CHARS[long_value] + result
    # Bitcoin does a little leading-zero-compression:
    # leading 0-bytes in the input become leading-1s
    nPad = 0
    for c in v:
        if c == '\0':
            nPad += 1
        else:
            break
    return (B58_CHARS[0]*nPad) + result
