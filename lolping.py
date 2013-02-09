import os
import subprocess

for x in range(1,23):
    lolsrv = "ping 66.150.148.%i" %x
    if subprocess.call(lolsrv) == 0:
        print subprocess.check_output(lolsrv, stderr=subprocess.STDOUT)
