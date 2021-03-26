import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

#import RVR stuff
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import DriveFlagsBitmask #used for setting angle of RVR
from sphero_sdk import BatteryVoltageStatesEnum as VoltageStates
from sphero_sdk import RawMotorModesEnum

rvr = SpheroRvrObserver()

#function to tell the RVR to drive in a certain direction (based on angle)
def DriveWithHeading(sp,head):
    rvr.drive_with_heading(
        speed=sp, #speed=0-255
        heading=head, #angle=0-359
        flags=DriveFlagsBitmask.none.value
    )

try:
    #this is code that tells the rvr what to do
    time.sleep(2)
    rvr.reset_yaw()
    DriveWithHeading(50,0)
    time.sleep(0.5)
    DriveWithHeading(50,90)
    time.sleep(.05)
    
    
except KeyboardInterrupt:
    print('\nProgram terminated with keyboard interrupt')

#closes the connection to the rvr
rvr.close() 
