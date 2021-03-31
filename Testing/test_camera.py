import smbus
import os
import sys
import time
import io
from datetime import datetime, timedelta
import statistics

import pantilthat
import picamera


tf_width = 299 #Width required for Tensorflow
tf_height = 299 #Height required for Tensorflow
tf_bw = True #Whether Tensflow wants black and white

'''
take_picture() captures a single black and white frame in the dimensions required for TF
arguments: outFile - defines where to store the captured image
'''
def take_picture(outFile):
	with picamera() as camera:
		camera.vflip = True
		camera.hflip = True
		camera.contrast = 15
		camera.sharpness = 35
		camera.saturation = 20
		camera.shutter_speed = 0 #auto
		camera.color_effects = (128,128) #sets camera to black and white
		camera.PiResolution(width=tf_width, Height=tf_height)
		camera.capture(outFile, format="jpeg")
'''
take_poicture() captures a single high-resolution image from the pi camera.
Note: this image will need to be downgrated to 299x299 and converted to black and white for TF
arguments: outFile - defines where to store the image 
'''
def take_picture_hd(outFile):
	with picamera() as camera:
		camera.vflip = True
		camera.hflip = True
		# camera.iso = 400
		camera.contrast = 15
		camera.sharpness = 35
		camera.saturation = 35
		#time.sleep(2)
		#camera.shutter_speed = camera.exposure_speed
		camera.shutter_speed = 0 #auto
		#camera.exposure_mode = 'off'
		camera.capture(outFile, format="png")

'''
convert_pic_to_tf process pic to TF requirements.
arguments:	inFile - name and path of input file
			outFile - name and path of outfile
			outWidth - width of output image (pixels)
			outHeight - height of output image (pixels)
			black_and_white - boolean indicating change to black and white
'''
def convert_pic_to_tf(inFile, outFile, outWidth, outHeight, black_and_white=True):
	pass

'''
point_camera() uses the pan/tilt mast to point the camera in a particular azimuth and elevation.
Note: the mapping from the argument values to actual direction and elevation angle has not been determined.  Will need to do this experimentally.
Arguments:	pan - direction to pan the camera (positive if left)
			tilt - angle to tilt the camera. (negative is up)
'''
def point_camera(panval, tiltval):
	pantilthat.pan(panval) #positive is left from cam POV
	pantilthat.tilt(tiltval) #negative is up from cam POV

def center_camera():
	pantilthat.tilt(90)
	pantilthat.pan(-12)

def main():
	center_camera()
	PicCount = 1 #keeps track of picture count
	pantilthat.tilt(90)
	#Look Right
	for PanAngle in range(0, -100, -10):
		pantilthat.pan(PanAngle)
		picFile = "rocko%0.3d.png" % (PicCount)
		time.sleep(1) #let the camera stop moving
		time_picture(PicFile)
		#cRange = adc_to_range()
		#print("Picture %s, range %0.3f, azimuth %d" % (PicFile, cRange, PanAngle))
		PicCount += 1
	#Look Left
	for PanAngle in range(0, 100, 10):
		pantilthat.pan(PanAngle)
		picFile = "rocko%0.3d.png" % (PicCount)
		time.sleep(1) #let the camera stop moving
		take_picture(PicFile)
		#cRange = adc_to_range()
		#print("Picture %s, range %0.3f, azimuth %d" % (PicFile, cRange, PanAngle))
		PicCount += 1
	center_camera
