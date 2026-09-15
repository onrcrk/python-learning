a = 15
b = 23
c = 53
if a > b or c == a or c > b:
    print("Bir veya daha daha fazla koşul sağlandı.")
else:
    print("Koşul sağlanamadı.")
print("'or' bağlacı Türkçede 'veya' anlamına gelmektedir.\nOndan dolayı koşullardan herhangi birisi doğru ise if bloğu çalışır.")
if a < c and a == b:
    print("Koşulların tümü sağlandı.")
else:
    print("Sağlanmayan koşul var.")
print("'and' bağlacı Türkçede 've' anlamına gelmektedir.\nOndan dolayı koşulların hepsi doğru değil ise if bloğu çalışmaz.")

numbers = [1,2,3,4,5,6,7,9]
a = 8
print("Eğer 'a' sayısı 'numbers' listesinin içinde ise 'if' bloğu çalışacak.")
if a in numbers:
    print("Listede var.")
else:
    print("Listede yok.")
print("'a' sayısı listede olmadığı için 'if' bloğu çalışmadı.")

print("'in'i stringlerde de kullanabiliriz. Örneğin:")
isim = "Onur"
a= "o"
if a in isim:
    print("Karakter mevcut.")
else:
    print("Karakter mevcut değil.")
print("'else' bloğu çalıştı çünkü 'o' ile 'O' aynı karakter değil.")

if not a in isim:
    print("Merhaba")
else:
    print("Hayır")
print("'not' eklediğim için koşul yanlışken doğruya dönüştü. 'Merhaba' stringi yazıldı.")

