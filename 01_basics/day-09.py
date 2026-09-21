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
print("Sonsuz bir döngü oluşturduk. 'x' 2'ye tam bölünüyorsa 1 ekleyip döngüye devam etmesini, eğer bölünmüyorsa yazdırdıktan sonra 1 ekleyip başa döndük.\n'x' 53'e ulaştığında da döngünün sona ermesini sağladık.")

# input fonksiyonu

sayi = int(input("Bir sayı giriniz: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
    print(faktoriyel)
print(f"{sayi}! = {faktoriyel}")
print(f"'faktoriyel' (1) değişkenini 1'den {sayi}'ya kadar olan tüm sayılarla çarptık. Bu da bize {sayi}'nın faktöriyelini verdi.")

print("Bunu 'while' döngüsü ile de yapabiliriz.")
sayi = int(input("Tekrar sayı giriniz: "))
faktoriyel = 1
i = 1
while i <= sayi:
    faktoriyel *= i
    i += 1
print(f"Bu döngü sayesinde {sayi}! = {faktoriyel}'i bulduk.")
