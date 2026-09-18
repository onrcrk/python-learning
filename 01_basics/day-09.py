liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if i == 1:
        print("Döngünün")
        continue
    if i == 2:
        print("İçinde")
        continue
    if i == 3:
        print("'if' bloklarıyla")
        continue
    if i == 4:
        print("İstediğimiz değerlerde")
        continue
    if i == 5:
        print("Farklı şeyler")
        continue
    if i == 6:
        print("Yaptırabiliriz")
        continue
    print(i)
print("6'ya kadar 'if' bloklarıyla farklı şeyler yazdırıp döngüye devam ettirdik.\nBundan dolayı döngü sadece 6'dan sonraki sayıları yazdırdı.")

liste = range(51)
print("Listemize 0'dan 50'a kadar olan sayıları tanımladık. Şimdi sadece 5'e bölünen sayıları yazdırmak istiyoruz.")
for i in liste:
    if i % 5 != 0:
        continue
    print(i)