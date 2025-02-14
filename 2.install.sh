#!/bin/bash

[[ -n "$BUILDDIR" ]] || (echo "! BUILDDIR envvar not set; do 'source 1.setup.sh'" && exit 1)
set -ex

rm -rf $BUILDDIR

# installs only 3rdparty deps (transitively, including ones from our own deps)
# could use both `--build=missing --build=editabble`, but separation of concerns is nice
conan workspace install --build=missing
