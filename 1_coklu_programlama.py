import time
import threading

def program1():
    for i in range(5):
        print(f"Program 1 çalışıyor: {i}")
        time.sleep(1) # Simüle edilen gecikme

def program2():
    for i in range(5):
        print(f"Program 2 çalışıyor: {i}")
        time.sleep(1)

if __name__ == "__main__":
    print("--- Çoklu Programlama (Threading) Başlıyor ---")
    
    # İki programı ayrı iş parçacıkları (threads) olarak tanımlıyoruz
    thread1 = threading.Thread(target=program1)
    thread2 = threading.Thread(target=program2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Tüm programlar tamamlandı!")