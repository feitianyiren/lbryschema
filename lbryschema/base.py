from lbryschema.schema import B58_CHARS


def b58decode(v):
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += B58_CHARS.find(c) * (58 ** i)
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
    return chr(0) * nPad + result


def b58encode(v):
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += (256 ** i) * ord(c)
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
    return (B58_CHARS[0] * nPad) + result
