from copy import deepcopy
from lbryschema.schema import metadata_pb2
from lbryschema.schema.fee import Fee
from lbryschema.schema.schema import Schema
from lbryschema.utils import VERSION_MAP


class Metadata(Schema):
    @classmethod
    def load(cls, message, address_base=64):
        _metadata = deepcopy(message)
        _message_pb = metadata_pb2.Metadata()
        _message_pb.version = VERSION_MAP[_metadata.pop("version")]
        if 'fee' in _metadata:
            fee_pb = Fee.load(_metadata.pop('fee'), address_base)
            _message_pb.fee.CopyFrom(fee_pb)
        return cls._load(_metadata, _message_pb)
