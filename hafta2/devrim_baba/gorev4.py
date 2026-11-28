import time
from gorev3 import MesafeSensoru

sensor = MesafeSensoru()

try:
    while True:
        mesafe = sensor.oku() 
        if mesafe < 20:
            print("DUR")

        elif mesafe <= 50:
           print("YAVASLA")

        else: 
           print("ILERI")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Robot Durduruldu")
