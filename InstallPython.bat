@echo off
echo Seeing if python is installed
python --version >nul
if %errorlevel% neq 0 (
    echo Python is not installed, installing
    set PythonVersion=3.12.4
    set PythonInstaller=https://www.python.org/ftp/python/%PythonVersion%/python-%PythonVersion%-amd64.exe
    set InstallerPath=%TEMP%\python-installer.exe
    powershell -Command "Invoke-WebRequest -Uri '%PythonInstaller%' -OutFile '%InstallerPath%'"
    %InstallerPath% /quiet InstallAllUsers=1 PrependPath=1
    echo python should be installed now
) else (
    echo Python is installed, version below
    python --version
)
