yapilacaklar = []
while True:
    print("\n--- YAPILACAKLAR LİSTESİ ---")
    print("1.Görev ekle")
    print("2. Listeyi Göster")
    print("3. Görev Sil")
    print("q. Çıkış")
    secim = input("Seçiminiz: ")
    if secim == '1':
        gorev = input("Yapılacak Görevi Yazınız: ")
        yapilacaklar.append(gorev)
        print("Görev başarıyla eklendi")
    elif secim == '2':
        print("\nListeniz:")
        for i in yapilacaklar:
            print("- " + i)
    elif secim == '3':
        silinecek = input("Silmek istediğiniz görevin tam adını yazın: ")
        if silinecek in yapilacaklar:
            yapilacaklar.remove(silinecek)
            print("Görev silindi.")
        else:
            print("Böyle bir görev bulunamadı!")
    elif secim == 'q':
        print("Görüşmek Üzere")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")
