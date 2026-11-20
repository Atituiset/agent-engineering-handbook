cmake_minimum_required(VERSION 3.20)
project(durations LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # clang-tidy reads build/compile_commands.json

option(DURATIONS_WERROR "Treat compiler warnings as errors" ON)

add_library(durations src/parse.cpp)
target_include_directories(durations PUBLIC include)
target_compile_options(durations PRIVATE -Wall -Wextra -Wpedantic -Wconversion -Wshadow
                                         $<$<BOOL:${DURATIONS_WERROR}>:-Werror>)

enable_testing()
add_executable(durations_tests tests/test_parse.cpp)
target_link_libraries(durations_tests PRIVATE durations)
# doctest is vendored (single header, MIT, v2.5.3) so builds need no network.
target_include_directories(durations_tests SYSTEM PRIVATE third_party/doctest)
target_compile_options(durations_tests PRIVATE -Wall -Wextra $<$<BOOL:${DURATIONS_WERROR}>:-Werror>)
add_test(NAME durations_tests COMMAND durations_tests)
