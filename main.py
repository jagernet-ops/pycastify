import time
import pychromecast
import os
import subprocess

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Mikes Hard Visual Aid"])

def videoServer():
    videoDirectory = input("What directory is the file stored?: ")
    command = "python3 -m http.server -d " + videoDirectory + " &"
    subprocess.run(command, shell=True)

def videoCast():
    videoTitle = input("What is the filename of the video?: ")
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    videoLink = "http://192.168.1.3:8000/" + videoTitle
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
    elif(userResponse == "n"):
        print("Resuming server operations?")
    else:
        print("Somethings wrong I can feel it...")
subprocess.run("pkill python3")