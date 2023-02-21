import time
import pychromecast
import os
import subprocess
import socket

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[" "]) # Place the name of your chromecast device within the open-close quotes

PORT = 8000
HOSTNAME = socket.gethostname()
ADDRESS = socket.gethostbyname(HOSTNAME)

def videoServer():
    videoDirectory = input("What directory is the file stored?: ")
    command = f"python3 -m http.server -d {videoDirectory} &"
    server = subprocess.run(command, shell=True)
    
    

def videoCast():
    videoTitle = input("What is the filename of the video?: ")
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    videoLink = f"http://{ADDRESS}:{PORT}/{videoTitle}"
    mc.play_media(videoLink, 'video/mp4')
    mc.block_until_active()
    print(mc.status)

videoServer()
videoCast()
stopVideo = False
while(stopVideo == False):
    userResponse = input("End Server?(y/n): ")
    if(userResponse == "y"):
        stopVideo = True
        break
    elif(userResponse == "n"):
        print("Resuming server operations?")
    else:
        print("Somethings wrong I can feel it...")
if(os.name == 'postix'):
    subprocess.run("pkill python3", shell=True)
elif(os.name == 'nt'):
    subprocess.run("taskkill /im python.exe", shell=True)
print("Exiting")