name = "ffmpeg"

version = "6.1.1.hh.1.0.2"

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

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")


build_system = "cmake"
uuid = "repository.FFmpeg"
