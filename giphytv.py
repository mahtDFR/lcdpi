import subprocess
import time

print("choose your hashtag:")

x = input()
command = "DISPLAY=:0 chromium-browser --disable-infobars --kiosk --app=http://tv.giphy.com/" + str(x)

print("showing random gifs with the hashtag '" + str(x) + "' on lcdpi")
time.sleep(0.5)

print("sending URL to chromium: http://tv.giphy.com/" + str(x))
time.sleep(0.5)

subprocess.call((command), shell=True)
