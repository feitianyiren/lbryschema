import hashlib


def sha256(x):
    return hashlib.sha256(x).digest()


def double_sha256(x):
    if type(x) is unicode:
        x = x.encode('utf-8')
    return sha256(sha256(x))


def ripemd160(x):
    md = hashlib.new('ripemd160')
    md.update(x)
    return md.digest()


def hash160(x):
    return ripemd160(sha256(x))
