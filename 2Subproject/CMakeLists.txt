cmake_minimum_required(VERSION 3.20)
project(Subproject)

include(../common.cmake)
add_project(Wrappers ../1Wrappers)

add_library(Subproject src/lib.cpp)
add_library(Company::Subproject ALIAS Subproject)
target_include_directories(Subproject PUBLIC include)
target_link_libraries(Subproject PRIVATE Company::Wrappers)

add_executable(SubprojectMain src/main.cpp)
target_link_libraries(SubprojectMain PRIVATE Subproject)
