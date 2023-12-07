import random
import time

class Kumanda():

    def __init__(self,tv_durumu = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "TRT"):
        self.tv_durumu = tv_durumu
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if (self.tv_durumu == "Açık"):
            print("TV zaten açıkk..")
        else:
            print("TV açılıyor..")
            self.tv_durumu = "Açık"

    def tv_kapat(self):
        if (self.tv_durumu == "Kapalı"):
            print("TV zaten kapalı")
        else:
            print("TV kapanıyor..")
            self.tv_durumu = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi Artır: '>'\nÇıkış: çıkış")

            if (cevap == "<"):
                if (self.tv_ses != 0 ):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            
            elif (cevap == ">"):
                if (self.tv_ses != 31):
                    
                    self.tv_ses += 1

                    print("Ses:",self.tv_ses)
            
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyorr")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi....")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal",self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)
    
    def __str__(self):

        return "TV Durumu: {}\nKanal Listesi: {}\nŞu Anki Kanal: {}\n".format(self.tv_durumu,self.kanal_listesi,self.kanal)

kumanda = Kumanda()    

print("""

TV UYGULAMASI
      
1. TV Aç
      
2. TV Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için 'q'ya basınız. 
""")

while True:

    işlem = input("İşlem giriniz: ")

    if (işlem == "q"):
        print("Program sonlandırılıyor")
        break

    elif (işlem == "1"):
        kumanda.tv_ac
    elif (işlem == "2"):
        kumanda.tv_kapat
    elif (işlem == "3"):
        kumanda.ses_ayarları
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")
        
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal Sayısı:",len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)

    else:
        print("Geçersiz işlem..")
                






