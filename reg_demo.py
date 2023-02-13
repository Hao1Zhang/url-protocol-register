# importing required module
import winreg as wrg
import os
# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_CURRENT_USER
  
# Store path in soft
soft = wrg.OpenKeyEx(location, r"SOFTWARE\\")
classes = wrg.OpenKeyEx(soft, r"CLASSES\\")
# print(classes)
key_1 = wrg.CreateKey(classes, "abd")
  
# Creating values in Geeks
wrg.SetValueEx(key_1, None, 0, wrg.REG_SZ,
               "URL:abd")
wrg.SetValueEx(key_1, "URL Protocol", 0, wrg.REG_SZ,
               "")
shell = wrg.CreateKey(key_1, "shell")
open = wrg.CreateKey(shell, "open")
command = wrg.CreateKey(open, "command")

exe_path=os.path.join(os.getcwd(),"ivlauncher.exe")
wrg.SetValueEx(command, None, 0, wrg.REG_SZ,
               f"{exe_path} %1")
# wrg.SetValueEx(key_1, "value Two", 0, wrg.REG_SZ,
#                "Participate in Technical Scripter")
  
# if key_1:
#     wrg.CloseKey(key_1)
wrg.CloseKey(key_1)