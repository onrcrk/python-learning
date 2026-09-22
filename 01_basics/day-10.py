# metinde aynı harften kaç tane var?

metin = input("Bir metin giriniz: ")
metin.lower
sozluk = dict()

for harf in metin:
    if harf in sozluk:
        sozluk[harf] += 1
    else:
        sozluk[harf] = 1

for harf,adet in sozluk.items():
    print(f"Harf: {harf}, Adet: {adet}")