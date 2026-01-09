import requests, time
def iss_takip_et():
   url = "http://api.open-notify.org/iss-now.json"
   print("ISS Takip Sistemi Başlatılıyor...")
   print("---------------------------------")
   sayac = 0
   while sayac < 10:
       cevap = requests.get(url)
       veri = cevap.json()
       enlem = veri["iss_position"]["latitude"]
       boylam = veri["iss_position"]["longitude"]
       print(f"Ölçüm {sayac + 1}: Enlem {enlem} | Boylam {boylam}")
       sayac = sayac + 1
       
       time.sleep(3)
   print("-----------------------")
   print("Görev Tamamlandı")
   
iss_takip_et()
       
       