sinav = int(input("Sınavdan aldığınız notu giriniz: "))
sozlu = int(input("Sözlü notunuzu giriniz: "))
obp = (sinav + sozlu) // 2
if obp < 50:
    print("Sınıfta kaldınız.")
elif obp >= 50 and obp < 70:
    print("Sınıfı geçtiniz. Herhangi bir belgeniz bulunmamakta.")
elif obp >= 70 and obp < 85:
    print("Sınıfı geçtiniz. Teşekkür belgesi kazandınız.")
elif obp >= 85 and obp <= 99:
    print("Sınıfı geçtiniz. Takdir belgesi kazandınız.")
elif obp == 100:
    print("Sınıfı geçtiniz. Onur ve Takdir belgesi kazandınız.")
else:
    print("Hatalı not girişi.")
