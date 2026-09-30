# ilk 10000 asal sayının kaç tanesi 3 ile başlar ve 7 ile biter?

prime_list = list()
prime_list.append(2)
sayi = 3
while True:
    prime = True
    for i in range(2,int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            prime = False
            break
    if prime == True:
        prime_list.append(sayi)
        if len(prime_list) == 10000:
            break
    sayi +=1
liste = list()
for prime in prime_list:
    strprime = str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
        liste.append(prime)
print("İlk 10 bin asal sayıdan 3 ile başlayıp 7 ile bitenler:")
for i in liste:
    print(i)
    