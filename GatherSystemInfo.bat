@echo off
set get_microsoft_defender_settings=powershell -Command "Get-MpComputerStatus"
%get_microsoft_defender_settings%>".defender_status.txt"
echo Getting: Defender status and information
set get_app_locker_settings=powershell -Command "Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollection"
%get_app_locker_settings%>".locker_rules.txt"
echo Getting: App Locker settings
set get_app_locker_cmd=powershell -Command "Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone"
%get_app_locker_cmd%>".cmd_avalib.txt"
echo Getting: If cmd.exe is avalable
set get_system_info=systeminfo
%get_system_info%>".system_info.txt"
echo Getting: System info
set get_hotfixes=wmic qfe
%get_hotfixes%>".hotfixes.txt"
echo Getting: Hotfixes
set get_software_versions=powershell -Command "GetWmiObject -Class Win32_Product | select Name, Version"
%get_software_versions%>".software_versions.txt"
echo Getting: Software versions
set get_route=route print
%get_route%>".route.txt"
echo Getting: Routing table
set get_connections=netstat -ano
%get_connections%>".connections.txt"
echo Getting: Current connections:
set get_ip_info=ipconfig /all
%get_ip_info%>".ipconfig.txt"
echo Getting: IP table
set get_users=query user
%get_users%>".current_users.txt"
echo Getting: Current logged in users via query
set get_current_perms=whoami /priv
%get_current_perms%>".current_perms.txt"
set get_current_perms=whoami /groups
%get_current_perms%>>".current_perms.txt"
set user=%USERNAME%
echo Getting: Current user '%user%' perms
set get_all_users=net user
%get_all_users%>".all_users.txt"
echo Getting: All users
set get_all_groups=net localgroup
%get_all_groups%>".all_groups.txt"
echo Getting: All groups
set get_password_policy=net accounts
%get_password_policy%>".password_policy.txt"
echo Getting: Password policy and other info
