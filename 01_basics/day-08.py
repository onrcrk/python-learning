print("'for' ve 'while' döngüsü çalışmaları.")
liste = ["Ahmet", "Mehmet", "Onur", "Ayşe", "Fatma"]
for i in liste:
    print(i)
print("'i' değişkenimiz listenin içindeki tüm elemanlara tek tek gitti ve 'print' dediğimiz için hepsini tek tek yazırdı.\nAynısını stringler için de yapabiliriz.")

isim = "Onur"
for i in isim:
    print(i)
print("'i', 'Onur' stringindeki tüm karakterlere tek tek gitti ve yazdı.")

print("Belirli aralıktaki sayıları tek tek yazdırmak için 'range' veri tipine başvurabiliriz.")
for i in range(0,5):
    print(i)
print("'range' veri tipine yazdığımız ilk değer dahil, ikinci değer dahil değildir.\nBundan dolayı 0'dan 4'e kadar yazdı.")

print("Tek tek yazdırmak değil de belirli aralıklarla yazdırmak istersek 3. bir değer girmemiz gerekiyor.")
for i in range(0,15,2):
    print(i)
print("Bu sefer 1'den 14'e kadar değerleri ikişer şekilde yazdırdı.")

rakam = 2
for i in range(5):
    rakam *= 2
    print(rakam)
print("'rakam' değişkenini (2'yi) 2 ile 5 kez çarptık. Yani sonuç,", rakam, "oldu.")

print("'for' döngülerini iç içe kullanmamız da mümkün.")
list1 = ["Ayşe","Mehmet","Onur"]
list2 = ["Yılmaz","Söner","Kral"]
for isim in list1:
    for soyisim in list2:
        print(isim,soyisim)
print("İlk döngü 'list1' içindeki ilk elemanı aldı ve alttaki döngüyü çalıştırdı.\nAlttaki döngü bitince ikinci elemana geçti ve döngü tekrarladı.\nİlk döngü tamamlanınca işlem sona erdi.")
