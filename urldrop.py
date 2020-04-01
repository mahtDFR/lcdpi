import subprocess
import time

print("input your url:")
x = input()
command = "DISPLAY=:0 chromium-browser --disable-infobars --kiosk --app=" + str(x)

print("opening " + str(x) + " on lcdpi")
time.sleep(1)

subprocess.call((command), shell=True)
