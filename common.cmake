include_guard()
include(FetchContent)
function(add_project NAME DIR)
    FetchContent_Declare(
        ${NAME}
        SOURCE_DIR ${CMAKE_SOURCE_DIR}/${DIR}
        SYSTEM
        OVERRIDE_FIND_PACKAGE
    )
    FetchContent_MakeAvailable(${NAME})

    find_package(${NAME} CONFIG REQUIRED)
endfunction()
