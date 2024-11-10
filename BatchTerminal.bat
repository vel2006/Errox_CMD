@echo off
:loop
set cdir=%CD%
set /p usr_cmd="%cdir%> "
%usr_cmd%
goto loop
echo Somehow exited the main loop
pause
