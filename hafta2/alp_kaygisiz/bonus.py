def palindrom_mu(sayi):
    if sayi < 0:
        return False

    orijinal = sayi
    ters_sayi = 0

    while sayi > 0:
        son_basamak = sayi % 10
        ters_sayi = (ters_sayi * 10) + son_basamak
        sayi = sayi // 10

    return orijinal == ters_sayi


if __name__ == "__main__":
    testler = [121, -121, 10, 12321, 456]
    for s in testler:
        print(f"{s} palindrom mu? -> {palindrom_mu(s)}")
