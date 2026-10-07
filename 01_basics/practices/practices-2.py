# 3 basamaklı sayıların kaç tanesi rakamlarının küplerinin toplamına eşittir?
eslesme = 0
liste = []
for i in range(100,1000):
    sayistr = str(i)
    kup_toplami = 0
    for x in sayistr:
        rakam = 0
        x_int = int(x)
        rakam = x_int ** 3
        kup_toplami += rakam
    if kup_toplami == i:
        liste.append(i)
        eslesme += 1
    else:
        continue
print(eslesme)
print(liste)