
project(summer_algo_training)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin)
set(CMAKE_OSX_ARCHITECTURES "arm64")






add_executable(82612 programmers/82612.cpp)
add_executable(3 "programmers/code challenge 3-2/3.cpp")
add_executable(2805_2 BOJ/2805_2.cpp)
add_executable(1654 BOJ/1654.cpp)
add_executable(84021 programmers/84021.cpp)