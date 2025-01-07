#!/bin/bash

[[ -n "$BUILDDIR" ]] || (echo "! BUILDDIR envvar not set; do 'source 1.setup.sh'" && exit 1)
set -ex

for x in pyreq.py 1Wrappers 2Subproject 3BigProject ; do conan editable add ./$x ; done

rm -rf $BUILDDIR
mkdir $BUILDDIR
cd $BUILDDIR
conan install .. --build=missing
