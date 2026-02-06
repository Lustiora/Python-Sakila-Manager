@echo off
cd /d "%~dp0"

:START_LOOP
cls

echo ---------------------------------------------------
echo Cleaning up Flet and Python processes...
echo ---------------------------------------------------

pause
taskkill /F /IM flet.exe /T >nul 2>&1
taskkill /F /IM python.exe /T >nul 2>&1

echo ---------------------------------------------------
echo Connect...
echo ---------------------------------------------------

call .venv\Scripts\activate

echo ---------------------------------------------------
echo Flet Hot Reload Mode Starting...
echo [Web Mode] http://localhost:34636
echo [Exit] Ctrl + C
echo ---------------------------------------------------

flet run -r -v -w -p 34636 test_main_window.py

echo ---------------------------------------------------
echo Restart...
echo ---------------------------------------------------

set START_MODE=RESTART
set USER_INPUT=y
set /p USER_INPUT="Restart? (Enter: Auto / N: Exit) : "

if /i "%USER_INPUT%"=="n" goto END
goto START_LOOP

:END
pause