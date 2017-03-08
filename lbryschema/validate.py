import ecdsa
import hashlib
from lbryschema.schema.signature import Signature
from lbryschema.schema.cert import Cert
from lbryschema.schema.claim import Claim


def _make_sig(signature, sig_type):
    _sig = {
        "version": "_0_0_1",
        "signatureType": sig_type,
        "signature": signature
    }
    return Signature.load(_sig)


def _sign_stream(stream, claim_id, public_key, cert_claim_id):
    validate_claim_id(claim_id)
    validate_claim_id(cert_claim_id)
    serialized = stream.SerializeToString()
    to_sign = "%s%s%s" % (claim_id, serialized, cert_claim_id)
    digest = hashlib.sha256(to_sign).digest()
    if isinstance(public_key, ecdsa.SigningKey):
        sig = public_key.sign_digest_deterministic(digest, hashfunc=hashlib.sha256)
        sig_type = "ECDSA"
    else:
        raise Exception("Unknown key type")

    sig_msg = _make_sig(sig, sig_type)
    return sig_msg


def sign_stream_claim(claim, claim_id, public_key, cert_claim_id):
    if isinstance(claim, dict):
        claim = Claim.load(claim)
    signature = _sign_stream(claim, claim_id, public_key, cert_claim_id)
    msg = {
        "version": "_0_0_1",
        "stream": claim.stream,
        "publisherSignature": signature
    }
    return Claim.load(msg)


def make_cert(public_key):
    return Cert.load_from_key_obj(public_key)


def validate_claim_id(claim_id):
    hex_chars = "0123456789abcdefABCDEF"
    assert len(claim_id) == 64, "Incorrect claimid length: %i" % len(claim_id)
    for c in claim_id:
        assert c in hex_chars, "Claim id is not hex encoded"


def validate_signed_stream_claim(claim, claim_id, cert, cert_claim_id):
    # check that the claim ids provided are the 64 characters long and hex encoded
    validate_claim_id(claim_id)
    validate_claim_id(cert_claim_id)

    # extract and serialize the stream from the claim, then check the signature
    cert_public_key = cert.publicKey
    key_type = cert.keyType
    if key_type == 1:
        key = ecdsa.VerifyingKey.from_der(cert_public_key)

    publisher_signature = claim.publisherSignature.signature
    _temp_claim_dict = {
        "version": "_0_0_1",
        "stream": claim.stream
    }
    _temp_claim = Claim.load(_temp_claim_dict)
    serialized = _temp_claim.SerializeToString()
    to_sign = "%s%s%s" % (claim_id, serialized, cert_claim_id)

    if isinstance(key, ecdsa.VerifyingKey):
        verified = key.verify(publisher_signature, to_sign, hashfunc=hashlib.sha256)
    else:
        raise Exception("Unknown key type")
    return verified
