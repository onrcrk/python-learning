sinav1 = int(input("İlk sınav notunuzu giriniz: "))
sinav2 = int(input("İkinci sınav notunuzu giriniz: "))
sinav_ort = (sinav1 + sinav2) / 2
sozlu1 = int(input("İlk sözlü notunuzu giriniz: "))
sozlu2 = int(input("İkinci sözlü notunuzu giriniz: "))
sozlu_ort = (sozlu1 + sozlu2) / 2
obp = (sinav_ort + sozlu_ort) / 2
if obp < 50:
    print("Sınıfta kaldınız. OBP'niz:", obp)
elif obp >= 50 and obp < 70:
    print("Sınıfı geçtiniz. OBP'niz:", obp, "Herhangi bir belgeniz bulunmamakta.")
elif obp >= 70 and obp < 85:
    print("Sınıfı geçtiniz. OBP'niz:", obp, "Teşekkür belgesi kazandınız.")
elif obp >= 85 and obp <= 99:
    print("Sınıfı geçtiniz. OBP'niz:", obp, "Takdir belgesi kazandınız.")
elif obp == 100:
    print("Sınıfı geçtiniz. OBP'niz:", obp, "Onur ve Takdir belgesi kazandınız.")
else:
    print("Hatalı not girişi.")
