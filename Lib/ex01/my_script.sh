#!/bin/sh

pip --version

rm -rf local_lib
mkdir local_lib

# 2>&1 redirige los errores (salida estandar 2) al mismo lugar que la salida estandar 1
pip install --target local_lib git+https://github.com/jaraco/path > path_install.log 2>&1

if [-d "$local_lib"]; then
    python3 my_program.py
else
    echo "Error al instalar path"
fi
