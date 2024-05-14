import os
import network
import requests

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    wlan.active(True)
    wlan.connect("TurkTelekom_T753B", "yLkXGAfV")
while not wlan.isconnected():
    pass

if not "kernels" not in os.listdir():
    os.mkdir("kernels")

os.mkdir("kernels/cnrkernel_v1")
os.mkdir("kernels/cnrkernel_v1/kernelscripts")
os.mkdir("kernels/cnrkernel_v1/kerneldrivers")
os.mkdir("kernels/cnrkernel_v1/kernelinfo")

with open("kernels/cnrkernel_v1/kernelscripts/cnrkernel_v1.py") as kernelscript:
    mainkernelscript = requests.get("https://raw.githubusercontent.com/NachosIsJustNachos/CenterOS/main/packages/cnrkernel/cnrkernel.py")
    kernelscript.write(mainkernelscript)
