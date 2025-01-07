cmake_minimum_required(VERSION 3.20)
project(BigProject)
add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../2Subproject ${CMAKE_CURRENT_LIST_DIR}/../2Subproject/build/)

add_library(BigProject src/lib.cpp)
target_include_directories(BigProject PUBLIC include)
target_link_libraries(BigProject PRIVATE Subproject)
