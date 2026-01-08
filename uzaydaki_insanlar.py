import requests

def uzaydaki_insanlari_bul():
    url = "http://api.open-notify.org/astros.json"
    print("Uzay istasyonuna bağlanılıyor...")
    cevap = requests.get(url)

    if cevap.status_code == 200:
        veri = cevap.json()
        kisi_sayisi = veri["number"]
        print(f"Bağlantı BAŞARILI! Şu an uzayda {kisi_sayisi} insan var.\n")
        print("--- Astronot Listesi ---")
        for astronot in veri["people"]:
            isim = astronot["name"]
            arac = astronot["craft"]
            print(f"İsim:{isim}, (Araç: {arac})")
    else:
        print("HATA! Bağlantı Kurulamadı!")
        
uzaydaki_insanlari_bul()            
