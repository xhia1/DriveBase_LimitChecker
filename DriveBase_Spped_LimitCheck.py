from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)

drive_base = DriveBase(left_motor, right_motor, 56, 112)




#speed単体上限チェック

speed = 100

while True:
    try:
        drive_base.settings(speed, 500, 200, 400)
        print("OK:", speed)
        speed += 1
    except:
        print("上限に到達:", speed)
        break
