CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(pck_name ffmpeg)
set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules")

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

# ffplay needs SDL2-devel libs in the system

ExternalProject_add(
    ${pck_name}
    SOURCE_DIR ${CMAKE_SOURCE_DIR}
    PREFIX ${pck_name}
    CONFIGURE_COMMAND ${CMAKE_SOURCE_DIR}/configure
        --prefix=${CMAKE_INSTALL_PREFIX}
        --extra-libs=-lpthread
        --extra-libs=-lm
        --disable-doc
        --enable-gpl
        --enable-version3
        --enable-nonfree
        # --enable-shared  # always build static so not to conflict with Houdini's libs
        --enable-static
        --disable-shared
        --enable-ffplay
        --enable-libx264
        --enable-decoder=mp3
        --enable-libfontconfig
        --enable-libfreetype
        --enable-libharfbuzz
        --enable-libzimg
    BUILD_COMMAND make ${make_args}
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

# Necessary for REZ to create 'make install' target
rez_install_files(
    README.md
    DESTINATION .
)
