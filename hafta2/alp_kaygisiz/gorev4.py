import time
from gorev3 import MesafeSensoru


def robot_calistir():
    sensor = MesafeSensoru()
    print("Robot başlatıldı. Durdurmak için Ctrl+C'ye basın.\n")

    try:
        while True:
            mesafe = sensor.oku()
            ort = sensor.ortalama()

            if mesafe < 20:
                karar = "DUR"
            elif mesafe <= 50:
                karar = "YAVASLA"
            else:
                karar = "ILERI"

            print(f"Mesafe: {mesafe:6.2f} cm | Hareketli Ort: {ort:6.2f} cm -> Karar: {karar}")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nRobot durduruldu")


if __name__ == "__main__":
    robot_calistir()
