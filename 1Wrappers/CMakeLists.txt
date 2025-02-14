cmake_minimum_required(VERSION 3.20)
project(Wrappers)
find_package(rttr REQUIRED)

add_library(Wrappers src/lib.cpp)
add_library(Company::Wrappers ALIAS Wrappers)
target_include_directories(Wrappers PUBLIC include)
target_link_libraries(Wrappers PUBLIC RTTR::Core_Lib)

add_executable(WrappersMain src/main.cpp)
target_link_libraries(WrappersMain PRIVATE Wrappers)
