import random
import os
import csv
class MesafeSensoru:
    def __init__(self):
        self.okumalar = []
        os.makedirs("sensor_data", exist_ok=True)
    def oku(self):
        mesafe = random.uniform(10,200)
       	self.okumalar.append(mesafe)
        with open("sensor_data/sensor_log.csv","a") as dosya:
            dosya.write(str(mesafe) + "\n")
        return mesafe

    def ortalama(self):
        son_okumalar = self.okumalar[-5:] 	
        toplam = 0
        
        for sayi in son_okumalar:
            toplam = toplam + sayi
    
        sonuc = toplam / len(son_okumalar)

        return sonuc

sensor = MesafeSensoru()
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.oku())
print(sensor.ortalama())
