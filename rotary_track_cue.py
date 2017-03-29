import RPi.GPIO as GPIO
import os, time
from time import sleep

# The class KY040 is originally from https://github.com/conradstorz/KY040
# Original license: https://github.com/conradstorz/KY040/blob/master/LICENSE
class KY040:

    CLOCKWISE = 0
    ANTICLOCKWISE = 1
    DEBOUNCE = 12

    def __init__(self, clockPin, dataPin, switchPin, rotaryCallback, switchCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        #setup pins
        GPIO.setup(clockPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(dataPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, callback=self._clockCallback, bouncetime=self.DEBOUNCE)
        GPIO.add_event_detect(self.switchPin, GPIO.FALLING, callback=self.switchCallback, bouncetime=self.DEBOUNCE)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.switchPin)
    
    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            self.rotaryCallback(GPIO.input(self.dataPin))
        """
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)
        
        self.rotaryCallback(GPIO.input(self.dataPin))
        """

    def _switchCallback(self, pin):
        """
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()
        """
        self.switchCallback()


# define commands for pideck: 
def rotaryTrack(direction):
    if direction == 1:
        os.system("wmctrl -a xwax")
        os.system("xdotool key \"Up\"")
    else:
        os.system("wmctrl -a xwax")
        os.system("xdotool key \"Down\"")

def rotaryFolder(direction):
    if direction == 1:
        os.system("wmctrl -a xwax")
        os.system("xdotool key \"Left\"")
    else:
        os.system("wmctrl -a xwax")
        os.system("xdotool key \"Right\"")

def buttonTrack(load):
    load = os.system("xdotool key \"F1\"")

def buttonCue(cue):
    cue = os.system("xdotool key \"F2\"")

 
if __name__ == "__main__":
 
# Pins used for selecting tracks
    CLOCKPIN = 5
    DATAPIN = 6
    LOAD1PIN = 13
# Pin 26 used for cue button; BLIND1 & BLIND2 for selecting folders
    CUE1PIN = 26
    BLIND1 = 17
    BLIND2 = 27
    
    GPIO.setmode(GPIO.BCM)
    
    ky0401 = KY040(CLOCKPIN, DATAPIN, LOAD1PIN, rotaryTrack, buttonTrack)
    ky0402 = KY040(BLIND1, BLIND2, CUE1PIN, rotaryFolder, buttonCue) 
    ky0401.start()
    ky0402.start()
    
    try:
        while True:
            time.sleep(0.15)
    finally:
        ky0401.stop()
        ky0402.stop()
        GPIO.cleanup()
 
