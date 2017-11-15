import lbryschema
from lbryschema.base import b58decode, b58encode
from lbryschema.hashing import double_sha256, hash160
from lbryschema.error import InvalidAddress
from lbryschema.schema import ADDRESS_LENGTH, ADDRESS_PREFIXES, PUBKEY_ADDRESS, SCRIPT_ADDRESS


def validate_lbry_address_bytes(addr_bytes):
    if len(addr_bytes) != ADDRESS_LENGTH:
        raise InvalidAddress("Invalid address length: %i" % len(addr_bytes))
    if lbryschema.BLOCKCHAIN_NAME not in ADDRESS_PREFIXES:
        raise Exception("no prefixes configured for blockchain: %s" % lbryschema.BLOCKCHAIN_NAME)
    if ord(addr_bytes[0]) not in ADDRESS_PREFIXES[lbryschema.BLOCKCHAIN_NAME].itervalues():
        raise InvalidAddress("Invalid address prefix: %.2X" % ord(addr_bytes[0]))
    addr_without_checksum, addr_checksum = addr_bytes[:21], addr_bytes[21:]
    if double_sha256(addr_without_checksum)[:4] != addr_checksum:
        raise InvalidAddress("Invalid address checksum")
    return addr_bytes


def decode_address(v):
    """decode and validate a b58 address"""
    return validate_lbry_address_bytes(b58decode(v))


def encode_address(addr_bytes):
    """validate and encode an address as b58"""
    v = validate_lbry_address_bytes(addr_bytes)
    return b58encode(v)


def hash_160_bytes_to_address(h160, addrtype=PUBKEY_ADDRESS):
    if addrtype == PUBKEY_ADDRESS:
        prefix = chr(ADDRESS_PREFIXES[lbryschema.BLOCKCHAIN_NAME][PUBKEY_ADDRESS])
    elif addrtype == SCRIPT_ADDRESS:
        prefix = chr(ADDRESS_PREFIXES[lbryschema.BLOCKCHAIN_NAME][SCRIPT_ADDRESS])
    else:
        raise Exception("Invalid address prefix")
    return b58encode(prefix + h160 + double_sha256(prefix + h160)[0:4])


def public_key_to_address(public_key):
    return hash_160_bytes_to_address(hash160(public_key))
