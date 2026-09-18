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
print("'i'nin 5'e bölümünden kalan 0 değilse devam et dedik. Bölümü 0'a eşit olanlar yazdırıldı.")

x = 1
while x <= 10:
    print(x)
    x += 1
print("'x' değeri 1'di. Döngü 10 olana kadar devam etti. En son", x,"olunca döngü sona erdi.")

x = 0
while True:
    if x == 53:
            break
    if x % 2 == 0:
        x += 1
        continue
    print(x)
    x += 1
print("Sonsuz bir döngü oluşturduk. 'i' 2'ye tam bölünüyorsa 1 ekleyip devam et, bölünmüyorsa yazdırıp 1 ekle dedik.\n54'e eşit olduğunda da döngüyü durdurmasını istedik.")
print("Döngüyü durdurmak istediğimiz sayı")