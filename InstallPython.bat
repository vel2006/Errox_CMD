@echo off
set PythonVersion=3.12.4
set PythonInstaller=https://www.python.org/ftp/python/%PythonVersion%/python-%PythonVersion%-amd64.exe
set InstallerPath=%TEMP%\python-installer.exe
powershell -Command "Invoke-WebRequest -Uri '%PythonInstaller%' -OutFile '%InstallerPath%'"
%InstallerPath% /quiet InstallAllUsers=1 PrependPath=1
