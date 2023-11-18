@echo off

SET PYTHON=python

REM Check Python version
python --version > nul 2>&1
IF %ERRORLEVEL% neq 0 (
    python3 --version > nul 2>&1
    IF %ERRORLEVEL% neq 0 (
        py --version > nul 2>&1
        IF %ERRORLEVEL% neq 0 (
            echo Python is not installed. Please install Python and retry.
            exit /b 1
        ) ELSE (
            SET PYTHON=py
        )
    ) ELSE (
        SET PYTHON=python3
    )
)

REM Clone the repository
git clone https://github.com/Jwizzed/IntercityRailwayReservationSystem.git
cd IntercityRailwayReservationSystem

REM Set up virtual environment
%PYTHON% -m venv venv
.\venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Migrate database
%PYTHON% manage.py migrate

REM Load sample data
%PYTHON% manage.py loaddata sample_db.json

REM Run the server
%PYTHON% manage.py runserver
