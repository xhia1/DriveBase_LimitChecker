from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)

drive_base = DriveBase(left_motor, right_motor, 56, 112)



default = drive_base.settings()
print("-----------------------------------")
print("初期settings:", default)


def find_limit(start, step, setter):
    value = start
    last_ok = None
    while True:
        try:
            setter(value)
            last_ok = value
            value += step
        except:
            return last_ok



# ===== 各上限を取得 =====
max_straight_speed = find_limit(
    100, 1,
    lambda v: drive_base.settings(v, default[1], default[2], default[3])
)

max_straight_acceleration = find_limit(
    100, 10,
    lambda v: drive_base.settings(default[0], v, default[2], default[3])
)

max_turn_rate = find_limit(
    50, 1,
    lambda v: drive_base.settings(default[0], default[1], v, default[3])
)

max_turn_acceleration = find_limit(
    50, 10,
    lambda v: drive_base.settings(default[0], default[1], default[2], v)
)



# ===== 結果表示 =====

print("---------- 上限値まとめ -----------")
print("straight_speed:", max_straight_speed)
print("straight_acceleration:", max_straight_acceleration)
print("turn_rate:", max_turn_rate)
print("turn_acceleration:", max_turn_acceleration)
print("-----------------------------------")
