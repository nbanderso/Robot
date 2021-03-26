import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

#import RVR stuff
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import DriveFlagsBitmask #not sure what this does

rvr = SpheroRvrObserver()

"""
all_lights commands
    status_indication_left
    status_indication_right
    headlight_left
    headlight_right
    battery_door_front
    battery_door_rear
    power_button_front
    power_button_rear
    brakelight_left
    breaklight_right
"""

#function to right headlights
def LightsRightHead(red,green,blue):
    rvr.set_all_leds(
        led_group=RvrLedGroups.headlight_right.value,
        led_brightness_values=[red,green,blue]
    )
 
try:
    #this is code that tells the rvr what to do
    rvr.wake()
    time.sleep(2)
    print('Rvr Online')
    LightsRightHead(0,0,255)
    time.sleep(1)
    
   
    
except KeyboardInterrupt:
    print('\nProgram terminated with keyboard interrupt')

#closes the connection to the rvr
rvr.close() 
