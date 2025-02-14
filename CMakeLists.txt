cmake_minimum_required(VERSION 3.20)
project(monorepo)
include(FetchContent)

function(add_project NAME DIR)
    FetchContent_Declare(
        ${NAME}
        SOURCE_DIR ${CMAKE_SOURCE_DIR}/${DIR}
        SYSTEM
        OVERRIDE_FIND_PACKAGE
    )
    FetchContent_MakeAvailable(${NAME})
endfunction()

add_project(Wrappers 1Wrappers)
add_project(Subproject 2Subproject)
add_project(BigProject 3BigProject)
