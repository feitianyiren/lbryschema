

claim_id_1 = "63f2da17b0d90042c559cc73b6b17f853945c43e"

claim_address_2 = "bDtL6qriyimxz71DSYjojTBsm6cpM1bqmj"

claim_address_1 = "bUG7VaMzLEqqyZQAyg9srxQzvf1wwnJ48w"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIHvE3A1ETY3BelasigKYFhte8oO3u4MJRa5Ag3WA4PrIoAoGCCqGSM49
AwEHoUQDQgAEWpvz9VLObJe5nMemYOx3nN7gtAIPqkw28YlWTN3wD7/JkirAbV5W
1AJR63k0VPx7kjZVMao/AKev5eeITPNbcw==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDB03e6ZKluVpNMBZT3MgzoI15xM8gSXSqi0ep7uew9arQS9p5N+eFY4
IyejkHMhMmKgBwYFK4EEACKhZANiAARlNW9feoF/F8HhIyPCSFiqcomaUDd6EUR6
lgYrZzp9ssmHMlRpTWEBfrm8yM9VeKyOtF1a4Ae6NjVyKQf2Xf+U6wvWrSFUiv8t
PezH1zioFRNJc6CtXVIzPM2DkdIHV2A=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIEjQeHXQVlJSQdNssQfvn0s0XH85NkykuPD6yGJXaA7ooAcGBSuBBAAK
oUQDQgAESldQDPYoeV8Ft2cj/PrksI3Js7aHYDQw5GfSw91qjwuphisMKmBmXU3O
3AfJuzqlqsrOPIuE4GnsBQ651FnCyw==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d030107034200045a9bf3f552ce6c97b99cc7a660ec779cdee0b4020faa4c36f189564cddf00fbfc9922ac06d5e56d40251eb793454fc7b92365531aa3f00a7afe5e7884cf35b73", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b810400220362000465356f5f7a817f17c1e12323c24858aa72899a50377a11447a96062b673a7db2c9873254694d61017eb9bcc8cf5578ac8eb45d5ae007ba3635722907f65dff94eb0bd6ad21548aff2d3decc7d738a815134973a0ad5d52333ccd8391d2075760", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a034200044a57500cf628795f05b76723fcfae4b08dc9b3b687603430e467d2c3dd6a8f0ba9862b0c2a60665d4dcedc07c9bb3aa5aacace3c8b84e069ec050eb9d459c2cb", 
    "keyType": "SECP256k1", 
    "version": "_0_0_1"
  }
}

malformed_secp256k1_cert = {
  "keyType": "NIST256p", 
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a034200044a57500cf628795f05b76723fcfae4b08dc9b3b687603430e467d2c3dd6a8f0ba9862b0c2a60665d4dcedc07c9bb3aa5aacace3c8b84e069ec050eb9d459c2cb", 
    "keyType": "SECP256k1", 
    "version": "_0_0_1"
  }
}

example_003 = {
  "language": "en", 
  "license": "LBRY Inc", 
  "nsfw": False, 
  "description": "What is LBRY? An introduction with Alex Tabarrok", 
  "content_type": "video/mp4", 
  "author": "Samuel Bryan", 
  "ver": "0.0.3", 
  "title": "What is LBRY?", 
  "sources": {
    "lbry_sd_hash": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b"
  }, 
  "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
}

example_010 = {
  "version": "_0_0_1", 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash", 
      "publishTime": "0"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

example_010_serialized = "080110011ade010801129401080410011a0d57686174206973204c4252593f223057686174206973204c4252593f20416e20696e74726f64756374696f6e207769746820416c6578205461626172726f6b2a0c53616d75656c20427279616e32084c42525920496e6338004a2f68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f66696c65732e6c6272792e696f2f6c6f676f2e706e6752005a001a43080110011a30d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b2209766964656f2f6d70342800"

claim_010_signed_nist256p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "certificateId": "63f2da17b0d90042c559cc73b6b17f853945c43e", 
    "signatureType": "NIST256p", 
    "version": "_0_0_1", 
    "signature": "d629b1c1201efb73a6f92b07cdb8041508150101561aa90dfcc3e2f1a09caea5bd36b3d6ca8b546ae825c528938694dd3e8d0bae17c1e69dd46748429df1cb4d"
  }, 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash", 
      "publishTime": "0"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

claim_010_signed_nist384p = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "certificateId": "63f2da17b0d90042c559cc73b6b17f853945c43e", 
    "signatureType": "NIST384p", 
    "version": "_0_0_1", 
    "signature": "44a612ab870f7006bb0d52aa6a523e53a56fe8e5e0ce73c3c945d306b6e820e7fa6ad62a93cc8f59f8b6171a59a0a5955fe5c3abb9610c12122074d308780b3f544297f662ff74cee0c3a26ca097272dc3e2396898e37827fbc3785ac4766a14"
  }, 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash", 
      "publishTime": "0"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

claim_010_signed_secp256k1 = {
  "version": "_0_0_1", 
  "publisherSignature": {
    "certificateId": "63f2da17b0d90042c559cc73b6b17f853945c43e", 
    "signatureType": "SECP256k1", 
    "version": "_0_0_1", 
    "signature": "4393212922689643561cf40ce92f86b8bcd91c17c277b1bb73021079886b4649d618afb07973a36b6ff231007abbeb63c197587818e4455f50c004319311f919"
  }, 
  "claimType": "streamType", 
  "stream": {
    "source": {
      "source": "d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b", 
      "version": "_0_0_1", 
      "contentType": "video/mp4", 
      "sourceType": "lbry_sd_hash", 
      "publishTime": "0"
    }, 
    "version": "_0_0_1", 
    "metadata": {
      "license": "LBRY Inc", 
      "description": "What is LBRY? An introduction with Alex Tabarrok", 
      "language": "en", 
      "title": "What is LBRY?", 
      "author": "Samuel Bryan", 
      "version": "_0_1_0", 
      "nsfw": False, 
      "licenseUrl": "", 
      "preview": "", 
      "thumbnail": "https://s3.amazonaws.com/files.lbry.io/logo.png"
    }
  }
}

hex_encoded_003 = "080110011ade010801129401080410011a0d57686174206973204c4252593f223057686174206973204c4252593f20416e20696e74726f64756374696f6e207769746820416c6578205461626172726f6b2a0c53616d75656c20427279616e32084c42525920496e6338004a2f68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f66696c65732e6c6272792e696f2f6c6f676f2e706e6752005a001a43080110011a30d5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b2209766964656f2f6d70342800"

decoded_hex_encoded_003 = {u'version': u'_0_0_1', u'claimType': u'streamType', u'stream': {u'source': {u'source': u'd5169241150022f996fa7cd6a9a1c421937276a3275eb912790bd07ba7aec1fac5fd45431d226b8fb402691e79aeb24b', u'version': u'_0_0_1', u'contentType': u'video/mp4', u'sourceType': u'lbry_sd_hash', u'publishTime': u'0'}, u'version': u'_0_0_1', u'metadata': {u'license': u'LBRY Inc', u'description': u'What is LBRY? An introduction with Alex Tabarrok', u'language': u'en', u'title': u'What is LBRY?', u'author': u'Samuel Bryan', u'version': u'_0_1_0', u'nsfw': False, u'licenseUrl': u'', u'preview': u'', u'thumbnail': u'https://s3.amazonaws.com/files.lbry.io/logo.png'}}}
