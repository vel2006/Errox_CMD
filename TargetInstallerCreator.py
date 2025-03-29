import os
class LayOfTheLandCommands():
    def ReadFileContents(self, file_path:str, as_list:bool):
        with open(file_path, 'r') as file:
            if as_list is True:
                response = []
                for line in file:
                    response.append(f'{line.strip()}\\n')
                return response
            return file.read().strip()
    def __init__(self):
        print("[i] Loading modules...")
        self.modules = {}
        directories_to_read = {
            'src/batch/commands/cmd/':'cmd',
            'src/batch/commands/powershell/':'powershell',
            'src/batch/commands/netsh/':'netsh'
        }
        self.AddModules(directories_to_read)
    def HasMicroModules(self, parent_module:str, child_module:str) -> bool:
        if [parent_module, child_module] in self.GetModulesAndSubs():
            return self.modules[parent_module][child_module]['has_micro']['state']
        return False
    def GetModules(self) -> list:
        return list(self.modules.keys())
    def GetModulesAndSubs(self) -> list:
        modules = []
        for module in self.modules.keys():
            for sub_module in self.modules[module]:
                if sub_module != 'description':
                    modules.append([module, sub_module])
        return list(modules)
    def AddModules(self, directories_to_read:dict):
        # Reading the folders and files that hold the commands
        base_dir = os.getcwd()
        self.modules = {}
        for dir, module in directories_to_read.items():
            os.chdir(dir)
            self.modules[module] = {}
            self.modules[module]['description'] = self.ReadFileContents('description.txt', False)
            for item in os.listdir():
                if os.path.isdir(item):
                    os.chdir(item)
                    self.modules[module][item] = {'description':self.ReadFileContents('description.txt', False)}
                    self.modules[module][item]['modules'] = {}
                    for file in os.listdir():
                        if os.path.isfile(file):
                            if file != "description.txt":
                                self.modules[module][item]['has_micro'] = {'state':True}
                                file_name, _ = os.path.splitext(file)
                                self.modules[module][item]['modules'][file_name] = self.ReadFileContents(file, True)
                    os.chdir(base_dir)
                    os.chdir(dir)
            os.chdir(base_dir)
    def GetModule(self, parent_module:str):
        if parent_module in self.GetModules():
            return list(self.modules[parent_module])
        else:
            return [f"[!] Error: \'{parent_module}\' not in loaded modules."]
    def RemoveModule(self, parent_module:str):
        if parent_module in self.GetModules():
            _ = self.modules.pop(parent_module)
        else:
            return f"[!] Error: \'{parent_module}\' not in loaded modules."
    def GetChildModules(self, parent_module:str):
        if parent_module in self.GetModules():
            return list(self.modules[parent_module].keys())
        return f"[!] Error: \'{parent_module}\' not in loaded modules."
    def RemoveChildModule(self, parent_module:str, child_module:str):
        if [parent_module, child_module] in self.GetModulesAndSubs():
            _ = self.modules[parent_module].pop(child_module)
        else:
            return f"[!] Error: \'{parent_module}/{child_module}\' not in loaded modules."
    def GetChildLines(self, parent_module:str, child_module:str):
        if [parent_module, child_module] in self.GetModulesAndSubs():
            _, lines = self.modules[parent_module][child_module].items()
            return lines
        return f"[!] Error: \'{parent_module}/{child_module}\' not in loaded modules."
    def GetMinorModules(self, parent_module:str, child_module:str):
        if [parent_module, child_module] in self.GetModulesAndSubs():
            return self.modules[parent_module][child_module]['modules'].keys()
        return f"[!] Module \'{parent_module}/{child_module}\' not in loaded modules."
    def RemoveMinorModules(self, parent_module:str, child_module:str, minor_module:str):
        if [parent_module, child_module] in self.GetModulesAndSubs() and minor_module in self.GetMinorModules(parent_module, child_module):
            _ = self.modules[parent_module][child_module]['modules'].pop(minor_module)
        else:
            return f"[!] Module \'{parent_module}/{child_module}/{minor_module}\' not in loaded modules."
    def GetMinorLines(self, parent_module:str, child_module:str, minor_module:str):
        if [parent_module, child_module] in self.GetModulesAndSubs() and minor_module in self.GetMinorModules(parent_module, child_module):
            lines = self.modules[parent_module][child_module]['modules'][minor_module]
            return lines
        return f"[!] Module \'{parent_module}/{child_module}/{minor_module}\' not in loaded modules."
# Creating the shell file, it's what's used as a way to bypass the blockage of CMD without having to use shellcode injection
def ShellScript_Creation(target_language:str, parent_language_c:bool):
    allowed_languages = ('batch', 'python')
    target_language = target_language.strip().lower()
    if target_language not in allowed_languages:
        return '\'target_language\' has to be one of the following: \'batch\', \'python\''
    print("[#] Creating shell script...")
    match target_language:
        case 'batch':
            if parent_language_c is True:
                print("[#] Shell script created.")
                return "@echo off\\n:loop\\nset cdir=%%CD%%\\nset /p usr_cmd=\\\"%%cdir%%> \\\"\\n%%usr_cmd%%\\ngoto loop\\necho Somehow exited the main loop\\npause\\n"
            print("[#] Shell script created.")
            return "@echo off\\n:loop\\nset cdir=%CD%\\nset /p usr_cmd=\\\"%cdir%> \\\"\\n%usr_cmd%\\ngoto loop\\necho Somehow exited the main loop\\npause\\n"
        case 'python':
            return_code = "import subprocess\\nimport threading\\nimport queue\\nimport time\\n\\nclass Shell():\\n\\tdef __init__(self):\\n\\t\\t"
            return_code += "print(\\\"[#] Starting shell...\\\")\\n\\t\\tself.cmd_shell = subprocess.Popen(\\n\\t\\t\\t[\\\'cmd\\\'],\\n\\t\\t\\tstdin=subprocess.PIPE,\\n\\t\\t\\t"
            return_code += "stdout=subprocess.PIPE,\\n\\t\\t\\tstderr=subprocess.PIPE,\\n\\t\\t\\ttext=True,\\n\\t\\t\\tbufsize=1\\n\\t\\t)\\n\\t\\tself.timeout_buffer = 2\\n\\t\\tself.output_queue = queue.Queue()\\n\\t\\t"
            return_code += "self.read_shell_handle = threading.Thread(target=self.read_shell, args=(self.cmd_shell, self.output_queue))\\n\\t\\tself.read_shell_handle.start()\\n\\t\\tprint(\\\"[#] Shell started!\\\")\\n\\t"
            return_code += "def read_shell(self, process_handle, output_queue):\\n\\t\\tfor line in iter(process_handle.stdout.readline, \\\'\\\'):\\n\\t\\t\\toutput_queue.put(line)\\n\\t\\t"
            return_code += "process_handle.stdout.close()\\n\\tdef execute_command(self, command:str):\\n\\t\\tself.cmd_shell.stdin.write(command.strip() + \\\'\\\\n\\\')\\n\\t\\tself.cmd_shell.stdin.flush()\\n\\t\\t"
            return_code += "time.sleep(self.timeout_buffer)\\n\\t\\toutput_data = []\\n\\t\\twhile not self.output_queue.empty():\\n\\t\\t\\toutput_data.append(self.output_queue.get())\\n\\t\\t"
            return_code += "response = \\'\\'.join(output_data).strip()\\n\\t\\tif response:\\n\\t\\t\\treturn response\\n\\t\\treturn \\\'[!] Command had no response.\\\\n[!] Likely due to cmd.exe process ending or never started.\\\'\\n\\t"
            return_code += "def close_shell(self):\\n\\t\\tself.execute_command(\\\'exit\\\')\\n\\t\\tself.read_shell_handle.join()\\nshell = Shell()\\nwhile True:\\n\\tprint(\\\"[*] Input command to execute.\\\\n[i] Type \\\\'EnD\\\\' to end the program.\\\")\\n\\t"
            return_code += "user_command = input(\\\">\\\")\\n\\tif user_command.strip() == \\\'EnD\\\':\\n\\t\\tshell.close_shell()\\n\\t\\tbreak\\n\\tresponse = shell.execute_command(user_command)\\n\\tprint(response)"
            print("[#] Shell script created")
            return return_code
# Creating the installer file, can be different languages and calls the 'LayOfTheLand_File_Creation' method
def InstallerScript_Creation(target_language:str, target_lines:list):
    print("[i] Creating installer file, if needs to be compiled (installer.c) will have to be compiled for windows.")
    match target_language.lower():
        case 'c':
            with open('installer.c', 'w') as installer_file:
                installer_file.write("#include <windows.h>\n#include <stdio.h>\n#include <stdlib.h>\nint main()\n{\n\t")
                installer_file.write("FILE *fptr = fopen(\"created.bat\", \"w\");\n\tfprintf(fptr, \"@echo off\\n\");\n\t")
                for line in target_lines:
                    for command in line:
                        installer_file.write(f"fprintf(fptr, \"set var={command}%%var%%>>\\\".output1423.txt\\\"\\n\");\n\t")
                installer_file.write("fclose(fptr);\n\t")
                print("[#] What language shall the shell be written in? (python, batch)")
                shell_language = input(">")
                match shell_language:
                    case 'python':
                        installer_file.write(f"fptr = fopen(\"shell.py\", \"w\");\n\tfprintf(fptr, \"{ShellScript_Creation('python', True)}\");\n\tfclose(fptr);\n\t")
                        installer_file.write("printf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\t")
                        installer_file.write("printf(\"[#] Starting local shell...\\n\");\n\tsystem(\"python .\\\\shell.py\");\n\treturn 0;\n}")
                        installer_file.close()
                    case 'batch':
                        installer_file.write(f"fptr = fopen(\"shell.bat\", \"w\");\n\tfprintf(fptr, \"{ShellScript_Creation('batch', True)}\");\n\tfclose(fptr);\n\t")
                        installer_file.write("printf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\t")
                        installer_file.write("printf(\"[#] Starting local shell...\\n\");\n\tsystem(\".\\\\shell.bat\");\n\treturn 0;\n}")
                        installer_file.close()
                    case _:
                        print("[!] Error: incorrect shell language, defaulting to batch.")
                        installer_file.write(f"fptr = fopen(\"shell.bat\", \"w\");\n\tfprintf(fptr, \"{ShellScript_Creation('batch', True)}\");\n\tfclose(fptr);\n\t")
                        installer_file.write("printf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\t")
                        installer_file.write("printf(\"[#] Starting local shell...\\n\");\n\tsystem(\".\\\\shell.bat\");\n\treturn 0;\n}")
                        installer_file.close()
        case 'python':
            with open('installer.py', 'w') as installer_file:
                installer_file.write("import os\nwith open(\"created.bat\", \"w\") as file:\n\tfile.write(\"@echo off\\n\")\n")
                for line in target_lines:
                    for command in line:
                        installer_file.write(f"\tfile.write(\"set var={command}%var%>>\\\".output1423.txt\\\"\\n\")\n")
                installer_file.write("file.close()\n")
                print("[#] What language shall the shell be written in? (python, batch)")
                shell_language = input(">")
                match shell_language:
                    case 'python':
                        installer_file.write(f"with open(\"shell.py\", \"w\") as file:\n\tfile.write(\"{ShellScript_Creation('python', False)}\")\n\tfile.close()\n")
                        installer_file.write("print(\"[#] collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting local shell...\")\n")
                        installer_file.write("os.system(\"python .\\\\shell.py\")")
                        installer_file.close()
                    case 'batch':
                        installer_file.write(f"with open(\"shell.bat\", \"w\") as file:\n\tfile.write(\"{ShellScript_Creation('batch', False)}\")\n\tfile.close()\n")
                        installer_file.write("print(\"[#] collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting local shell...\")\n")
                        installer_file.write("os.system(\".\\\\shell.bat\")")
                        installer_file.close()
                    case _:
                        print("[!] Error: incorrect shell language, defaulting to batch.")
                        installer_file.write(f"with open(\"shell.bat\", \"w\") as file:\n\tfile.write(\"{ShellScript_Creation('batch', False)}\")\n\tfile.close()\n")
                        installer_file.write("print(\"[#] collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting local shell...\")\n")
                        installer_file.write("os.system(\".\\\\shell.bat\")")
                        installer_file.close()
    print("[#] Installer file created.")
    return "worked"
print(" _____                        ____ __  __ ____  \n| ____|_ __ _ __ _____  __   / ___|  \\/  |  _ \\ ")
print("|  _| | '__| '__/ _ \\ \\/ /  | |   | |\\/| | | | |\n| |___| |  | | | (_) >  <   | |___| |  | | |_| |")
print("|_____|_|  |_|  \\___/_/\\_\\___\\____|_|  |_|____/ \n                        |_____|")
print("                    Created by: That1EthicalHacker\n                       Version: 3.7")
lol_creator = LayOfTheLandCommands()
while True:
    command_lines = []
    while True:
        allowed_modules = lol_creator.GetModules()
        print(f"Please enter the module you wish to get a command from.\n{allowed_modules}\nType \'end\' to continue with script generation.")
        mod = input(">").strip()
        if mod == 'end':
            break
        if mod in allowed_modules:
            while True:
                subs = lol_creator.GetChildModules(mod)
                print(f"Please select a sub module.\n{subs}\nType \'end\' to return to module selection.")
                sub = input(">").strip()
                if sub == 'end':
                    break
                if sub == 'description':
                    print(lol_creator.GetChildLines(mod, 'description'))
                if sub in subs:
                    if lol_creator.HasMicroModules(mod, sub):
                        while True:
                            micros = lol_creator.GetMinorModules(mod, sub)
                            if micros.__len__() == 0:
                                print(f"[i] All minor modules selected, removing sub module.")
                                lol_creator.RemoveChildModule(mod, sub)
                                break
                            print(f"Please select a minor module.\n{micros}\nType \'end\' tp return to mico module selection.")
                            micro = input(">").strip()
                            if micro == 'end':
                                break
                            if micro == 'description':
                                print(lol_creator.GetMinorLines(mod, sub, micro))
                            else:
                                if micro in micros:
                                    command_lines.append(lol_creator.GetMinorLines(mod, sub, micro))
                                    lol_creator.RemoveMinorModules(mod, sub, micro)
                                else:
                                    print(f"[!] Error, minor \'{micro}\' not in loaded minor modules.\nPlease try again.")
                    else:
                        command_lines.append(lol_creator.GetChildLines(mod, sub))
                        lol_creator.RemoveChildModule(mod, sub)
                else:
                    print(f"[!] Error, child module \'{sub}\' not in loaded child modules.\nPlease try again.")
        else:
            print(f"[!] Error, module \'{mod}\' not in loaded modules.\nPlease try again.")
    user_choice = ""
    while True:
        print("[i] Please input the language the installer file will be made in;\n\tC\n\tPython")
        user_choice = input(">").lower().strip()
        if user_choice not in ('c', 'python'):
            print("[!] Error: unknown selection of installer file.")
        else:
            break
    output = InstallerScript_Creation(user_choice, command_lines)
    if output != "worked":
        print("[!] Encountered error while creating Installer script!\n[i] Please report as an issue and try again :3")
    break
print("Thanks for using Errox_CMD, please check out the author at \'https://github.com/vel2006\'")
print(" _____ _ _____ _   _ ")
print("|_   _/ | ____| | | |")
print("  | | | |  _| | |_| |")
print("  | | | | |___|  _  |")
print("  |_| |_|_____|_| |_|")
