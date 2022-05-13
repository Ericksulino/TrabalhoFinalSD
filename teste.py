import subprocess
import sys
import timeit
import time
cmd = "C:/Users/erick/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/Codigos/Python/TrabalhoFinalSD/cliente.py"
inicioScript = timeit.default_timer()

for i in range(30):
    return_code = subprocess.call(cmd, stderr=subprocess.DEVNULL, shell=True)
    time.sleep(1)

fimScript = timeit.default_timer()

print("Tempo de execução: {}".format(fimScript-inicioScript))