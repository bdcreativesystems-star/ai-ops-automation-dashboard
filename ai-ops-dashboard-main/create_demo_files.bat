@echo off
setlocal

cd /d "%~dp0"

if not exist "demo_test" mkdir "demo_test"

echo item,quantity,status> "demo_test\inventory.csv"
echo Laptops,12,ready>> "demo_test\inventory.csv"
echo Monitors,8,ready>> "demo_test\inventory.csv"
echo Badges,24,pending>> "demo_test\inventory.csv"

echo Operations notes:> "demo_test\ops_notes.txt"
echo - Review inventory intake>> "demo_test\ops_notes.txt"
echo - Confirm onboarding packets>> "demo_test\ops_notes.txt"
echo - Schedule system health check>> "demo_test\ops_notes.txt"

echo Sample image placeholder for the demo file organizer.> "demo_test\team_photo.jpg"
echo Sample PDF placeholder for the demo file organizer.> "demo_test\monthly_report.pdf"
echo Sample spreadsheet placeholder for the demo file organizer.> "demo_test\client_data.xlsx"

echo Demo files are ready in:
echo %cd%\demo_test
echo.
pause

endlocal
