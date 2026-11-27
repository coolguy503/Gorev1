import os
import random


class MesafeSensoru:
    def __init__(self, klasor="loglar", dosya_adi="sensor_log.csv"):
        self.okumalar = []
        os.makedirs(klasor, exist_ok=True)
        self.dosya_yolu = os.path.join(klasor, dosya_adi)

    def oku(self):
        mesafe = round(random.uniform(10, 200), 2)
        self.okumalar.append(mesafe)

        with open(self.dosya_yolu, "a", encoding="utf-8") as dosya:
            dosya.write(f"{mesafe}\n")

        return mesafe

    def ortalama(self):
        if not self.okumalar:
            return 0.0
        son_bes = self.okumalar[-5:]
        return round(sum(son_bes) / len(son_bes), 2)


if __name__ == "__main__":
    sensor = MesafeSensoru()
    for i in range(7):
        deger = sensor.oku()
        print(f"{i + 1}. Okuma: {deger} cm | Son 5 Ortalama: {sensor.ortalama()} cm")
