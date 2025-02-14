#!/bin/bash

[[ -n "$BUILDDIR" ]] || (echo "! BUILDDIR envvar not set; do 'source 1.setup.sh'" && exit 1)
set -ex

cmake --preset conan-release
cmake --build --preset conan-release
