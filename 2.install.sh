#!/bin/bash

[[ -n "$BUILDDIR" ]] || (echo "! BUILDDIR envvar not set; do 'source 1.setup.sh'" && exit 1)
set -ex

rm -rf $BUILDDIR
mkdir $BUILDDIR
cd $BUILDDIR

# installs only 3rdparty deps (transitively, including ones from our own deps)
# could use both `--build=missing --build=editabble`, but separation of concerns is nice
conan install .. --build=missing
