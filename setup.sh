#!/bin/bash

# Script to create and set up a Python virtual environment with a specified name

# Check for command-line argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <venv_name>"
  exit 1
fi

# Set the name of the virtual environment directory from the first command-line argument
VENV_DIR=$1

# Check if the virtual environment directory already exists
if [ -d "$VENV_DIR" ]; then
  echo "Virtual environment $VENV_DIR already exists."
else
  # Create the virtual environment
  python3 -m venv $VENV_DIR
  echo "Virtual environment $VENV_DIR created."
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate
echo "Activated the virtual environment."

# Install dependencies from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
  pip3 install -r requirements.txt
  echo "Dependencies installed."
else
  echo "requirements.txt not found, no dependencies installed."
fi

echo "Setup complete."