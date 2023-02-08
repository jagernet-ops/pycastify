import time
import pychromecast
import os
from subprocess import Popen

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Mikes Hard Visual Aid"])


videoDirectory = input("What directory is the file stored?: ")
command = "python3 -m http.server -d " + videoDirectory

def videoCast():
    videoTitle = input("What is the filename of the video?: ")
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    videoLink = "http://192.168.1.3:8000/" + videoTitle
    mc.play_media(videoLink, 'video/mp4')
    mc.block_until_active()
    print(mc.status)

p = Popen(command)
videoCast()

