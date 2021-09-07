
project(summer_algo_training)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin)
set(CMAKE_OSX_ARCHITECTURES "arm64")



add_executable(4 programmers/kakao_2021/4.cpp)
add_executable(6 programmers/kakao_2021/6.cpp)