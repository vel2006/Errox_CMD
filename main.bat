@echo off
title Errox_CMD
echo  _____                        ____ __  __ ____  
echo ^| ____^|_ __ _ __ _____  __   / ___^|  \/  ^|  _ \ 
echo ^|  _^| ^| '__^| '__/ _ \ \/ /  ^| ^|   ^| ^|\/^| ^| ^| ^| ^|
echo ^| ^|___^| ^|  ^| ^| ^| (_) ^>  ^<   ^| ^|___^| ^|  ^| ^| ^|_^| ^|
echo ^|_____^|_^|  ^|_^|  \___/_/\_\___\____^|_^|  ^|_^|____/ 
echo                         ^|_____^|
echo.
echo                      Created By: That1EthicalHacker
echo                                        Version: 2.1
echo.
:: Starting basic info grabbing for a lay of the land
echo Starting a gather of information for a lay of the land
call GatherSystemInfo.bat
echo Running InstallPython.bat script
call InstallPython.bat
echo Starting a batch shell to bypass a block of cmd.exe
call BatchTerminal.bat
