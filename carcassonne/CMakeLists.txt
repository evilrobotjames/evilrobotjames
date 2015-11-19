cmake_minimum_required (VERSION 2.6)
project (carcassonne)

# Compiler and flags

if(UNIX)
    SET (CMAKE_CXX_COMPILER             "/usr/bin/clang++")
    SET (CMAKE_CXX_FLAGS                "-Weverything -Wno-c++98-compat -std=c++11 -g")
else()
    SET (CMAKE_CXX_FLAGS                "-W4 -WX /EHsc")
endif()

# Version number
set (carcassonne_VERSION_MAJOR 0)
set (carcassonne_VERSION_MINOR 1)

# Config file, with version number passed from CMake.
configure_file (
  "${PROJECT_SOURCE_DIR}/src/carcassonneConfig.h.in"
  "${PROJECT_BINARY_DIR}/include/carcassonneConfig.h"
  )

include_directories("${PROJECT_BINARY_DIR}/include" "include")

set (
  SOURCE_FILES
  src/carcassonne.cxx
  src/Tile.cxx
  src/Edge.cxx
  src/FeatureSection.cxx
  src/Board.cxx
  src/TileSet.cxx
)

set (
  HEADER_FILES
  include/Tile.h
  include/Edge.h
  include/FeatureSection.h
  include/Board.h
  include/TileSet.h
)

add_executable(
  carcassonne
  ${HEADER_FILES}
  ${SOURCE_FILES})

