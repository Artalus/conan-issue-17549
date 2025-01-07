cmake_minimum_required(VERSION 3.20)
project(Wrappers)
find_package(rttr REQUIRED)

add_library(Wrappers src/lib.cpp)
target_include_directories(Wrappers PUBLIC include)
target_link_libraries(Wrappers PUBLIC RTTR::Core_Lib)
