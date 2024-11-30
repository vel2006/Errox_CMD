@echo off
echo Seeing if python is installed
python --version >nul
if %errorlevel% neq 0 (
    echo Python is not installed, installing
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.4/python-%PythonVersion%-amd64.exe' -OutFile '%TEMP%\python-installer.exe'"
    %InstallerPath% InstallAllUsers=1 PrependPath=1
    echo python should be installed now
) else (
    echo Python is installed, version below
    python --version
)
echo Testing for python...
python --version >nul
if %errorlevel% neq 0 (
    echo Out of luck it seems.
) else (
    echo Python installed!
)
