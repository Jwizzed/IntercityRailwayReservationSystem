#!/bin/bash

# Function to check Python version
check_python_version() {
    if command -v python3 &>/dev/null; then
        PYTHON=python3
    elif command -v python &>/dev/null; then
        PYTHON=python
    else
        echo "Python is not installed. Please install Python and retry."
        exit 1
    fi
}

# Clone the repository
git clone https://github.com/Jwizzed/IntercityRailwayReservationSystem.git
cd IntercityRailwayReservationSystem

# Check Python version
check_python_version

# Set up virtual environment
$PYTHON -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
$PYTHON manage.py migrate

# Load sample data
$PYTHON manage.py loaddata sample_db.json

# Run the server
$PYTHON manage.py runserver
