import modi_plus
import time

bundle = modi_plus.MODIPlus()

speaker = bundle.speakers[0]
led = bundle.leds[0]
imu = bundle.imus[0]
display = bundle.displays[0]

if __name__ == "__main__":
    
    print("모듈 연결 중이라고 기다려 좀")
    time.sleep(3)

    tof = bundle.tofs[0]
    display.reset()

    print("내 손길을 줘라")

    while True:
        distance = tof.distance

        if distance > 100 : distance = 100
        print(f"현재 삽입 거리 : {distance} inch", end="\r")

        display.reset()

        if distance <= 30:
            display.text = "  ( >_< )  \n  !!!!  \n  too close"
        elif 30 < distance <= 70:
            display.text = "  ( ^_^ )  \n  !!!!  \n  a-jas~"
        else:
            display.text = "  ( T_T )  \n  !!!!  \n  longlongint"

        time.sleep(0.2)

        