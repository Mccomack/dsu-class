

try:
    while True:
        # 겁나 효율적인 토글 알고리즘
        if (depth is True or button.toggled) and toggle is False:
            depth = True
            if not button.toggled:
                toggle = True
                depth = False

        elif (depth is True or button.toggled) and toggle is True:
            depth = True
            if not button.toggled:
                toggle = False
                depth = False

        motorSpeed = 0
        if toggle is True and imu.angle_x < -50:
            motorSpeed = 100

        motor.speed = motorSpeed