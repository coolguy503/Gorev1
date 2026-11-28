def two_sum(sayilar, hedef):
    for i in range(len(sayilar)):
        for j in range(i + 1, len(sayilar)):
            if sayilar[i] + sayilar[j] == hedef:
                return [i, j]

    return None


sayilar = [2, 7, 11, 15]
hedef = 9

sonuc = two_sum(sayilar, hedef)

print("Sayılar:", sayilar)
print("Hedef:", hedef)
print("Sonuç:", sonuc)
