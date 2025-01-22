#!/bin/bash

[[ -n "$BUILDDIR" ]] || (echo "! BUILDDIR envvar not set; do 'source 1.setup.sh'" && exit 1)
set -ex

cd $BUILDDIR
# --build=editable enforces that local dependencies are built first
conan build .. --build=editable
