kelimeler = ["TELESKOP", "YÖRÜNGE", "ASTEROİD", "GALAKSİ", "MARS", "SATÜRN"]
import random
gizli_kelime = random.choice(kelimeler)
harf_sayisi = len(gizli_kelime)
gorunen_kelime = ["_"] * harf_sayisi
print(gorunen_kelime)
can = 8
while can > 0:
    tahmin = input("Lütfen bir harf seçiniz: ").upper()
    if tahmin in gizli_kelime:
        for i in range(len(gizli_kelime)):
            if gizli_kelime[i] == tahmin:
                print("Bingo!")
                gorunen_kelime[i] = tahmin
    else:
        can = can - 1
        print(f"kelimenin içinde {tahmin} harfi bulunmamakta.Tekrar deneyiniz!")
    print(f"Kalan canınız: {can}")
    print("Kelime durumu: "+"".join(gorunen_kelime))
    print("-------------------")
    if "_" not in gorunen_kelime:
        print("TEBRİKLER! KAZANDINIZ!")
        print(f"Kelime şuydu: {gizli_kelime}")
        break
if can == 0:
    print(f"Maalesef kaybettin.Kelime şuydu: {gizli_kelime}")
           
        
                 

    