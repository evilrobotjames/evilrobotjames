SET (CMAKE_CXX_COMPILER             "/usr/bin/clang++")
SET (CMAKE_CXX_FLAGS                "-Weverything -std=c++11")

cmake_minimum_required (VERSION 2.6)
project (carcassonne)
add_executable(carcassonne src/carcassonne.cxx src/Tile.cxx src/Edge.cxx)
