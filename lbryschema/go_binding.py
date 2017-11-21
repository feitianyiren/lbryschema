import os
import json
from ctypes import *
from ecdsa.keys import BadSignatureError
from lbryschema.error import DecodeError


class GoString(Structure):
    _fields_ = [
        ("p", c_char_p),
        ("n", c_longlong)
    ]


def from_go_string(s):
    return string_at(addressof(s), sizeof(s))


def get_go_string(s):
    if not isinstance(s, (str, unicode)):
        raise TypeError("invalid type: %s" % str(type(s)))
    x = str(s)
    return GoString(x, len(x))


GO_TYPES = {
    str: GoString
}

GO_TYPE_MAP = {
    str: get_go_string
}

RETURN_TYPES = {
    bool: c_bool,
    int: c_int,
    str: c_char_p,
}

_LOADED = {}
_FUNCTIONS = {}

GO_MODULE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "include/lbryschema-python-binding.so")


def import_go_function(f, r_type, *a_types):
    for v in a_types:
        if not isinstance(v, type):
            raise TypeError("invalid argument type")
        if v not in GO_TYPES:
            raise TypeError("type does not have a mapping: %s" % str(type(v)))

    # load the library
    if GO_MODULE_PATH not in _LOADED:
        print "Loading library: %s" % GO_MODULE_PATH
        lib = cdll.LoadLibrary(GO_MODULE_PATH)
        _LOADED[GO_MODULE_PATH] = lib
    else:
        lib = _LOADED[GO_MODULE_PATH]

    # get the function
    if not f.__name__.startswith("Go"):
        raise NameError("decorated functions must be prefixed with \"Go\"")
    fn_name = f.__name__[2:]

    if fn_name in _FUNCTIONS:
        go_func = _FUNCTIONS[fn_name]
    else:
        # set the argtypes and return type and cache the function
        if not hasattr(lib, fn_name):
            raise AttributeError("function (%s) not found in module: %s" % (fn_name,
                                                                            GO_MODULE_PATH))
        go_func = getattr(lib, fn_name)
        go_func.argtypes = [GO_TYPES[v] for v in a_types]
        # set the return type
        go_func.restype = RETURN_TYPES[r_type]
        _FUNCTIONS[fn_name] = go_func
        print "Set up binding for %s(%s)" % (f.__name__,
                                                    ", ".join(t.__name__
                                                              for t in go_func.argtypes))
    return go_func


def go_function(return_type=bool, *arg_types):
    """
    Get a binding to a go function of the same name in the given .so file
    The python function itself may return a callback to be called with the results of the go
    function. If the function does not return a callable, the python function is ignored and
    the result from go is returned.

    :param return_type: (type) return type
    :param arg_types: (type) *parameter types
    """

    if not os.path.isfile(GO_MODULE_PATH):
        raise OSError("path to library is invalid: %s" % GO_MODULE_PATH)

    def inner(fn):
        go_func = import_go_function(fn, return_type, *arg_types)

        # return a function which wraps the arguments to their go types and calls the go function
        def _wrap(*args):
            if len(args) != len(go_func.argtypes):
                raise ArgumentError("argument count mismatch, %i provided but %i were expected" %
                                    (len(args), len(go_func.argtypes)))
            _args = [GO_TYPE_MAP[arg_type](arg) for arg_type, arg in zip(arg_types, args)]

            go_result = go_func(*tuple(_args))

            # if the function returns a callable, callback the from go to it
            # otherwise return
            fn_result = fn(*args)
            if callable(fn_result):
                return fn_result(go_result)
            return go_result
        return _wrap
    return inner


if not os.path.isfile(GO_MODULE_PATH):
    def GoVerifySignature(claim, certificate, claim_address, certificate_id, blockchain_name):
        raise NotImplementedError()


    def GoDecodeClaimHex(claim, blockchain_name):
        raise NotImplementedError()
else:
    @go_function(bool, str, str, str, str, str)
    def GoVerifySignature(claim, certificate, claim_address, certificate_id, blockchain_name):
        """
        Use ClaimHelper.ValidateClaimSignature from lbryschema.go

        :param claim: (string) serialized claim hex
        :param certificate:  (string) serialized certificate claim hex
        :param claim_address: (string) claim address
        :param certificate_id: (string) certificate claim id hex
        :return: (bool) True or raise BadSignatureError
        """

        def callback(result):
            if result:
                return True
            raise BadSignatureError()
        return callback

    @go_function(str, str, str)
    def GoDecodeClaimHex(claim, blockchain_name):
        """
        Use ClaimHelper.DecodeClaimHex to decode a serialized claim to json

        :param blockchain_name: (string) blockchain name:
                                         lbrycrd_main | lbrycrd_testnet | lbrycrd_regtest
        :param claim: (string) serialized claim hex
        :return: (string) claim json
        """

        def callback(result):
            try:
                result = json.loads(result)
            except ValueError:
                raise DecodeError()
            return result[result.keys()[0]]
        return callback
