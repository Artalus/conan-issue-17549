#!/bin/bash

export BUILDDIR=`pwd`/3BigProject/build/
echo "** Building the BigProject"
./2.install.sh
./3.build.sh

echo "** Building the Subproject instead"
export BUILDDIR=`pwd`/2Subproject/build/
./2.install.sh
./3.build.sh

echo "** Building just the Wrappers"
export BUILDDIR=`pwd`/1Wrappers/build/
./2.install.sh
./3.build.sh
