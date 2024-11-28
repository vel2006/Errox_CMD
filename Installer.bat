@echo off
powershell -Command "Invoke-WebRequest -Uri 'https://vel2006.github.io/Errox_CMD/GatherSystemInfo.bat' -OutFile 'GatherSystemInfo.bat'
powershell -Command "Invoke-WebRequest -Uri 'https://vel2006.github.io/Errox_CMD/BatchTerminal.bat' -OutFile 'BatchTerminal.bat'
powershell -Command "Invoke-WebRequest -Uri 'https://vel2006.github.io/Errox_CMD/InstallPython.bat' -OutFile 'InstallPython.bat'
powershell -Command "Invoke-WebRequest -Uri 'https://vel2006.github.io/Errox_CMD/main.bat' -OutFile 'main.bat'
