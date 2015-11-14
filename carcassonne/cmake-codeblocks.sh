#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILD_DIR="$SCRIPT_DIR/build.codeblocks-unix"

mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"
cmake -G "CodeBlocks - Unix Makefiles" ..
