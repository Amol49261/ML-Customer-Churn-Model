#!/bin/bash
echo "Setting up Python virtual environment..."

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

echo ""
echo "Virtual environment setup complete!"
echo "To activate in the future, run: source .venv/bin/activate"
echo ""



