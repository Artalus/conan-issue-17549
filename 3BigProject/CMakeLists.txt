cmake_minimum_required(VERSION 3.20)
project(BigProject)
add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../2Subproject ${CMAKE_CURRENT_LIST_DIR}/../2Subproject/build/)

add_library(BigProject src/lib.cpp)
target_include_directories(BigProject PUBLIC include)

add_executable(BigProjectMain src/main.cpp)
target_link_libraries(BigProjectMain PRIVATE BigProject)
