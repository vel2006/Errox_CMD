@echo off
:loop
set cdir=%CD%
ser usr=%USERNAME%
set /p usr_cmd="%usr%@%cdir%> "
%usr_cmd%
set usr_cmd=" "
goto loop
echo Somehow exited the main loop
pause
