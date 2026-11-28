sayilar = [2, 7, 11, 15]
hedef = 9
bulundu = False

for i in range(len(sayilar)):
    if bulundu:
        break

    for j in range(i + 1, len(sayilar)):
        if sayilar[i] + sayilar[j] == hedef:
            print([i, j])
            bulundu = True
            break
