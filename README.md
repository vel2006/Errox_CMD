# Errox_CMD

### Current Version:

Version: 4.0

(dont ask about 1.0)

## Basic coverage:

Errox_CMD is a collection of scripts designed to collect basic system information, (eventually) escalate privileges, and act as a shell for cmd.exe.

## How Errox_CMD works:

### TargetInstallerCreator.py

TargetInstallerCreator.py is used to create the installer file that would be used on the target system. It works by getting the wanted modules and programming language for the installer. The modules are loaded and held within a json file allowing for customizability by the user and future update maintainability. Once all of the modules are gotten the installer file is created and dropped to disk.

  ### Batch shell:

  Works by abusing how Batch is the same language used to make cmd.exe work, meaning that the user can input the same commands as they would in a user created instance of cmd. This also means that it bypasses the blocking of a user creating a cmd process.

  ### Python shell:

  Works by calling cmd.exe through subprocess (has not been tested for bypassing the blockage of cmd.exe yet) and constantly reading it's output, meaning that the process never closes or halts. While a crude method, it does work. The input is then fed into the subprocess input, executed, then read due to the constant reading of the process. While, this can be detected by it's long cmd.exe process, it does pass any pure file scan.

## Out dated information:

### Version 3.7

  Version 3.7 brought changes to how the dictionary is handled inside of TargetInstallerCreator.py. Instead of using a static dictionary of commands, anyone can now simply edit the contents of each directory holding commands, and even add their own! This allows for the script to be more versatile and change on the fly with each user's needs.


### Version 2

#### Installer.bat

  Installer.bat is the first installer file for Errox_CMD. You simply need to recreate or run this file on the device you wish to have Errox_CMD on and BAM there it is, however this file does depend NOT on github being blocked on the network that the device running Installer.bat is on. This is due to Installer.bat testing to see if a connection page is up and responding, if it is then Installer.bat will install all other files through web requests. If the page is not reachable or doesnt respond, then Installer.bat will create the hard coded in versions inside of itself through base64.
  
  Example of Installer.bat running with no internet connection:
  
    Testing if GitHub repo is reachable...
    GitHub not reachable, creating via base64...
    Creating GatherSystemInfo script...
    Creating BatchTerminal script...
    Creating InstallPython script...
    Creating Main script...
    Install Script ended, run main.bat for Errox_CMD              

  Example of Installer.bat running with GitHub reachable:

    Testing if GitHub repo is reachable...
    GitHub is reachable, creating via download...
    Getting GatherSystemInfo script...
    Getting BatchTerminal script...
    Getting InstallPython script...
    Getting Main script...
    Install Script ended, run main.bat for Errox_CMD

#### main.bat:
  
  Runs GatherSystemInfo.bat, BatchTerminal.bat, and InstallPython.bat. It is the script that runs all of the other files, its not a needed file and is only here for automation and convenience.

  Example of main.bat running:

     _____                        ____ __  __ ____
    | ____|_ __ _ __ _____  __   / ___|  \/  |  _ \
    |  _| | '__| '__/ _ \ \/ /  | |   | |\/| | | | |
    | |___| |  | | | (_) >  <   | |___| |  | | |_| |
    |_____|_|  |_|  \___/_/\_\___\____|_|  |_|____/
                            |_____|
    
                         Created By: That1EthicalHacker
                                           Version: 2.1
    
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
    Running InstallPython.bat script
    Seeing if python is installed
    Python is installed, version below
    Python 3.12.4
    Starting a batch shell to bypass a block of cmd.exe
    <USERNAME>@C:\Users\<USERNAME>\Downloads>
  
#### GatherSystemInfo.bat:
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

#### BatchTerminal.bat:
  
  This file is designed to bypass the blockage of cmd.exe through the abilies that batch scripting has. It takes in a command, then executing it directly within the same process. While crude, the job gets done.

  Example of BatchTerminal.bat being executed via main.bat after GatherSystemInfo.bat has ran:

     _____                        ____ __  __ ____
    | ____|_ __ _ __ _____  __   / ___|  \/  |  _ \
    |  _| | '__| '__/ _ \ \/ /  | |   | |\/| | | | |
    | |___| |  | | | (_) >  <   | |___| |  | | |_| |
    |_____|_|  |_|  \___/_/\_\___\____|_|  |_|____/
                            |_____|
    
                         Created By: That1EthicalHacker
                                           Version: 2.1
    
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
    Running InstallPython.bat script
    Seeing if python is installed
    Python is installed, version below
    Python 3.12.4
    Starting a batch shell to bypass a block of cmd.exe
    <USERNAME>@C:\Users\<USERNAME>\Downloads> echo I Love Errox_CMD :3
    I Love Errox_CMD :3
    <USERNAME>@C:\Users\<USERNAME>\Downloads>
  
#### InstallPython.bat:

  This file is designed to try and install Python version 3.12.4, it doesnt check to see if Python has been installed but I am working on that currently.

### Usage:

  First you have to get the collection of scripts onto the target system. Once the files are on (or an installer file) run the installer file if you have one, then the main.bat file. Finnaly, sit back and let the script do its thing!
