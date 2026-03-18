@echo off
setlocal

cd /d "%~dp0"

echo Running AI Ops Assistant smoke tests...
echo.
python -m unittest tests.test_demo -v

echo.
pause

endlocal
