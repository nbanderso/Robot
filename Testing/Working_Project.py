import os
import sys
import time
from random import randrange
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

#import RVR stuff
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import DriveFlagsBitmask #not sure what this does
from sphero_sdk import BatteryVoltageStatesEnum as VoltageStates
from sphero_sdk import RawMotorModesEnum

#import Spark Fun stuff
import qwiic
import asyncio

rvr = SpheroRvrObserver()
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):                  # Begin returns 0 on a good init
    print("Sensor online!\n")

#function to get battery percentage
def LightsChange(red,green,blue):
    rvr.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in [red,green,blue]]
    )
    
#function to drive RVR    
def DriveWithHeading(sp,speed):
    rvr.drive_with_heading(
        speed=sp, # speed=0-255
        heading=head, # angle=0-359
        flags=DriveFlagsBitmask.none.value
    )

rvr.wake()
time.sleep(2)
print('Rvr Online')
rvr.reset_yaw()


while True:
    try:
    #this tells the Rvr what to do
        LightsChange(255,0,0)
        time.sleep(.2)
        LightsChange(0,0,255)
        time.sleep(.2)
        distance = ToF.get_distance()
        distanceInches = distance / 25.4
        print("Distance: %s Inches" % (distanceInches))
        if distanceInches < 12:
            DriveWithHeading(50,(randrange(359)))
        else:
            DriveWithHeading(50,0)
    except KeyboardInterrupt:
        print('Program Interruped by Keyboard Interrupt')
    
#except KeyboardInterrupt:
#    print('\nProgram terminated with keyboard interrupt')
      
#closes the connection to the rvr
rvr.close()
