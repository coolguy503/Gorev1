# 2. Hafta Görevi - Python ile Sensör Verisi Simülasyonu

## Ne Yaptım?
- **gorev1.py:** İç içe iki `for` döngüsü kullanarak hedef sayıya ulaşan iki elemanın indekslerini bulan Two Sum algoritmasını yazdım.
- **gorev2.py:** Hazır `min()`, `max()`, `sum()` fonksiyonlarını kullanmadan tek döngü ile minimum, maksimum ve ortalama hesaplayan; ardından 2-400 cm dışındaki hatalı sensör verilerini filtreleyen yapıyı kurdum.
- **gorev3.py:** `MesafeSensoru` sınıfı ile 10-200 cm arası gürültülü veri üreten, `self.okumalar[-5:]` dilimlemesi ile hareketli ortalama alan ve sonuçları otomatik oluşturulan `loglar/sensor_log.csv` dosyasına yazan OOP yapısını geliştirdim.
- **gorev4.py:** `gorev3` modülündeki sensör sınıfını içe aktararak saniyede 2 okuma yapan, mesafeye göre `DUR`, `YAVASLA`, `ILERI` kararı veren ve `KeyboardInterrupt` ile güvenli kapanan kontrol döngüsünü yazdım.


## Nasıl Çalıştırılır?
Terminalde `hafta2/alp_kaygisiz` dizini içerisindeyken:
```bash
python3 gorev1.py
python3 gorev2.py
python3 gorev3.py
python3 gorev4.py
python3 bonus.py
