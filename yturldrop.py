import subprocess
import time
import re

print("paste youtube link:")
x = input()

# extract youtube ID
findid = re.search("((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)", x)
id = (findid.group())
print("extracted youtube id: " + str(id))

# plug extracted id into the command
command = "DISPLAY=:0 chromium-browser --disable-infobars --kiosk --app=http://www.youtube.com/embed/" + str(id) + "?autoplay=1&mute=1&playsinline=1"

subprocess.call((command), shell=True)
