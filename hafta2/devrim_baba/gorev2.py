mesafeler = [15, 20, 35, 42, 50, 65, 80, 95, 110, 125,
             140, 155, 170, 185, 200, 220, 250, 450, 1, 300]

def en_kucuk_bul(liste):
    en_kucuk = liste[0]

    for sayi in liste:
        if sayi < en_kucuk:
            en_kucuk = sayi
    return en_kucuk

print(en_kucuk_bul(mesafeler))

def en_buyuk_bul(liste):
    en_buyuk = liste[0]
    
    for sayi in liste:
        if sayi > en_buyuk:
            en_buyuk = sayi

    return en_buyuk

print(en_buyuk_bul(mesafeler))

def ortalama_bul(liste):
    toplam = 0

    for sayi in liste:
        toplam = toplam + sayi
    ortalama = toplam / len(liste)
    return ortalama

print(ortalama_bul(mesafeler))

temiz_mesafeler = []

for sayi in mesafeler: 
    if sayi>=2 and sayi <=400:
        temiz_mesafeler.append(sayi)

print(temiz_mesafeler)

print("Temiz en kucuk:", en_kucuk_bul(temiz_mesafeler))
print("Temiz en buyuk:", en_buyuk_bul(temiz_mesafeler))
print("Temiz en ortalama:", ortalama_bul(temiz_mesafeler))
