#!/bin/bash

BLENDER_BIN=/Applications/Blender.app/Contents/MacOS/Blender
cd rpc_server_extension
${BLENDER_BIN} --command extension build
cd -