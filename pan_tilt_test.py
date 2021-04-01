import time
import pi_servo_hat
import picamera

servo = pi_servo_hat.PiServoHat()
servo.restart()

def center_camera():
    servo.move_servo_positon(1,0,180)
    servo.move_servo_position(0,0,180)
    
def left_camera():
    servo.move_servo_position(1,0,180)
    servo.move_servo_position(0,-90,180)

def right_camera():
    servo.move_servo_position(1,0,180)
    servo.move_servo_position(0,90,180)

def up_camera():
    servo.move_servo_position(1,90,180)
    servo.move_servo_position(0,0,180)
    
while True:
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
