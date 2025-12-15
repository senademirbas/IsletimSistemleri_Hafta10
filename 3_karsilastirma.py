from multiprocessing import Process
import threading
import time
import os

def kare_hesapla(sayi, yontem):
    pid = os.getpid()
    tid = threading.get_ident()
    print(f"[{yontem}] Sayı: {sayi} -> Kare: {sayi*sayi} | PID: {pid} | Thread ID: {tid}")
    time.sleep(0.5)

def coklu_programlama():
    print("\n--- Çoklu Programlama (Thread) ---")
    sayilar = [1, 2, 3]
    threads = []
    for sayi in sayilar:
        t = threading.Thread(target=kare_hesapla, args=(sayi, "THREAD"))
        threads.append(t)
        t.start()
    for t in threads: t.join()

def coklu_islemci():
    print("\n--- Çoklu İşlemci (Process) ---")
    sayilar = [1, 2, 3]
    processes = []
    for sayi in sayilar:
        p = Process(target=kare_hesapla, args=(sayi, "PROCESS"))
        processes.append(p)
        p.start()
    for p in processes: p.join()

if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()