name = "ffmpeg"

version = "7.1.1.hh.1.0.2"

authors = [
    "FFmpeg",
]

description = """Collection of libraries and tools for processing multimedia contents"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "nasm",
    "yasm",
    "x264",
    "libpng",
    "freetype",
    "harfbuzz",
]

private_build_requires = []

variants = []


def commands():
    env.REZ_FFMPEG_ROOT = "{root}"
    env.FFMPEG_ROOT = "{root}"
    env.FFMPEG_LOCATION = "{root}"

    # We want to make sure that REZ envs will use this ffmpeg
    # and not any one installed in the system that may be available
    # in /usr/bin.
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")


build_system = "cmake"
uuid = "repository.FFmpeg"
