print("Şimdi sözlükler (dictionaries) kısmındayız. Bir sözlük oluşturalım.")
b = {"marka" : "apple", "model" : "air", "yıl" : 2022, "özellikler" : ["M2 işlemci", "256 hafıza", "16 ram"]}
print(b)
print("İlk kelimeler string veya integer olmak zorunda. Adına anahtar (key) diyoruz.\nİkinci kelimelere ise değer (value) adı veriyoruz. Değerler her şey olabilir.")
print("Sözlükteki marka:", b["marka"])

print("Sözlükteki anahtarları nasıl çağıracağmızı gördük. Şimdi o anahtarı nasıl değiştireceğimizi görelim.")
b["marka"] = "gamegaraj"
print("Yeni marka:", b["marka"])

print("Sözlükteki bir değil birden fazla anahtarı değiştirmek istersek şöyle yapmalıyız.")
b.update({"marka" : "hp", "model" : "victus", "yıl" : 2024})
print("Güncel sözlük:", b)

print("Yeni bir anahtar eklemek istediğimizde az önce anahtarı değiştirmek için kullandığımız yöntemi kullanacağız.")
b["klavye"] = "Türkçe Q"
print(b)
print("Gördüğünüz üzere 'klavye' anahtarımız eklendi. Ama şimdi silmek istiyorum.")
del b["klavye"]
print("Artık sözlüğümüz tekrardan:", b)

print("Sözlüğümdeki anahtarları tek tek görmek için 'for' komutuna başvuruyorum.")
for x in b:
    print(x)
print("Bu bana anahtarları yazdırdı. Şimdi de değerlerini tek tek görmek istiyorum.")
for y in b:
    print(b[y])

print("Şimdi anahtları sıralayacak komutumuzu yazıyoruz.")
print(b.keys())
print("Bu komut bana anahtarları verdi. Değerler için de aynısını yapalım.")
print(b.values())

print("Şimdi de sözlüğümüzdeki anahtar ve değerleri tekli bir arada yazdıralım.")
for k,l in b.items():
    print(k,":",l)
print("'items' komutu bize sözlüğümüzdeki anahtar ve değerleri ikili olarak verir.\nBu sayede 'for' döngüsü ile ikili gruplar halinde değerlerimizi tek tek yazdırabiliriz.")

print("Sözlüğümüzde olan veya olmayan bir anahtarı çekmek istediğimizde şöyle yapıyoruz:")
print(b.get("model"))
print("'model' anahtarını getirdim ve olduğu için değerini verdi. Olmayan bir anahtar için yapsaydım?")
print(b.get("renk"))
print("Gördüğünüz üzere 'None' dedi. Çünkü öyle bir anahtarımız yok.")

print("Bir anahtar bulunamadığında yazdırmasını istediğim mesajı virgül koyup yazarsam bana o mesajı yazdırır.")
print(b.get("renk","Ne yazık ki böyle bir anahtar yok."))
print("'renk' anahtarını aradım. Olmadığı için istediğim mesajı bana yazdırdı.")