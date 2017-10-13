from copy import deepcopy

from lbryschema.schema.schema import Schema
from lbryschema.schema import tag_pb2 as tag_pb
from lbryschema.schema import VERSION_MAP


class Tag(Schema):
    @classmethod
    def load(cls, message):
        _tag = deepcopy(message)
        _message_pb = tag_pb.Tag()
        _message_pb.version = VERSION_MAP[_tag.pop("version")]
        _message_pb.taggedClaimId = _tag.pop("taggedClaimId")
        return cls._load(_tag, _message_pb)
