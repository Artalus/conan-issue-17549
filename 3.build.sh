#!/bin/bash

[[ -n "$BUILDDIR" ]] || (echo "! BUILDDIR envvar not set; do 'source 1.setup.sh'" && exit 1)
set -ex

cd $BUILDDIR
cmake .. -DCMAKE_TOOLCHAIN_FILE=$BUILDDIR/Conan/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
cmake --build .
