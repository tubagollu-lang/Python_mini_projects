def topla(x, y):
    return x + y
def cikar(x, y):
    return x - y
def carp(x, y):
    return x * y
def bol(x, y):
    return x / y
#Sonradan hata engelleme eklendi.    
def bol(x, y):
    if y == 0:
        return "Hata: Bir sayı 0'a bölünemez!"
    return x / y    
    
print("Hesap makinesi açılıyor...")
print("İşlemler: 1.Topla , 2.Çıkar , 3.Çarp , 4.Böl , q.Çıkış")

while True:
    secim = input("İstediğin işlemin numarasını giriniz: ")
    
    if secim == 'q':
        print("Hesap makinesinden çıkılıyor...")
        break
    
    elif secim in ['1','2','3','4']:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
        
        if secim == '1':
            sonuc = topla(sayi1 , sayi2)
            print(f"Sonuç: {sonuc}")
        elif secim == '2':
            sonuc = cikar(sayi1, sayi2)
            print(f"Sonuç: {sonuc}")
        elif secim == '3':
            sonuc = carp(sayi1, sayi2)
            print(f"Sonuç: {sonuc}")
        elif secim == '4':
            sonuc = bol(sayi1, sayi2) 
            print(f"Sonuç: {sonuc}")
            
    else:
        print("Geçersiz bir giriş yaptınız, lütfen tekrar deneyiniz.")
