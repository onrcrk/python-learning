# if, elif, else
print("If koşulunu kullanırken kontrol operatörlerini kullanırız. Mesela iki değişken oluşturalım")
a = 35
b = 53
if a == b:
    print("Memleket sevdası")
print("Eşit olmadığı için if bloğu çalışmadı ve hiçbir şey yazılmadı. Şimdi eşit değildir ile yapalım.")
if a != b:
    print("Memleket sevdası")
print("Bu sefer 'Memleket sevdası' yazdı çünkü iki değişken birbirine eşit değil.")

print(("If bloğu doğru olmadığında yaptırmak istediğimiz şeyi else bloğuyla yaptırabiliriz."))
if a == b:
    print("Memleket sevdası")
else:
    print("Güzel memleketim")
print("Eşit olmadıkları için 'Güzel memleketim' mesajı yazdırıldı.")

print("Bir listede kontrol etmek istediğimiz birden fazla eleman varsa şöyle yapabiliriz.")
ayin_elemanlari = ["Ahmet", "Mehmet", "Onur", "Sıla", "Naz"]
print("Ayın elemanları:", ayin_elemanlari)
bolum = ["Rümeysa", "Ali", "Mahmut"]
print("Bölümümdeki elemanlar:", bolum)
if "Rümeysa" in ayin_elemanlari:
    print("Tebrikler Rümeysa!")
elif "Ali" in ayin_elemanlari:
    print("Tebrikler Ali!")
elif "Mahmut" in ayin_elemanlari:
    print("Tebrikler Mahmut!")
else:
    print("Bizim bölümden kimse ayın elemanı olamamış. Yazıklar olsun!")
print("Böyle tek tek kontrol etmiş oldum. Şimdi tek kişiyi tebrik etmek yerine giren en az bir kişi var ise bölümü tebrik edelim")
if bolum in ayin_elemanlari:
    print("Tebrikler! Aramızda ayın elemanı var.")
else:
    print("Bölümümüzden kimse ayın elemanı olamamış.")

print("'ayin_elemanlari'na bizim bölümden birini ekleyelim.")
ayin_elemanlari.append("Ali")
print("Yeni ayın elemanları:", ayin_elemanlari)
print("Şimdi tekrar aynı blokları yazalım.")
eslesme = False
for kisi in bolum:
    if kisi in ayin_elemanlari:
        eslesme = True
        break
if eslesme:
    print("Aramızda ayın elemanı var. Tebrikler!")
else:
    print("Kimse ayın elemanı olamamış.")
