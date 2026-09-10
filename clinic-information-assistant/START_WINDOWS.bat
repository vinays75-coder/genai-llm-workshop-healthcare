@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel% equ 0 (
    py -3 app.py
) else (
    python app.py
)
echo.
echo If Python was not found, follow the setup steps in README.md.
pause
