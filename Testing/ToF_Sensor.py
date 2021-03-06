#Sparkfun Sensor
import qwiic
import time

#Rvr
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))

import RPi.GPIO as GPIO
import asyncio

from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

#Testing Sparkfun ToF Sensor
print("Testing qwiic sensor")
ToF = qwiic.QwiicVL53L1X()
if (ToF.SensorInit() == None):
    print("Finally! not stuck!")
'''
while True:
    try:
        ToF.StartRanging()
        time.sleep(.05)
        distance = ToF.GetDistance()
        time.sleep(.05)
        ToF.StopRanging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0

    except Exception as e:
        print(e)
'''

ToF.StartRanging()
# distance = ToF.GetDistance()
# distanceInches = distance / 25.4

async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    while True:
            distance = ToF.GetDistance()
            distanceInches = distance / 25.4
            dist_f = int(distanceInches)
            print('Distance is {0} inches'.format(dist_f))
            if dist_f < 12:
                await rvr.raw_motors(2,150,1,150)
                dist_f = int(distanceInches)
                await asyncio.sleep(.5)
                print ('Turning Right')
                await rvr.reset_yaw()
            elif dist_f >= 12:
                await rvr.raw_motors(1,120,1,120)
                dist_f = int(distanceInches)
                await asyncio.sleep(.05)
                await rvr.reset_yaw()


try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
except KeyboardInterrupt:
    print("Program ended by KeyboardInterrupt")

