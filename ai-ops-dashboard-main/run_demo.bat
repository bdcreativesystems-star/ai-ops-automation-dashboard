@echo off
setlocal

cd /d "%~dp0"

echo Starting AI Ops Assistant demo...
echo.
echo If your browser does not open automatically, visit:
echo http://127.0.0.1:5000
echo.

set "PYTHON_CMD=python"
if exist "..\venv\Scripts\python.exe" set "PYTHON_CMD=..\venv\Scripts\python.exe"
if exist "venv\Scripts\python.exe" set "PYTHON_CMD=venv\Scripts\python.exe"

start "" cmd /c "timeout /t 2 /nobreak >nul && start "" http://127.0.0.1:5000"

%PYTHON_CMD% app.py
set "EXIT_CODE=%ERRORLEVEL%"

if not "%EXIT_CODE%"=="0" (
    echo.
    echo The demo server stopped with exit code %EXIT_CODE%.
    echo Keep this window open and read the error above.
    pause
)

endlocal
