# Errox_CMD

### Current Version:

Version: 2.0

(dont ask about 1.0)

## Basic coverage:

Errox_CMD is a collection of batch scripts designed to collect basic system information, escalate privileges, and act as a shell for cmd.exe.

## How Errox_CMD works:

### main.bat:
  
  Runs GatherSystemInfo.bat, BatchTerminal.bat, and InstallPython.bat
  
### GatherSystemInfo.bat:
  As in the name, this script is designed to gather system information like network connectsions and users on the device (for an example of the data collected, check below). Collected data is sent into files named .hotfixes.txt, .route.txt and so on. While the data is held inside of a cleartext within the .txt files, future updates will have the ability to encrypt the data using an XOR operation for basic obfuscation and bypass Windows Defender.

  Example data of the .all_groups.txt file:

    Aliases for \\<DEVICE_NAME>

    -------------------------------------------------------------------------------
    *Administrators
    *Device Owners
    *Distributed COM Users
    *Event Log Readers
    *Guests
    *Hyper-V Administrators
    *IIS_IUSRS
    *Performance Log Users
    *Performance Monitor Users
    *Remote Management Users
    *System Managed Accounts Group
    *Users
    The command completed successfully.

### BatchTerminal.bat:
  
  This file is designed to bypass the blockage of cmd.exe through the abilies that batch scripting has. It takes in a command, then executing it directly within the same process. While crude, the job gets done.

  Example of BatchTerminal.bat being executed via main.bat after GatherSystemInfo.bat has ran:

     _____                        ____ __  __ ____
    | ____|_ __ _ __ _____  __   / ___|  \/  |  _ \
    |  _| | '__| '__/ _ \ \/ /  | |   | |\/| | | | |
    | |___| |  | | | (_) >  <   | |___| |  | | |_| |
    |_____|_|  |_|  \___/_/\_\___\____|_|  |_|____/
                            |_____|
    
                         Created By: That1EthicalHacker
                                           Version: 2.0
    
    Starting a gather of information for a lay of the land
    Getting: Defender status and information
    Getting: App Locker settings
    Getting: If cmd.exe is avalable
    Getting: System info
    Getting: Hotfixes
    Getting: Software versions
    Getting: Routing table
    Getting: Current connections:
    Getting: IP table
    'query' is not recognized as an internal or external command,
    operable program or batch file.
    Getting: Current logged in users via query
    Getting: Current user '<USERNAME>' perms
    Getting: All users
    Getting: All groups
    Getting: Password policy and other info
    <USERNAME>@C:\Users\<USERNAME>\Desktop\Errox_CMD> echo This is a working test
    This is a working test
    <USERNAME>@C:\Users\<USERNAME>\Desktop\Errox_CMD>

### InstallPython.bat:

  This file is designed to try and install Python version 3.12.4, it doesnt check to see if Python has been installed but I am working on that currently.

## Usage:

  First you have to get the collection of scripts onto the target system. Once the files are on (or an installer file) run the installer file if you have one, then the main.bat file. Finnaly, sit back and let the script do its thing!
