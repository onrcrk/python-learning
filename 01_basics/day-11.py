# fonksiyonlar
def giris(isim):
    print(f"Hoş geldin {isim}! Bugün ne yapmak istersin?")
giris(input("Hitap için isminizi bağışlar mısınız?: "))
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
def sayi_carpimi(x,y):
    print(f"{x} * {y} = {x*y}")
sayi_carpimi(sayi1,sayi2)

def ortalama_hesapla(x,y):
    print(f"{x} ve {y}'nin ortalaması = {x+y/2}")
ortalama_hesapla(sayi1,sayi2)