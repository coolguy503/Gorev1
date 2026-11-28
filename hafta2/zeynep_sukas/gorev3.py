import random
import os
import csv


class MesafeSensoru:
    def __init__(self):
        self.olcumler = []

        klasor = os.path.dirname(os.path.abspath(__file__))
        self.dosya_yolu = os.path.join(klasor, "sensor_log.csv")

        os.makedirs(os.path.dirname(self.dosya_yolu), exist_ok=True)

    def oku(self):
        mesafe = round(random.uniform(10, 200), 2)

        self.olcumler.append(mesafe)

        if len(self.olcumler) > 5:
            self.olcumler.pop(0)

        dosya_var = os.path.exists(self.dosya_yolu)

        with open(self.dosya_yolu, "a", newline="") as dosya:
            yazici = csv.writer(dosya)

            if not dosya_var:
                yazici.writerow(["Mesafe (cm)"])

            yazici.writerow([mesafe])

        return mesafe

    def ortalama(self):
        if len(self.olcumler) == 0:
            return 0

        return sum(self.olcumler) / len(self.olcumler)


if __name__ == "__main__":
    sensor = MesafeSensoru()

    for i in range(10):
        mesafe = sensor.oku()
        print("Ölçüm:", mesafe, "cm")
        print("Son 5 ölçümün ortalaması:", round(sensor.ortalama(), 2))
