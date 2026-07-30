# 손코딩 했다
# 리눅스/Mac에서 돌려라 윈도우 안된다

import time
import math
import os

def timePrint():
    return round(time.time())

print('준비')
while True:
    os.system("clear")
    prevTime = timePrint()
    try:
        os.system("clear")
        while True:
            nowTime = timePrint()
            print(f'{nowTime - prevTime}초 경과', end="\r")
            time.sleep(0.05)

    except KeyboardInterrupt:
        try:
            os.system("clear")
            prevTime = timePrint()
            while nowTime - prevTime < 3:
                nowTime = timePrint()
                print(f'초기화됨. {3 - nowTime + prevTime}초 뒤 다시 시작', end="\r")
                time.sleep(0.05)
        except KeyboardInterrupt:
            os.system("clear")
            print("종료")
            break