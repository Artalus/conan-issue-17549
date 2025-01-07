cmake_minimum_required(VERSION 3.20)
project(Subproject)
add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../1Wrappers ${CMAKE_CURRENT_LIST_DIR}/../1Wrappers/build)

add_library(Subproject src/lib.cpp)
target_include_directories(Subproject PUBLIC include)
target_link_libraries(Subproject PRIVATE Wrappers)
