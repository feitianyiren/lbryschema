

claim_id_1 = "63f2da17b0d90042c559cc73b6b17f853945c43e"

claim_address_2 = "bDtL6qriyimxz71DSYjojTBsm6cpM1bqmj"

claim_address_1 = "bUG7VaMzLEqqyZQAyg9srxQzvf1wwnJ48w"

nist256p_private_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIHXZGMohUYoryhMYoStxZH7/PYFZQQFyhEU7KMRZKfdroAoGCCqGSM49
AwEHoUQDQgAEcrhIvF3igeK+C91x6xLQCMpra2jSXMVinTj0CS8VP23tLXo5y6Pb
YLab2fMTKDwepl4BGCYvN73G7cnxKdg6wA==
-----END EC PRIVATE KEY-----
"""

nist384p_private_key = """-----BEGIN EC PRIVATE KEY-----
MIGkAgEBBDCnWRVKuHS/fItPyvJw0B+VDmy9QmcI+ZzIoztMW4cnmCf281Aw0C0+
aN1w8248K9+gBwYFK4EEACKhZANiAATx9UnpoL9NcbWRcdtFyTlrFO1Tc6Mc4+tI
kbcfbC83azTEmatGtGbTWLn1QxfRh0VGzu1z2SLLTtf6ovxtnwDcn/tMd0gDsAtD
2eVgEWrUsB7Z+TF019MqehoRBApRWR4=
-----END EC PRIVATE KEY-----
"""

secp256k1_private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIH5u47ekD6CQujHM1/32yFy1p/XdWS6klYFnJZBG6in4oAcGBSuBBAAK
oUQDQgAEtvPIpSPxXjxRvv0pZY9C6lnDRVhmHOJ0+3ItNOlbJqnNykVw/Lqf2QZc
mNhZzfiapBUPgoa0GWkEH9lI8IEilw==
-----END EC PRIVATE KEY-----
"""

nist256p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3059301306072a8648ce3d020106082a8648ce3d0301070342000472b848bc5de281e2be0bdd71eb12d008ca6b6b68d25cc5629d38f4092f153f6ded2d7a39cba3db60b69bd9f313283c1ea65e0118262f37bdc6edc9f129d83ac0", 
    "keyType": "NIST256p", 
    "version": "_0_0_1"
  }
}

nist384p_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3076301006072a8648ce3d020106052b8104002203620004f1f549e9a0bf4d71b59171db45c9396b14ed5373a31ce3eb4891b71f6c2f376b34c499ab46b466d358b9f54317d1874546ceed73d922cb4ed7faa2fc6d9f00dc9ffb4c774803b00b43d9e560116ad4b01ed9f93174d7d32a7a1a11040a51591e", 
    "keyType": "NIST384p", 
    "version": "_0_0_1"
  }
}

secp256k1_cert = {
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a03420004b6f3c8a523f15e3c51befd29658f42ea59c34558661ce274fb722d34e95b26a9cdca4570fcba9fd9065c98d859cdf89aa4150f8286b41969041fd948f0812297", 
    "keyType": "SECP256k1", 
    "version": "_0_0_1"
  }
}

malformed_secp256k1_cert = {
  "keyType": "NIST256p", 
  "version": "_0_0_1", 
  "claimType": "certificateType", 
  "certificate": {
    "publicKey": "3056301006072a8648ce3d020106052b8104000a03420004b6f3c8a523f15e3c51befd29658f42ea59c34558661ce274fb722d34e95b26a9cdca4570fcba9fd9065c98d859cdf89aa4150f8286b41969041fd948f0812297", 
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
    "signature": "4d764a5c6a776a90ff20e9ef5e9d0c1aa639f4e59ebed52b013504710e802b9bbea224d8393b37a60a47ee3593f1df606b663a471fceaf3a640e0d1d255e559c"
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
    "signature": "c77d00a079eb173315775484b9c9d41b972462cfdc234b000cad520b0f64af4d6f4cf6ec2557067f5492c975a3bf63612e9637001a4b9b5a6c551116be9674ea7d1d9af1e6019f6d74249da5272af0c735dca3f3b7649fce59bb884cce71706c"
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
    "signature": "f3c740904f4e0dbc50303dd59cfc045dea7afae0359a23387089950d1e45c1db2fb56be296b9f6177e13590f9685ecc2b432424cffb16f963286d09fd626652b"
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
