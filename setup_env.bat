@echo off
echo Setting up Python virtual environment...

REM Create virtual environment
python -m venv .venv

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
pip install -r requirements.txt

echo.
echo Virtual environment setup complete!
echo To activate in the future, run: .venv\Scripts\activate.bat
echo.
pause



