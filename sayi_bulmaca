import random
gizli_sayi = random.randint(1, 100)
can = 5
while can > 0:
    tahmin = int(input("Tahmininiz nedir?: "))
    if tahmin == gizli_sayi:
        print("Oyunu kazandınız,Tebrikler!")
        break
    elif tahmin < gizli_sayi:
        print("Sayıyı bulamadınız,daha büyük bir sayı seçerek tekrar deneyiniz.")
        can = can - 1
        print(f"Kalan canınız: {can}")
    else:
        print("Sayıyı bulamadınız,daha küçük bir sayı seçerek tekrar deneyiniz.")
        can = can - 1
        print(f"Kalan canınız: {can}")
if can == 0:
    print("Oyunu kaybettiniz,Şansına küs dostum!")
        
        