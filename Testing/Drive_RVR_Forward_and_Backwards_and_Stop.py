import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

#import RVR stuff
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import DriveFlagsBitmask #not sure what this does
from sphero_sdk import BatteryVoltageStatesEnum as VoltageStates
from sphero_sdk import RawMotorModesEnum

rvr = SpheroRvrObserver()

#function to get RVR to drive forward
def DriveForward(speed):
    rvr.raw_motors(
        left_mode=RawMotorModesEnum.forward.value,
        left_speed=speed, #speed = 0 - 255
        right_mode=RawMotorModesEnum.forward.value,
        right_speed=speed #speed = 0 - 255
    )

#function to get RVR to drive backwards
def DriveReverse(speed):
    rvr.raw_motors(
        left_mode=RawMotorModesEnum.reverse.value,
        left_speed=speed, #speed = 0 - 255
        right_mode=RawMotorModesEnum.reverse.value,
        right_speed=speed #speed = 0 - 255
    )

#function to get RVR to stop driving
def MotorsStop():
    rvr.raw_motors(
        left_mode=RawMotorModesEnum.off.value,
        left_speed=0, #speed = 0 - 255
        right_mode=RawMotorModesEnum.off.value,
        right_speed=0 #speed = 0 - 255
    )

try:
    #this is code that tells the rvr what to do
    DriveForward(100)
    time.sleep(1)
    MotorsStop()
    time.sleep(.02)
    DriveBackward(100)
    time.sleep(1)
    MotorsStop()
    
    
except KeyboardInterrupt:
    print('\nProgram terminated with keyboard interrupt')

#closes the connection to the rvr
rvr.close() 
