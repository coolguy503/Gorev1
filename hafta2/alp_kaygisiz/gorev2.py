def istatistik_hesapla(veri_listesi):
    if not veri_listesi:
        return None, None, None

    en_kucuk = veri_listesi[0]
    en_buyuk = veri_listesi[0]
    toplam = 0
    eleman_sayisi = 0

    for deger in veri_listesi:
        if deger < en_kucuk:
            en_kucuk = deger
        if deger > en_buyuk:
            en_buyuk = deger
        toplam += deger
        eleman_sayisi += 1

    ortalama = toplam / eleman_sayisi
    return en_kucuk, en_buyuk, ortalama


def hatalari_ayikla(veri_listesi):
    temiz = []
    for deger in veri_listesi:
        if 2 <= deger <= 400:
            temiz.append(deger)
    return temiz


if __name__ == "__main__":
    # 20 elemanlı örnek sensör verisi (hatalı veriler dahil: -5, 1, 450, 999)
    ham_veriler = [
        15, 22, -5, 120, 340, 450, 85, 92, 1, 210,
        175, 999, 64, 48, 399, 2, 130, 280, 405, 55
    ]

    ham_min, ham_max, ham_ort = istatistik_hesapla(ham_veriler)
    print("--- HAM VERİ SONUÇLARI ---")
    print(f"En Küçük: {ham_min} cm | En Büyük: {ham_max} cm | Ortalama: {ham_ort:.2f} cm")

    temiz_veriler = hatalari_ayikla(ham_veriler)
    temiz_min, temiz_max, temiz_ort = istatistik_hesapla(temiz_veriler)
    print("\n--- TEMİZLENMİŞ VERİ SONUÇLARI (2-400 cm) ---")
    print(f"Kalan Eleman Sayısı: {len(temiz_veriler)}")
    print(f"En Küçük: {temiz_min} cm | En Büyük: {temiz_max} cm | Ortalama: {temiz_ort:.2f} cm")
