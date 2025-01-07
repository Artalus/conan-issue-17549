# Reproduction repo for conan-io/conan#17549

```
source 1.setup.sh
./2.install.sh
./3.build.sh
```
The last step (building the `Parsing` project) fails with
```
[ 16%] Building CXX object /tmp/c/1Wrappers/build/CMakeFiles/Wrappers.dir/src/lib.cpp.o
In file included from /tmp/c/1Wrappers/src/lib.cpp:1:
/tmp/c/1Wrappers/include/Wrappers.hpp:2:10: fatal error: rttr/registration: No such file or directory
```
