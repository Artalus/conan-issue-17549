#!/bin/bash

export BUILDDIR=`pwd`/build/
echo "** Building all./bui"
./2.install.sh
./3.build.sh
