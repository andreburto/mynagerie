#!/bin/bash

# Ensure we start from the same directory as the script.
cd $(dirname $0)

# Move to the project root.
cd ..

CURRENT_DIR="$(pwd)"

docker run -it --env-file "${CURRENT_DIR}/.env" \
--mount type=bind,source="${CURRENT_DIR}/src",target=/app/src \
--mount type=bind,source="${CURRENT_DIR}/data",target=/app/data \
-p 8000:8000 mynagerie $@
