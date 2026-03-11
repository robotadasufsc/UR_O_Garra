#!/bin/bash

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

docker build -t ur-driver-ros:main -f "$REPO_ROOT/Dockerfiles/ur_driver_Dockerfile" .