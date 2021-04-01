import pi_servo_hat
import picamera

pi_servo_hat.restart()

def point_camera(panval,tiltval):
    pi_servo_hat.pan(panval)
    pi_servo_hat.tilt(tiltval)


def center_camera():
    pi_servo_hat.tilt(1,0,180)
    pi_servo_hat.pan(0,0,180)
    
def left_camera():
    pi_servo_hat.tilt(1,0,180)
    pi_servo_hat.pan(0,-90,180)
    
def right_camera():
    pi_servo_hat.tilt(1,0,180)
    pi_servo_hat.pan(0,90,180)

def up_camera():
    pi_servo_hat.tilt(1,90,180)
    pi_servo_hat.pan(0,0,180)
    
while True:
    camera.start_preview()
    print('centering')
    center_camera()
    time.sleep(1)
    print('left')
    left_camera()
    time.sleep(1)
    print('right')
    right_camera()
    time.sleep(1)
    print('up')
    up_camera()
