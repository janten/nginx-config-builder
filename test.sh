#!/bin/bash

docker build --tag config-builder .
docker run --rm -v $(pwd)/sites:/sites config-builder