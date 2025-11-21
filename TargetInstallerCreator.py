import copy
import json
import os

# Script wide variables
IMPT_HEAD = "[#] "
INFO_HEAD = "[I] "
MISC_HEAD = "[*] "
EROR_HEAD = "[!] "
ALLOWED_SHELL_LANGUAGES = ["python", "batch"]
ALLOWED_INSTALLER_LANGUAGES = ["c", "python"]

# Script wide functions
def close_script():
    exit()

def create_shell(shell_language: str, installer_language: str):
    output = ""
    parsed_languages = ["c"]
    match shell_language:
        case 'batch':
            if installer_language in parsed_languages:
                print("[#] Shell script created.")
                output = "@echo off\\n:loop\\nset cdir=%%CD%%\\nset /p usr_cmd=\\\"%%cdir%%> \\\"\\n%%usr_cmd%%\\ngoto loop\\necho Somehow exited the main loop\\npause\\n"
            output = "@echo off\\n:loop\\nset cdir=%CD%\\nset /p usr_cmd=\\\"%cdir%> \\\"\\n%usr_cmd%\\ngoto loop\\necho Somehow exited the main loop\\npause\\n"
        case 'python':
            output = "import subprocess\\nimport threading\\nimport queue\\nimport time\\n\\nclass Shell():\\n\\tdef __init__(self):\\n\\t\\t"
            output += "print(\\\"[#] Starting shell...\\\")\\n\\t\\tself.cmd_shell = subprocess.Popen(\\n\\t\\t\\t[\\\'cmd\\\'],\\n\\t\\t\\tstdin=subprocess.PIPE,\\n\\t\\t\\t"
            output += "stdout=subprocess.PIPE,\\n\\t\\t\\tstderr=subprocess.PIPE,\\n\\t\\t\\ttext=True,\\n\\t\\t\\tbufsize=1\\n\\t\\t)\\n\\t\\tself.timeout_buffer = 2\\n\\t\\tself.output_queue = queue.Queue()\\n\\t\\t"
            output += "self.read_shell_handle = threading.Thread(target=self.read_shell, args=(self.cmd_shell, self.output_queue))\\n\\t\\tself.read_shell_handle.start()\\n\\t\\tprint(\\\"[#] Shell started!\\\")\\n\\t"
            output += "def read_shell(self, process_handle, output_queue):\\n\\t\\tfor line in iter(process_handle.stdout.readline, \\\'\\\'):\\n\\t\\t\\toutput_queue.put(line)\\n\\t\\t"
            output += "process_handle.stdout.close()\\n\\tdef execute_command(self, command:str):\\n\\t\\tself.cmd_shell.stdin.write(command.strip() + \\\'\\\\n\\\')\\n\\t\\tself.cmd_shell.stdin.flush()\\n\\t\\t"
            output += "time.sleep(self.timeout_buffer)\\n\\t\\toutput_data = []\\n\\t\\twhile not self.output_queue.empty():\\n\\t\\t\\toutput_data.append(self.output_queue.get())\\n\\t\\t"
            output += "response = \\'\\'.join(output_data).strip()\\n\\t\\tif response:\\n\\t\\t\\treturn response\\n\\t\\treturn \\\'[!] Command had no response.\\\\n[!] Likely due to cmd.exe process ending or never started.\\\'\\n\\t"
            output += "def close_shell(self):\\n\\t\\tself.execute_command(\\\'exit\\\')\\n\\t\\tself.read_shell_handle.join()\\nshell = Shell()\\nwhile True:\\n\\tprint(\\\"[*] Input command to execute.\\\\n[i] Type \\\\'EnD\\\\' to end the program.\\\")\\n\\t"
            output += "user_command = input(\\\">\\\")\\n\\tif user_command.strip() == \\\'EnD\\\':\\n\\t\\tshell.close_shell()\\n\\t\\tbreak\\n\\tresponse = shell.execute_command(user_command)\\n\\tprint(response)"
    return output

# Creating the installer
def create_installer(installer_language: str, shell_language: str, modules_to_add: list[str]) -> str:
    output = ""
    # We have it formatted like this because instead of having four different match statements it is compressed into two
    match installer_language:
        case "c":
            output += "#include <windows.h>\n#include <stdio.h>\n#include <stdlib.h>\nint main()\n{\n\t"
            output += "FILE *fptr = fopen(\"created.bat\", \"w\");\n\tfprintf(fptr, \"@echo off\\n\");\n\t"
            for module in modules_to_add:
                output += f"fprintf(fptr, \"set var={module}%%var%%>>\\\".output1423.txt\\\"\\n\");\n\t"
            output += "fclose(fptr);\n\t"
            match shell_language:
                case "python":
                    output += f"fptr = fopen(\"shell.py\", \"w\");\n\tfprintf(fptr, \"{create_shell('python', 'c')}\");\n\tfclose(fptr);\n\t"
                    output += "printf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\t"
                    output += "printf(\"[#] Starting local shell...\\n\");\n\tsystem(\"python .\\\\shell.py\");\n\treturn 0;\n}"
                case "batch":
                    output += f"fptr = fopen(\"shell.bat\", \"w\");\n\tfprintf(fptr, \"{create_shell('batch', 'c')}\");\n\tfclose(fptr);\n\t"
                    output += "printf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\t"
                    output += "printf(\"[#] Starting local shell...\\n\");\n\tsystem(\".\\\\shell.bat\");\n\treturn 0;\n}"
        case "python":
            output += "import os\nwith open(\"created.bat\", \"w\") as file:\n\tfile.write(\"@echo off\\n\")\n"
            for module in modules_to_add:
                output += f"\tfile.write(\"set var={module}%var%>>\\\".output1423.txt\\\"\\n\")\n"
            match shell_language:
                case "python":
                    output += f"with open(\"shell.py\", \"w\") as file:\n\tfile.write(\"{create_shell('python', 'python')}\")\n\tfile.close()\n"
                    output += "print(\"[#] collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting local shell...\")\n"
                    output += "os.system(\"python .\\\\shell.py\")"
                case "batch":
                    output += f"with open(\"shell.bat\", \"w\") as file:\n\tfile.write(\"{create_shell('batch', 'python')}\")\n\tfile.close()\n"
                    output += "print(\"[#] collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting local shell...\")\n"
                    output += "os.system(\".\\\\shell.bat\")"
    return output

# Import modules
class HandleModules():
    def load_module(module_path: str) -> list[str, dict] | list[None, None]:
        data = {}
        try:
            with open(module_path, "r") as file_handle:
                data = json.load(file_handle)
                file_handle.close()
        except Exception as error:
            print(f"{EROR_HEAD}Failed to read module path \"{module_path}\" with error \'{error}\'")
            return [None, None]
        return data
    def create_module():
        # This is designed to be small and not include all of the "base" modules to have a smaller file
        data = {
            "cmd": {
                "system information": {
                    "description": "Commands to get high level information about the system",
                    "commands": [
                        "hostname",
                        "ver",
                        "systeminfo",
                        "driverquery /v"
                    ]
                },
                "user information": {
                    "description": "Commands to get high level current user information",
                    "commands": [
                        "whoami /all",
                        "whoami /priv",
                        "whoami /groups",
                        "net user",
                        "net localgroup",
                        "net localgroup administrators",
                        "query user"
                    ]
                },
                "networking basic": {
                    "description": "Commands to get high level networking information",
                    "commands": [
                        "ipconfig /all",
                        "netstat -ano",
                        "arp -a",
                        "route print",
                        "tracert 8.8.8.8"
                    ]
                }
            },
            "powershell": {
                "system information": {
                    "description": "Commands to get high level information about the system",
                    "commands": [
                        "powershell -Command \"Get-ComputerInfo\"",
                        "powershell -Command \"Get-HotFix\""
                    ]
                },
                "user permissions": {
                    "description": "Commands to get current user permissions",
                    "commands": [
                        "powershell -Command \"Get-LocalUser\"",
                        "powershell -Command \"GetLocalGroupMember -Group Administrators\"",
                        "powershell -Command \"Get-Acl -Path C:\\Windows\""
                    ]
                }
            }
        }
        try:
            with open(f"modules.json", "w") as file_handle:
                json.dump(data, file_handle)
                file_handle.close()
        except Exception as error:
            print(f"{EROR_HEAD}Failed to write module \"modules.json\" as error \'{error}\'")
    def __init__() -> dict:
        modules = {}
        # Create modules if not existing
        if os.path.exists("modules.json"):
            modules = HandleModules.load_module("modules.json")
        else:
            print(f"{INFO_HEAD}File holding modules does not exist, creating base modules...")
            modules_to_create = ["cmd", "powershell"]
            for module in modules_to_create:
                print(f"{MISC_HEAD}Creating module \'{module}\'...")
                HandleModules.create_module()
        if modules == {}:
            print(f"{EROR_HEAD}Failed to read all modules, exiting.")
            close_script()
        print(f"{INFO_HEAD}All modules loaded!")
        return modules
    def select_modules(loaded_modules: list[str]) -> list[str]:
        allowed_modules = copy.copy(loaded_modules)
        output = []
        while True:
            print(f"{INFO_HEAD}Please select from these modules which one you wish to use; {allowed_modules.keys()}")
            print(f"{MISC_HEAD}Type \"EnD\" to create installer program or go back one module.")
            choice = input(">").rstrip("\n")
            if choice in allowed_modules:
                if choice == "description":
                    print(f"{INFO_HEAD}description: {allowed_modules[choice]}\n")
                elif choice == "commands":
                    output += allowed_modules[choice]
                    return output
                elif type(allowed_modules[choice]) == dict:
                    selected = HandleModules.select_modules(allowed_modules[choice])
                    if allowed_modules[choice] == {} or allowed_modules[choice].keys() == ["description", "commands"]:
                        del allowed_modules[choice]
                    output += selected
                else:
                    print(f"{EROR_HEAD}Selection \'{choice}\' does not exist.")
            elif choice == "EnD":
                break
        return output
if __name__ == "__main__":
    print(" _____                        ____ __  __ ____  \n| ____|_ __ _ __ _____  __   / ___|  \\/  |  _ \\ ")
    print("|  _| | '__| '__/ _ \\ \\/ /  | |   | |\\/| | | | |\n| |___| |  | | | (_) >  <   | |___| |  | | |_| |")
    print("|_____|_|  |_|  \\___/_/\\_\\___\\____|_|  |_|____/ \n                        |_____|")
    print("                    Created by: That1EthicalHacker\n                       Version: 4.0")
    # Get wanted modules
    modules = HandleModules.__init__()
    selected_modules = HandleModules.select_modules(modules)
    installer_code = create_installer("python", "batch", selected_modules)
    with open("installer.py", "w") as file_handle:
        file_handle.write(installer_code)
        file_handle.close()
