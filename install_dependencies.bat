@echo off

:: Set the execution policy to allow running PowerShell scripts
powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"

:: Run the PowerShell script
powershell -File "%~dp0install_dependencies.ps1"

:: Pause to keep the console window open (optional)
pause
