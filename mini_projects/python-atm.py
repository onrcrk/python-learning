import time
ykullanici_adi = input("Hoşgeldiniz. Kayıt olmak için kullanıcı adı giriniz: ")
ysifre = input("Şifre oluşturunuz: ")
sifre_kont = input("Şifrenizi tekrar giriniz: ")
time.sleep(1)
while ysifre != sifre_kont:
    print("Şifreler uyuşmuyor. Lütfen tekrar deneyin.")
    time.sleep(1)
    ysifre = input("Şifre oluşturunuz: ")
    sifre_kont = input("Şifrenizi tekrar giriniz: ")
    time.sleep(1)
print("Hesabınız başarıyla oluşturuldu. Sisteme yönlendiriliyorsunuz...")
time.sleep(2)
bakiye = 0
kullanici_adi = input("Kullanıcı adı: ")
sifre = input("Şifre: ")
while ykullanici_adi != kullanici_adi or ysifre != sifre:
   print("Hatalı giriş. Lütfen tekrar deneyiniz.")
   time.sleep(1)
   kullanici_adi = input("Kullanıcı adı: ")
   sifre = input("Şifre: ")
   time.sleep(1)
istek = ()
while not ("çık" in istek):
    istek = input("Hoşgeldiniz. Bugün ne yapmak istiyorsunsuz?\n(para çekmek, para yatırmak, bakiye sorgulama)\nÇıkmak için 'çık' yazınız: ")
    istek = istek.lower()
    if "çık" in istek:
        time.sleep(1)
        break
    if "bakiye" in istek:
        print("Güncel bakiyeniz: ", bakiye)
        istek = ()
        time.sleep(2)
        continue
    elif "yatır" in istek:
        yatırma = input("Ne kadar yatırmak istiyorsunuz?\nİşlemi iptal etmek için 'iptal' yazınız: ")
        if "iptal" in yatırma:
            time.sleep(1)
            istek = ()
            continue
        try:
            yatırma = int(yatırma)
        except ValueError:
            print("Lütfen geçerli bir değer giriniz.")
            time.sleep(1)
            continue
        time.sleep(1)
        while yatırma <= 0:
            print("Geçersiz tutar. Lütfen geçerli bir sayı girin.")
            time.sleep(1)
            yatırma = int(input("Ne kadar yatırmak istiyorsunuz?: "))
            time.sleep(1)
        bakiye = bakiye + yatırma
        print("Paranız yatırılmıştır. Yeni bakiyeniz: ", bakiye)
        istek = ()
        time.sleep(1)
        continue
    elif "çek" in istek:
        çekme = input("Ne kadar çekmek istiyorsunuz?\nİşlemi iptal etmek için 'iptal' yazınız: ")
        if "iptal" in çekme:
            print("İşlem iptal edildi.")
            istek = ()
            time.sleep(1)
            continue
        try:
            çekme = int(çekme)
        except ValueError:
            print("Lütfen geçerli bir değer giriniz.")
            time.sleep(1)
            continue
        time.sleep(1)
        while çekme <= 0:
            print("Geçersiz tutar. Lütfen geçerli bir sayı girin.")
            time.sleep(1)
            çekme = int(input("Ne kadar çekmek istiyorsunuz?: "))
            time.sleep(1)
        while çekme >= bakiye:
            print("Yeterli bakiyeniz yok. Lütfen geçerli bir tutar giriniz.")
            time.sleep(1)
            çekme = int(input("Ne kadar çekmek istiyorsunuz?: "))
            time.sleep(1)
        bakiye = bakiye - çekme
        print("Paranız çekiliyor... Yeni bakiyeniz: ", bakiye)
        istek = ()
        time.sleep(1)
        continue
    else:
        print("Hatalı giriş. Lütfen tekrar deneyin.")
        istek = ()
        time.sleep(1)
        continue
       
