cmake_minimum_required (VERSION 2.6)
project (carcassonne)

# Compiler and flags

if(UNIX)
    SET (CMAKE_CXX_COMPILER             "/usr/bin/clang++")
    SET (CMAKE_CXX_FLAGS                "-Weverything -std=c++11 -g")
else()
    SET (CMAKE_CXX_FLAGS                "-Wall -WX")
endif()

# Version number
set (carcassonne_VERSION_MAJOR 0)
set (carcassonne_VERSION_MINOR 1)

# Config file, with version number passed from CMake.
configure_file (
  "${PROJECT_SOURCE_DIR}/src/carcassonneConfig.h.in"
  "${PROJECT_BINARY_DIR}/carcassonneConfig.h"
  )

include_directories("${PROJECT_BINARY_DIR}")

add_executable(carcassonne src/carcassonne.cxx src/Tile.cxx src/Edge.cxx src/Component.cxx)
