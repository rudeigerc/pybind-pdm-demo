cmake_minimum_required(VERSION 3.4...3.18)
project(pybind_pdm_demo)

include(.venv/lib/python3.11/site-packages/pybind11/share/cmake/pybind11/pybind11Config.cmake)
pybind11_add_module(demo src/pybind_pdm_demo/csrc/main.cpp)

target_compile_definitions(demo PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
