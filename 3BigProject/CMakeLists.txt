cmake_minimum_required(VERSION 3.20)
project(BigProject)

include(../common.cmake)
add_project(Subproject ../2Subproject)

add_library(BigProject src/lib.cpp)
target_include_directories(BigProject PUBLIC include)
target_link_libraries(BigProject PRIVATE Company::Subproject)

add_executable(BigProjectMain src/main.cpp)
target_link_libraries(BigProjectMain PRIVATE BigProject)
