#!/bin/sh

rm -rf django_venv

if python3 -m venv django_venv; then
    if [ -f "requirement.txt" ]; then
        ./django_venv/bin/python3 -m pip install -r requirement.txt
    else
        echo "requirement.txt not found."
    fi
    # Activate the environment
    . django_venv/bin/activate
else
    echo "Error: Failed to create the virtual environment."
    return 1 2>/dev/null || exit 1
fi

# ejecutar ". ./my_script.sh" o "source ./my_script.sh"