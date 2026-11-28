mesafeler = [12, 25, 35, 48, 52, 60, 75, 80, 95, 110,
             125, 140, 155, 170, 185, 200, 215, 450, 1, 90]


def en_kucuk(liste):
    sonuc = liste[0]
    for sayi in liste:
        if sayi < sonuc:
            sonuc = sayi
    return sonuc


def en_buyuk(liste):
    sonuc = liste[0]
    for sayi in liste:
        if sayi > sonuc:
            sonuc = sayi
    return sonuc


def ortalama(liste):
    toplam = 0
    for sayi in liste:
        toplam += sayi
    return toplam / len(liste)


temiz_mesafeler = []

for mesafe in mesafeler:
    if mesafe >= 2 and mesafe <= 400:
        temiz_mesafeler.append(mesafe)

print("Orijinal mesafeler:", mesafeler)
print("Hatalı ölçümler temizlendikten sonra:", temiz_mesafeler)
print("En küçük mesafe:", en_kucuk(temiz_mesafeler))
print("En büyük mesafe:", en_buyuk(temiz_mesafeler))
print("Ortalama mesafe:", ortalama(temiz_mesafeler))
