from multiprocessing import Process
import os
import time

def islem_yap(sayi):
    # os.getpid() çalışan işlemin ID'sini verir. Farklı olması farklı çekirdek/işlem demektir.
    pid = os.getpid()
    kare = sayi * sayi
    print(f"İşlemci: {pid} - Sayı: {sayi}, Kare: {kare}")
    time.sleep(2) # Simüle edilen işlem süresi

if __name__ == "__main__":
    print("\n--- Çoklu İşlemci (Multiprocessing) Başlıyor ---")
    
    sayilar = [1, 2, 3, 4, 5]
    islemler = []

    # Her sayı için ayrı bir Process oluşturuyoruz
    for sayi in sayilar:
        islem = Process(target=islem_yap, args=(sayi,))
        islemler.append(islem)
        islem.start()

    # İşlemlerin bitmesini bekle
    for islem in islemler:
        islem.join()

    print("Tüm İşlemler Tamamlandı!")