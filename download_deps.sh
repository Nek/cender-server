#!/bin/bash

BLENDER_PYTHON=/Applications/Blender.app/Contents/Resources/4.2/python/bin/python3.11
cd rpc_server_extension
${BLENDER_PYTHON} -m pip download transit-python2 --dest ./wheels --only-binary=:all: --pre --python-version=3.11 --platform=win_amd64
${BLENDER_PYTHON} -m pip download transit-python2 --dest ./wheels --only-binary=:all: --pre --python-version=3.11 --platform=macosx_11_0_arm64
# /Applications/Blender.app/Contents/Resources/4.2/python/bin/python3.11 -m pip download transit-python2 --dest ./wheels --only-binary=:all: --pre --python-version=3.11 --platform=manylinux_2_28_x86_64
${BLENDER_PYTHON} -m pip download zerorpc --dest ./wheels --only-binary=:all:  --pre --python-version=3.11 --platform=win_amd64
${BLENDER_PYTHON} -m pip download zerorpc --dest ./wheels --only-binary=:all:  --pre --python-version=3.11 --platform=macosx_11_0_arm64
# /Applications/Blender.app/Contents/Resources/4.2/python/bin/python3.11 -m pip download zerorpc --dest ./wheels --only-binary=:all:  --pre --python-version=3.11 --platform=manylinux_2_28_x86_64
cd -