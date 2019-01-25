#!/bin/bash
set -e  # Exit on any failure

BasePath=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
PROJECT_NAME="teamtry"
Archive="$PROJECT_NAME.tar.gz"

VirtualEnvPath="$BasePath/virtualenv"

if [[ ! -e "${VirtualEnvPath}" ]]; then
    echo "-> Setting up virtualenv"
    virtualenv ${VirtualEnvPath}
fi

echo "-> Installing requirements into ${VirtualEnvPath}"
"${VirtualEnvPath}/bin/pip" install --upgrade pip
"${VirtualEnvPath}/bin/pip" install -r "$BasePath/build/requirements.txt"

echo "-> Done"

cp -r src build/
cd build
make all
rm -rf src