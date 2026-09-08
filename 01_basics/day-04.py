print("Bugün Demet ve Küme kavramlarını öğreniyorum.\nDemet, listenin ekleme çıkarma yapılamayan versiyonudur.")
kume = {"Kumanda", "Araba", "Ev", "Oyuncak"}
print(kume)
print("Kümemiz bu. Şimdi öğrendiğimiz ilk döngü ile elemanları tek tek yazdıralım.")

for esya in kume:
    print(esya)

kume.add("Adaptör")
print("Kümemize 'Adaptör' elemanını ekledik. Tekrar yazdırdığımızda artık 5 elemanımız olmalı\nHatta önce 'len' komutu ile kontrol edelim.")
print("Kümemizde toplam", len(kume), "eleman var.")
print("Yeni kümemiz:", kume)

kume.remove("Araba")
print("'remove' komutu ile 'Araba' elemanını sildik. Artık kümemizde olmayacak.")
print(kume)

kume.discard("Peçete")
print("Şimdi ise 'discard' komutu ile varsa 'Peçete' elemanını kaldır dedik. Olmadığı için kümemiz aynı kalacak.")
print(kume)

kume.discard("Ev")
print("Aynı şeyi 'Ev' elemanı için yaptık. 'Ev' elemanı kümemizde olduğu için kümemizden silinecek.")
print("Son hali ile kümemiz:", kume)

kume = {"Kumanda", "Araba", "Ev", "Oyuncak"}
kume2 = {"Kumanda", "Araba", "Tablet", "Telefon"}
print("Şimdi ikinci kümemizi oluşturduk ve bunların kesişim kümesini 'intersection' komutu ile bulacağız.")
print("Bu kümelerin kesişimi:", kume.intersection(kume2))

print("Peki bu kümeleri birleştirmek isteseydik? O zaman devreye 'union' komutu girecekti.")
print("Bu kümelerin birleşimi:", kume.union(kume2))

print("Bu sefer de 'difference' komutu ile farklı elemanları yazdıralım.")
print("Kümede olup küme2de olmayan elemanlar:", kume.difference(kume2))
print("Küme2de olup kümede olmayan elemanlar", kume2.difference(kume))

print("Araba" in kume)
print("True yazdı çünkü araba bizim ilk kümemizde var.")

print("Klavye" in kume.union(kume2))
print("False değeri verdi çünkü iki kümede de klavye elemanı yok.")

bosliste1 = []
bosliste2 = list()

bosdemet1 = ()
bosdemet2 = tuple()

boskume1 = set()
boskume2 = {}

print("boskume2 bir", type(boskume2),"dir. Boş küme yalnız 1'deki gibi oluşturulur.")
print("Gün 4 bitti...")