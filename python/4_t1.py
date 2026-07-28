#잠자는 표정 봇

import modi_plus
import time
bundle=modi_plus. MODIPlus()

display=bundle.displays[0]
env=bundle.envs[0]

while True:
    if env.volume>20:
        display.text="        !!!!   0    0                     0"
        time.sleep(2)
        display.text="        zzzz  --   --                  -----"
    else:
        display.text="        zzzz  --   --                  -----"

