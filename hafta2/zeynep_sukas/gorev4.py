import time
from gorev3 import MesafeSensoru


sensor = MesafeSensoru()

print("Robot çalışıyor... Durdurmak için Ctrl+C tuşlarına basın.")

try:
    while True:
        mesafe = sensor.oku()

        if mesafe < 20:
            komut = "DUR"
        elif mesafe <= 50:
            komut = "YAVASLA"
        else:
            komut = "ILERI"

        print("Mesafe:", mesafe, "cm - Komut:", komut)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nRobot durduruldu")
