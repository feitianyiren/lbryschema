#!/bin/bash
set -euxo pipefail
echo "Building protobuf files"
protoc --python_out=. lbryschema/proto/*.proto
