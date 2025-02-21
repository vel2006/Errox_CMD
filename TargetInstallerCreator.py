def LayOfTheLand_Creation(tagret_modules:list):
    modules = {
        'netsh':{
            'description':'Network Shell interface commands.',
            'modules':{
                'advfirewall':{
                    'description':'A more advanced Windows firewall.',
                    'modules':{
                        'consec':(
                            'netsh advfirewall consec dump\\n',
                            'netsh advfirewall consec show rule name=all dir=in type=static\\n',
                            'netsh advfirewall consec show rule name=all dir=out type=static\\n',
                            'netsh advfirewall consec show rule name=all dir=in type=dynamic\\n',
                            'netsh advfirewall consec show rule name=all dir=out type=dynamic\\n'
                        ),
                        'dump':(
                            'netsh advfirewall dump\\n'
                        ),
                        'firewall':(
                            'netsh advfirewall firewall show rule name=all dir=in type=dynamic\\n', 
                            'netsh advfirewall firewall show rule name=all dir=in type=static\\n', 
                            'netsh advfirewall firewall show rule name=all dir=out type=dynamic\\n', 
                            'netsh advfirewall firewall show rule name=all dir=out type=static\\n'
                        ),
                        'mainmode':(
                            'netsh advfirewall mainmode dump\\n', 
                            'netsh advfirewall mainmode show rule=all dir=in type=static\\n', 
                            'netsh advfirewall mainmode show rule=all dir=out type=static\\n', 
                            'netsh advfirewall mainmode show rule=all dir=in type=dynamic\\n', 
                            'netsh advfirewall mainmode show rule=all dir=out type=dynamic\\n'
                        ),
                        'monitor':(
                            'netsh advfirewall monitor dump\\n', 
                            'netsh advfirewall monitor show consec\\n', 
                            'netsh advfirewall monitor show currentprofile\\n', 
                            'netsh advfirewall monitor show firewall\\n', 
                            'netsh advfirewall monitor show mainmode\\n', 
                            'netsh advfirewall monitor show mmsa\\n', 
                            'netsh advfirewall monitor show qmsa\\n'
                        ),
                        'show':(
                            'netsh advfirewall show allprofiles\\n', 
                            'netsh advfirewall show currentprofile\\n', 
                            'netsh advfirewall show domainprofile\\n', 
                            'netsh advfirewall show global\\n', 
                            'netsh advfirewall show privateprofile\\n', 
                            'netsh advfirewall show publicprofile\\n', 
                            'netsh advfirewall show store\\n'
                        )
                    }
                },
                'bridge':{
                    'description':'A bridge from one network adapter to another.',
                    'modules':{
                        'dump':(
                            'netsh bridge dump\\n'
                        ),
                        'show':(
                            'netsh bridge show adapter\\n'
                        )
                    }
                },
                'dnsclient':{
                    'description':'The client side of a device for the DNS protocol.',
                    'modules':{
                        'dump':(
                            'netsh dnsclient dump\\n'
                        ),
                        'show':(
                            'netsh dnsclient show encryption\\n',
                            'netsh dnsclient show global\\n',
                            'netsh dnsclient show state\\n'
                        )
                    }
                },
                'firewall':{
                    'description':'Windows firewall (think about it, if advfirewall is advanced, this must be basic.)',
                    'modules':{
                        'dump':(
                            'netsh firewall dump\\n'
                        ),
                    }
                },
                'http':{
                    'description':'Built in Windows HTTP server',
                    'modules':{
                        'dump':(
                            'netsh http dump\\n'
                        ),
                        'show':(
                            'netsh http show cacheparam\\n',
                            'netsh http show cachestate\\n',
                            'netsh http show iplisten\\n',
                            'netsh http show servicestate\\n',
                            'netsh http show setting\\n',
                            'netsh http show sslcert\\n',
                            'netsh http show timeout\\n',
                            'netsh http show urlacl\\n'
                        )
                    }
                },
                'interface':{
                    'description':'Device\'s network interfaces.',
                    'modules':{
                        '6to4':(
                            'netsh interface 6to4 dump\\n',
                            'netsh interface 6to4 show interface\\n',
                            'netsh interface 6to4 show relay\\n',
                            'netsh interface 6to4 show routing\\n',
                            'netsh interface 6to4 show state\\n'
                        ),
                        'dump':(
                            'netsh interface dump\\n'
                        ),
                        'fl48':(
                            'netsh interface fl48 dump\\n',
                            'netsh interface fl48 show virtualinterfaces\\n'
                        ),
                        'fl68':(
                            'netsh interface fl68 dump\\n',
                            'netsh interface fl68 show virtualinterfaces\\n'
                        ),
                        'htttpstunnel':(
                            'netsh interface httpstunnel dump\\n',
                            'netsh interface httpstunnel show interfaces\\n',
                            'netsh interface httpstunnel show statistics\\n'
                        ),
                        'ipv4':(
                            'netsh interface ipv4 dump\\n',
                            'netsh interface ipv4 show addresses\\n',
                            'netsh interface ipv4 show compartments\\n',
                            'netsh interface ipv4 show config\\n',
                            'netsh interface ipv4 show destinationcache\\n',
                            'netsh interface ipv4 show dnsservers\\n',
                            'netsh interface ipv4 show excludedportrange\\n',
                            'netsh interface ipv4 show global\\n',
                            'netsh interface ipv4 show icmpstats\\n',
                            'netsh interface ipv4 show interfaces\\n',
                            'netsh interface ipv4 show ipaddresses\\n',
                            'netsh interface ipv4 show ipnettomedia\\n',
                            'netsh interface ipv4 show ipstats\\n',
                            'netsh interface ipv4 show joins\\n',
                            'netsh interface ipv4 show neighbors\\n',
                            'netsh interface ipv4 show offload\\n',
                            'netsh interface ipv4 show route\\n',
                            'netsh interface ipv4 show subinterfaces\\n',
                            'netsh interface ipv4 show tcpconnections\\n',
                            'netsh interface ipv4 show tcpstats\\n',
                            'netsh interface ipv4 show udpconnections\\n',
                            'netsh interface ipv4 show udpstats\\n',
                            'netsh interface ipv4 show winsserver\\n'
                        ),
                        'ipv6':(
                            'netsh interface ipv6 dump\\n',
                            'netsh interface ipv6 show addresses\\n',
                            'netsh interface ipv6 show compartments\\n',
                            'netsh interface ipv6 show destinationcache\\n',
                            'netsh interface ipv6 show dnsservers\\n',
                            'netsh interface ipv6 show dynamicportange\\n',
                            'netsh interface ipv6 show excludedportrange\\n',
                            'netsh interface ipv6 show global\\n',
                            'netsh interface ipv6 show interfaces\\n',
                            'netsh interface ipv6 show ipstats\\n',
                            'netsh interface ipv6 show joins\\n',
                            'netsh interface ipv6 show neighbors\\n',
                            'netsh interface ipv6 show offload\\n',
                            'netsh interface ipv6 show potentialrouters\\n',
                            'netsh interface ipv6 show prefixpolicies\\n',
                            'netsh interface ipv6 show privacy\\n',
                            'netsh interface ipv6 show route\\n',
                            'netsh interface ipv6 show siteprefixes\\n',
                            'netsh interface ipv6 show slaacsecretkey\\n',
                            'netsh interface ipv6 show subinterfaces\\n',
                            'netsh interface ipv6 show tcpstats\\n',
                            'netsh interface ipv6 show teredo\\n',
                            'netsh interface ipv6 show tfofallback\\n',
                            'netsh interface ipv6 show udpstats\\n',
                            'netsh interface ipv6 6t04 dump\\n',
                            'netsh interface ipv6 6t04 show interface\\n',
                            'netsh interface ipv6 6t04 show relay\\n',
                            'netsh interface ipv6 6t04 show routing\\n',
                            'netsh interface ipv6 6t04 show state\\n'
                        ),
                        'isatap':(
                            'netsh interface isatap dump\\n',
                            'netsh interface isatap show mode\\n',
                            'netsh interface isatap show router\\n',
                            'netsh interface isatap show state\\n'
                        ),
                        'portproxy':(
                            'netsh interface portproxy dump\\n',
                            'netsh interface portproxy show all\\n'
                        ),
                        'tcp':(
                            'netsh interface tcp dump\\n',
                            'netsh interface tcp show mode\\n',
                            'netsh interface tcp show global\\n',
                            'netsh interface tcp show heuristics\\n',
                            'netsh interface tcp show rscstats\\n',
                            'netsh interface tcp show security\\n',
                            'netsh interface tcp show supplemental\\n',
                            'netsh interface tcp show supplementalports\\n',
                            'netsh interface tcp show supplementalsubnets\\n'
                        ),
                        'teredo':(
                            'netsh interface teredo dump\\n',
                            'netsh interface teredo show state\\n'
                        ),
                        'udp':(
                            'netsh interface udp dump\\n',
                            'netsh interface udp show global\\n'
                        ),
                        'show':(
                            'netsh interface show interface\\n'
                        )
                    }
                },
                'ipsec':{
                    'description':'Built in windows IP protocol security.',
                    'modules':{
                        'dump':(
                            'netsh ipsec dump\\n'
                        ),
                        'dynamic':(
                            'netsh ipsec dynamic dump\\n',
                            'netsh ipsec dynamic show config\\n',
                            'netsh ipsec dynamic show mmfilter\\n',
                            'netsh ipsec dynamic show mmpolicy\\n',
                            'netsh ipsec dynamic show mmsas\\n',
                            'netsh ipsec dynamic show qmfilter\\n',
                            'netsh ipsec dynamic show qmpolicy\\n',
                            'netsh ipsec dynamic show qmsas\\n',
                        ),
                        'static':(
                            'netsh ipsec static dump\\n',
                            'netsh ipsec static show filteraction\\n',
                            'netsh ipsec dynamic show filterlist\\n',
                            'netsh ipsec dynamic show gpoassignedpolicy\\n',
                            'netsh ipsec dynamic show policy\\n',
                            'netsh ipsec dynamic show store\\n',
                        )
                    }
                },
                'lan':{
                    'description':'Configurations for the LAN a device is connected to.',
                    'modules':{
                        'dump':(
                            'netsh lan dump\\n'
                        ),
                        'show':(
                            'netsh lan show interfaces\\n',
                            'netsh lan show profiles\\n',
                            'netsh lan show settings\\n',
                            'netsh lan show tracing\\n'
                        )
                    }
                },
                'mbn':{
                    'description':'Mobile broadcast network information. DOES NOT WORK AND IS A WORK IN PROGRESS!',
                    'modules':{
                        'dump':(
                        'netsh mbn dump\\n'
                        ),
                        'show':(
                            'netsh mbn show acstate\\n',
                            'netsh mbn show capatability\\n',
                            'netsh mbn show connection\\n',
                            'netsh mbn show d3cold\\n',
                            'netsh mbn show dataenablement\\n',
                            'netsh mbn show dataroamcontrol\\n',
                            'netsh mbn show dmprofiles\\n',
                            'netsh mbn show enterpriseapnparams\\n',
                            'netsh mbn show highestconncategory\\n',
                            'netsh mbn show homeprovider\\n',
                            'netsh mbn show interfaces\\n',
                            'netsh mbn show netlteattachinfo\\n',
                            'netsh mbn show pin\\n',
                            'netsh mbn show pinlist\\n',
                            'netsh mbn show preferredproviders\\n',
                            'netsh mbn show profiles\\n',
                            'netsh mbn show profilestate\\n',
                            'netsh mbn show provisionedcontexts\\n',
                            'netsh mbn show purpose\\n',
                            'netsh mbn show radio\\n',
                            'netsh mbn show readyinfo\\n',
                            'netsh mbn show signal\\n',
                            'netsh mbn show slotmapping\\n',
                            'netsh mbn show tracing\\n',
                            'netsh mbn show UICCCardAdditionalInfoWithEFHPLMNwAct\\n',
                            'netsh mbn show visibleproviders\\n'
                        )
                    }
                },
                'namespace':{
                    'description':'Windows device network current device is connected to.',
                    'modules':{
                        'dump':(
                            'netsh namespace dump\\n'
                        ),
                        'show':(
                            'netsh namespace show effectivepolicy\\n',
                            'netsh namespace show policy\\n'
                        )
                    }
                },
                'netio':{
                    'description':'Legacy \'interface\', used for handling network interfaces.',
                    'modules':{
                        'dump':(
                            'netsh netio dump\\n'
                        ),
                        'show':(
                            'netsh netio show bindingfilters\\n'
                        )
                    }
                },
                'nlm':{
                    'description':'Network level maintaince and authentication.',
                    'modules':{
                        'dump':(
                            'netsh nlm dump\\n'
                        ),
                        'enum':(
                            'netsh nlm enum connections\\n',
                            'netsh nlm enum networks\\n'
                        ),
                        'show':(
                            'netsh nlm show connectivity\\n',
                            'netsh nlm show cost\\n'
                        )
                    }
                },
                'ras':{
                    'description':'Remote access to servers.',
                    'modules':{
                        'aaaa':(
                            'netsh ras aaaa dump\\n',
                            'netsh ras aaaa show accounting\\n',
                            'netsh ras aaaa show acctserver\\n',
                            'netsh ras aaaa show authentication\\n',
                            'netsh ras aaaa show authserver\\n',
                            'netsh ras aaaa show ipsecpolicy\\n'
                        ),
                        'dump':(
                            'netsh ras dump\\n'
                        ),
                        'ip':(
                            'netsh ras ip dump\\n',
                            'netsh ras ip show config\\n',
                            'netsh ras ip show preferredadapter\\n',
                        ),
                        'ipv6':(
                            'netsh ras ipv6 dump\\n',
                            'netsh ras ipv6 show config\\n'
                        ),
                        'show':(
                            'netsh ras show activeservers\\n',
                            'netsh ras show authmode\\n',
                            'netsh ras show authtype\\n',
                            'netsh ras show client\\n',
                            'netsh ras show conf\\n',
                            'netsh ras show ikev2connection\\n',
                            'netsh ras show ikev2saexpiry\\n',
                            'netsh ras show link\\n',
                            'netsh ras show multilink\\n',
                            'netsh ras show portstatus\\n',
                            'netsh ras show registeredserver\\n',
                            'netsh ras show sstp-ssl-cert\\n',
                            'netsh ras show status\\n',
                            'netsh ras show type\\n',
                            'netsh ras show user\\n',
                            'netsh ras show wanports\\n'
                        )
                    }
                },
                'rpc':{
                    'description':'Remote Procedure System, used for running things on distrobuted systems as if it was being ran localy.',
                    'modules':{
                        'dump':(
                            'netsh rpc dump\\n'
                        ),
                        'filter':(
                            'netsh rpc filter dump\\n',
                            'netsh rpc filter show filter\\n',
                        )
                    }
                },
                'trace':{
                    'description':'Traceroute but windows.',
                    'modules':{
                        'modules':{
                            'dump':(
                                'netsh trace dump\\n'
                            ),
                            'show':(
                                'netsh trace show globalKeywordsAndLevels\\n',
                                'netsh trace show interfaces\\n',
                                'netsh trace show provider\\n',
                                'netsh trace show providers\\n',
                                'netsh trace show scenario\\n',
                                'netsh trace show scenarios\\n',
                                'netsh trace show status\\n'
                            )
                        }
                    }
                },
                'wcn':{
                    # Query not included due to it needing interfaces and SSIDs
                    'description':'Windows Connect Now information',
                    'modules':{
                        'dump':(
                            'netsh wcn dump\\n'
                        )
                    }
                },
                'wfp':{
                    'description':'Windows Filtering Platform information.',
                    'modules':{
                        'dump':(
                            'netsh wfp dump\\n'
                        ),
                        'show':(
                            # Appid not included due to it needing an appID
                            'netsh wfp show boottimepolicy\\n',
                            'netsh wfp show filters\\n',
                            'netsh wfp show ikeevents\\n',
                            'netsh wfp show netevents\\n',
                            'netsh wfp show options NETEVENTS\\n',
                            'netsh wfp show options KEYWORDS\\n',
                            'netsh wfp show options TXNWATCHDOG\\n',
                            'netsh wfp show security\\n',
                            'netsh wfp show state\\n',
                            'netsh wfp show sysports\\n'
                        )
                    }
                },
                'winhttp':{
                    'description':'Windows HTTP information',
                    'modules':{
                        'dump':(
                            'netsh winhttp dump\\n'
                        ),
                        'show':(
                            'netsh winhttp show advproxy\\n',
                            'netsh winhttp show proxy\\n',
                            'netsh winhttp show tracing\\n'
                        )
                    }
                },
                'winsock':{
                    'description':'Windows socket information.',
                    'modules':{
                        'audit':(
                            'netsh winsock audit\\n'
                        ),
                        'dump':(
                            'netsh winsock dump\\n'
                        ),
                        'show':(
                            'netsh winsock show autoruning\\n',
                            'netsh winsock show catalog\\n'
                        )
                    }
                },
                'wlan':{
                    'description':'wLAN information (Wireless LAN)',
                    'modules':{
                        'dump':(
                            'netsh wlan dump\\n'
                        ),
                        'reportissues':(
                            'netsh wlan reportissues\\n'
                        ),
                        'show':(
                            'netsh wlan show allowexplicitcreds\\n',
                            'netsh wlan show autoconfig\\n',
                            'netsh wlan show blockednetworks\\n',
                            'netsh wlan show createalluserprofile\\n',
                            'netsh wlan show drivers\\n',
                            'netsh wlan show filters\\n',
                            'netsh wlan show hostednetwork\\n',
                            'netsh wlan show interfaces\\n',
                            'netsh wlan show networks\\n',
                            'netsh wlan show onlyUseGPProfilesforAllowedNetworks\\n',
                            'netsh wlan show profiles\\n',
                            'netsh wlan show randomization\\n',
                            'netsh wlan show settings\\n',
                            'netsh wlan show tracing\\n',
                            'netsh wlan show wirelesscapabilites\\n',
                            'netsh wlan show wlanreport\\n'
                        )
                    }
                }
            }
        },
        'powershell':{
            'description':'Windows powershell commands',
            'modules':{
                'defender':{
                    'description':'Windows Defender information',
                    'modules':{
                        'status':(
                            'powershell -Command \\\"Get-MpComputerStatus\\\"\\n'
                        )
                    }
                },
                'applocker':{
                    'description':'Windows App Locker information',
                    'modules':{
                        'rules':(
                            'powershell -Command \\\"Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollection\\\"\\n',
                            'powershell -Command \\\"Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C;\Windows\System32\cmd.exe -User Everyone\\\"\\n'
                        )
                    }
                }
            }
        },
        'cmd':{
            'description':'Windows CMD commands',
            'modules':{
                'system':{
                    'description':'System software and hardware information',
                    'modules':{
                        'systeminfo':(
                            'systeminfo\\n',
                            'wmic qfe\\n',
                        ),
                        'accountinfo':(
                            'query user\\n',
                            'whoami /priv\\n',
                            'whoami /groups\\n',
                            'net user\\n',
                            'net localgroup\\n',
                            'net accounts\\n'
                        )
                    }
                },
                'routing':{
                    'description':'System basic routing and networking information',
                    'modules':{
                        'routing':(
                            'route print\\n'
                        ),
                        'connections':(
                            'netstat -ano\\n'
                        ),
                        'ip':(
                            'ipconfig /all\\n'
                        )
                    }
                }
            }
        }
    }
    # Okay, I know this is hell to not only look at and understand, but at least it's orginized...?
    return_code = []
    for main_module in tagret_modules:
        if main_module[0] in modules.keys():
            if main_module[1] in modules[main_module[0]]['modules'].keys():
                if main_module[2] in modules[main_module[0]]['modules'][main_module[1]]['modules'].keys():
                    return_code.append(modules[main_module[0]]['modules'][main_module[1]]['modules'][main_module[2]])
                else:
                    print(f"\'{main_module[2]}\' not found in {modules[main_module[0]]['modules'][main_module[1]]['modules'].keys()}.")
            else:
                print(f"Second value \'{main_module[1]}\' not found in {modules[main_module[0]]['modules'].keys()}.")
        else:
            print("First value not found.")
    return return_code
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
# Method for creating the exfiltration script
def ExfilDataCreation(target_language:str, target_website:str, target_method:str):
    language = target_language.strip().lower()
    method = target_method.strip().lower()
    if language not in ('python', 'c#'):
        return '\'target_language\' has to be one of the following: \'python\', \'c#\''
    if method not in ('icmp', 'http', 'https'):
        return '\'target_language\' has to be one of the following: \'icmp\', \'http\', \'https\''
    print("[#] Creating exfil script...")
# Method for having less lines and to simplify the usage of smaller or embeded modules that have large sections within them
def SmallerModuleItteration(target_module:list, target_path:list):
    temp_modules = target_module
    temp_selected = []
    while True:
        if len(temp_modules) == 0:
            print("[i] All sub modules have been used.")
            break
        print("[i] Please select a sub-module:")
        for sub_module in temp_modules:
            print(f"[*] {sub_module}")
        print("[i] Type \'end\' to exit advfirewall selection.")
        selected_sub_module = input(">")
        selected_sub_module = selected_sub_module.strip().lower()
        if selected_sub_module == 'end':
            break
        if selected_sub_module not in temp_modules:
            print(f"\'{selected_sub_module}\' is not an option.\nPick from the options.")
        else:
            temp_modules.remove(selected_sub_module)
            temp_selected.append((target_path[0], target_path[1], selected_sub_module))
    return [temp_modules, temp_selected]
# Creating the installer file, can be different languages and calls the 'LayOfTheLand_File_Creation' method
def InstallerScript_Creation(target_language:str):
    allowed_languages = ('c', 'python')
    if target_language.lower() not in allowed_languages:
        return '\'target_language\' can be one of the following; C, or Python'
    print("[#] Creating installer script...")
    target_modules = []
    allowed_modules = ['network connections', 'local users', 'windows defender', 'system info', 'app locker', 'firewall', 'advanced firewall',
                        'domain name system', 'sockets', 'lan', 'wireless lan', 'interfaces', 'bridge', 'remote access servers', 'windows internal http',
                        'windows filtering platform']
    allowed_firewall_modules = ['monitor', 'dump', 'show', 'consec', 'firewall', 'mainmode']
    allowed_interface_modules = ['6to4', 'dump', 'fl48', 'fl68', 'htttpstunnel', 'ipv4', 'ipv6', 'isatap', 'portproxy', 'tcp', 'teredo', 'udp', 'show']
    allowed_ras_modules = ['aaaa', 'dump', 'ip', 'ipv6', 'show']
    while True:
        print("[i] Lay of the Land options:")
        for module in allowed_modules:
            print(f"[*] {module}")
        print('[i] Once all wanted modules are selected, type \'end\'')
        user_choice = input(">")
        user_choice = user_choice.strip().lower()
        if user_choice == 'end':
            break
        if user_choice not in allowed_modules:
            print(f"\'{user_choice}\' is not an option.\nPick from the options.")
        else:
            if user_choice != 'interface' and user_choice != 'advanced firewall':
                allowed_modules.remove(user_choice)
            match user_choice:
                case 'network connections':
                    target_modules.append(('cmd', 'routing', 'connections'))
                case 'local users':
                    target_modules.append(('cmd', 'system', 'accountinfo'))
                case 'windows defender':
                    target_modules.append(('powershell', 'defender', 'status'))
                case 'system info':
                    target_modules.append(('cmd', 'system', 'systeminfo'))
                case 'app locker':
                    target_modules.append(('powershell', 'applocker', 'rules'))
                case 'firewall':
                    target_modules.append(('netsh', 'firewall', 'dump'))
                case 'advanced firewall':
                    allowed_firewall_modules, temp_modules = SmallerModuleItteration(allowed_firewall_modules, ['netsh', 'advfirewall'])
                    if len(allowed_firewall_modules) == 0:
                        allowed_modules.remove('advanced firewall')
                    for module in temp_modules:
                        target_modules.append(module)
                case 'domain name system':
                    target_modules.append(('netsh', 'dnsclient', 'dump'))
                    target_modules.append(('netsh', 'dnsclient', 'show'))
                case 'sockets':
                    target_modules.append(('netsh', 'winsock', 'dump'))
                    target_modules.append(('netsh', 'winsock', 'show'))
                case 'lan':
                    target_modules.append(('netsh', 'lan', 'dump'))
                    target_modules.append(('netsh', 'lan', 'show'))
                case 'wireless lan':
                    target_modules.append(('netsh', 'wlan', 'dump'))
                    target_modules.append(('netsh', 'wlan', 'show'))
                case 'interfaces':
                    allowed_interface_modules, temp_modules = SmallerModuleItteration(allowed_interface_modules, ['netsh', 'interface'])
                    if len(allowed_interface_modules) == 0:
                        allowed_modules.remove('interfaces')
                    for module in temp_modules:
                        target_modules.append(module)
                case 'bridge':
                    target_modules.append(('netsh', 'bridge', 'dump'))
                    target_modules.append(('netsh', 'bridge', 'show'))
                case 'remote access servers':
                    allowed_interface_modules, temp_modules = SmallerModuleItteration(allowed_interface_modules, ['netsh', 'ras'])
                    if len(allowed_interface_modules) == 0:
                        allowed_modules.remove('remote access servers')
                    for module in temp_modules:
                        target_modules.append(module)
                case 'windows internal http':
                    target_modules.append(('netsh', 'winhttp', 'dump'))
                    target_modules.append(('netsh', 'winhttp', 'show'))
                case 'window filtering platform':
                    target_modules.append(('netsh', 'wfp', 'dump'))
                    target_modules.append(('netsh', 'wfp', 'show'))
    target_lines = []
    returned_lines = LayOfTheLand_Creation(target_modules)
    for line in returned_lines:
        target_lines.append(line)
    print("[i] Creating installer file, if needs to be compiled (installer.c) will have to be compiled for windows.")
    match target_language.lower():
        case 'c':
            with open('installer.c', 'w') as file:
                file.write("#include <windows.h>\n#include <stdio.h>\n#include <stdlib.h>\nint main()\n{\n")
                file.write(f"\tFILE *fptr;\n\tfptr = fopen(\"created.bat\", \"w\");\n\tfprintf(fptr, \"@echo off\\nset var={target_lines[0]}%%var%%>\\\".output1423.txt\\\"\\n\");\n")
                target_lines.remove(target_lines[0])
                for module in target_lines:
                    if type(module) == tuple:
                        for line in module:
                            file.write(f"\tfprintf(fptr, \"set var={line}%%var%%>>\\\".output1423.txt\\\"\\n\");\n")
                    else:
                        file.write(f"\tfprintf(fptr, \"set var={module}%%var%%>>\\\".output1423.txt\\\"\\n\");\n")
                file.write("\tfclose(fptr);\n")
                print("[#] What language will the shell be made in? [Batch / Python] Python")
                shell_language = input(">")
                shell_language = shell_language.strip().lower()
                if shell_language not in ('python', 'batch'):
                    print("[i] Language not recognized, defaulting to Batch...")
                    shell_language = 'batch'
                if shell_language == 'batch':
                    file.write(f"\tfptr = fopen(\"shell.bat\", \"w\");\n\tfprintf(fptr, \"{ShellScript_Creation(shell_language, True)}\");\n\tfclose(fptr);\n")
                    file.write("\tprintf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\tprintf(\"[#] Starting shell...\\n\");\n\tsystem(\".\\\\shell.bat\");\n")
                if shell_language == 'python':
                    file.write(f"\tfptr = fopen(\"shell.py\", \"w\");\n\tfprintf(fptr, \"{ShellScript_Creation(shell_language, True)}\");\n\tfclose(fptr);\n")
                    file.write("\tprintf(\"[#] Collecting system information...\\n\");\n\tsystem(\".\\\\created.bat\");\n\tprintf(\"[#] Starting shell...\\n\");\n\tsystem(\"python .\\\\shell.py\");\n")
                file.write("\treturn 0;\n}")
                file.close()
        case 'python':
            try:
                with open('installer.py', 'w') as file:
                    file.write(f"import os\nwith open (\'created.bat\', \'w\') as file:\n\tfile.write(\"@echo off\\nset var={target_lines[0]}%var%>\\\".output1423.txt\\\"\\n\")\n")
                    target_lines.remove(target_lines[0])
                    for module in target_lines:
                        if type(module) == tuple:
                            for line in module:
                                file.write(f"\tfile.write(\"set var={line}%var%>>\\\".output1423.txt\\\"\\n\")\n")
                        else:
                                file.write(f"\tfile.write(\"set var={module}%var%>>\\\".output1423.txt\\\"\\n\")\n")
                    file.write("\tfile.close()\n")
                    print("[#] What language will the shell be made in? [Batch / Python] Python")
                    shell_language = input(">")
                    shell_language = shell_language.strip().lower()
                    if shell_language not in ('python', 'batch'):
                        print("[i] Language not recognized, defaulting to Batch...")
                        shell_language = 'batch'
                    if shell_language == 'python':
                        file.write(f"with open(\'shell.py\', \'w\') as file:\n\tfile.write(\"{ShellScript_Creation(shell_language, False)}\")\n\tfile.close()\n")
                        file.write("print(\"[#] Collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting shell...\")\nos.system(\"python .\\\\shell.py\")")
                    if shell_language == 'batch':
                        file.write(f"with open(\'shell.bat\', \'w\') as file:\n\tfile.write(\"{ShellScript_Creation(shell_language, False)}\")\n\tfile.close()\n")
                        file.write("print(\"[#] Collecting system information...\")\nos.system(\".\\\\created.bat\")\nprint(\"[#] Starting shell...\")\nos.system(\".\\\\shell.bat\")")
                    file.close()
            except Exception as e:
                print(e)
                exit()
    print("[#] Installer file created.")
    return "worked"
print(" _____                        ____ __  __ ____  \n| ____|_ __ _ __ _____  __   / ___|  \\/  |  _ \\ ")
print("|  _| | '__| '__/ _ \\ \\/ /  | |   | |\\/| | | | |\n| |___| |  | | | (_) >  <   | |___| |  | | |_| |")
print("|_____|_|  |_|  \\___/_/\\_\\___\\____|_|  |_|____/ \n                        |_____|")
print("                    Created by: That1EthicalHacker\n                       Version: 3.1")
while True:
    print("[i] Please input the language the installer file will be made in;\n\tC\n\tPython")
    user_choice = input(">")
    output = InstallerScript_Creation(user_choice)
    if output == "worked":
        exit()
    else:
        print("[!] Encountered error while creating Installer script!\nPlease report as an issue and try again :3")
        exit()
