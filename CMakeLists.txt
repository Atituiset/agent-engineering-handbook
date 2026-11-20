cmake_minimum_required(VERSION 3.20)
project(durations LANGUAGES C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # clang-tidy reads build/compile_commands.json

option(DURATIONS_WERROR "Treat compiler warnings as errors" ON)
set(DURATIONS_WARNINGS -Wall -Wextra -Wpedantic -Wconversion -Wsign-conversion -Wshadow
                       -Wstrict-prototypes -Wmissing-prototypes
                       $<$<BOOL:${DURATIONS_WERROR}>:-Werror>)

add_library(durations src/parse.c)
target_include_directories(durations PUBLIC include)
target_compile_options(durations PRIVATE ${DURATIONS_WARNINGS})

# Unity is vendored (v2.7.0, MIT, see third_party/unity/LICENSE.txt) so builds
# need no network. It is third-party code: built without our warning flags.
add_library(unity STATIC third_party/unity/unity.c)
target_include_directories(unity SYSTEM PUBLIC third_party/unity)

enable_testing()
add_executable(durations_tests tests/test_parse.c)
target_link_libraries(durations_tests PRIVATE durations unity)
target_compile_options(durations_tests PRIVATE ${DURATIONS_WARNINGS})
add_test(NAME durations_tests COMMAND durations_tests)
