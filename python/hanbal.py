import modi_plus
import time
import math
MOTOR_COUNT = 2

bundle = modi_plus.MODIPlus()
imu = bundle.imus[0]

# 1. 가속도 (Acceleration) - 직선 움직임 및 중력
acc_x = imu.acceleration_x
acc_y = imu.acceleration_y
acc_z = imu.acceleration_z

def f_jakdog(speed, par):
    for i in range(MOTOR_COUNT):
        bundle.motors[i].speed = par * speed if i % 2 == 0 else -speed * par

for i in range(MOTOR_COUNT):
    bundle.motors[i].angle = 0, 0


while True:
    ang_x = imu.angle_x + 90
    ang_x = round(ang_x, 1)

    if -90 < ang_x < 90:
        ang_x = math.atan(ang_x) * 30

        f_jakdog(ang_x, -1)
        print(ang_x, end='\r')
    else:
        f_jakdog(0, 0)
        print(f"넘어짐 : {ang_x}", end='\r')