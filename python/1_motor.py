import modi_plus
import time
import random

bundle = modi_plus.MODIPlus()
print(bundle.modules)

def f_jakdog(speed):
    for i in range(4):
        bundle.motors[i].speed = speed if i % 2 == 0 else -speed

for i in range(4):
    bundle.motors[i].angle = 0, 0
time.sleep(2)

# while True:
#     randomintda = random.randint(-100,100)
#     f_jakdog(randomintda)
#     bundle.displays[0].text = f"{randomintda}"
