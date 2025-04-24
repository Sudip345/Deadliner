Set objShell = CreateObject("WScript.Shell")
pythonScriptPath = "C:\Users\sudip\Desktop\college\set_time.py" ' replace with your path
objShell.Run "python " & chr(34) & pythonScriptPath & chr(34), 0, False
