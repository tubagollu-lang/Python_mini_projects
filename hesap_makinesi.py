def topla(x, y):
    return x + y
def cikar(x, y):
    return x - y
def carp(x, y):
    return x * y
def bol(x, y):
    return x / y
    
print("Hesap makinesi açılıyor...")
print("İşlemler: 1.Topla , 2.Çıkar , 3,Çarp , 4.Böl , q.çıkış")

while True:
    secim = input("İstediğin işlemin saysıını giriniz: ")
    if secim == 'q':
        print("Hesap makinesinden çıkılıyor...")
        break
   if secim in ['1','2','3','4']:
       sayi1 = float(input("Birinci sayıyı giriniz: "))
       sayi2 = float(input("ikinci sayıyı giriniz: "))
       if secim == '1':
           sonuc = topla(sayi1 , sayi2)
           print(f"sonuç: {sonuc}")
       elif secim == '2':
           sonuc = cikar(sayi1, sayi2)
           print(f"sonuç: {sonuc}")
       elif secim == '3':
           sonuc = carp(sayi1, sayi2)
           print(f"sonuç: {sonuc}")
       elif secim == '4':
           sonuc == bol(sayi1, sayi2)
           print(f"sonuç: {sonuc}")
       else:
           print("Geçersiz bir giriş yaptınız, lütfen tekrar deneyiniz.")    