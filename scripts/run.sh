#!/bin/bash

set -e
set -u

export DISPLAY=:0.0

pushd vecx
./vecx > /dev/null
popd
