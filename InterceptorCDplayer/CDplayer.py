import numpy as np
import interceptor
import InputLogger 

def __init__(self, cd_name, interceptor=None):
    self.cd_name = cd_name
    self.playing = False
    
def play(self):
    if self.playing == True:
            print("{self.cd_name} is already playing")
    else:
        self.playing = True
        print(f"Playing {self.cd_name}")
    
def stop(self):
        if self.playing == False:
            print("{self.cd_name} is already stopped")
        else:
            self.playing = False
            print(f"Stopping {self.cd_name}")