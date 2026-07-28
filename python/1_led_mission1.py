# 경찰차 싸이렌 효과 10번 반복 빨간 > 파랑
import modi_plus
import time

bundle = modi_plus.MODIPlus()
print(bundle.modules)

led = bundle.leds[0]

for i in range(10):
    led.rgb = (255, 0, 0)  # 빨간색
    time.sleep(0.2)
    led.rgb = (0, 0, 255)  # 파란색
    time.sleep(0.2)

led.turn_off()