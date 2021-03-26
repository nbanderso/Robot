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

rvr = SpheroRvrObserver()

#function to get battery percentage
def BatteryStat(battery_percentage):
    print('Battery Percentage: ',battery_percentage)

try:
    #this is code that tells the rvr what to do
    rvr.wake()
    time.sleep(2)
    print('Rvr Online')
    rvr.get_battery_precentage(handler=BatteryStat)
    time.sleep(1)
    
except KeyboardInterrupt:
    print('\nProgram terminated with keyboard interrupt')

#closes the connection to the rvr
rvr.close() 
