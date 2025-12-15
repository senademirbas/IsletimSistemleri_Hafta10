def amdahl_yasasi_hesapla(seri_oran, cekirdek_sayisi):
    """
    Amdahl Yasasına göre maksimum hızlanmayı hesaplar.
    S: Seri oran (0 ile 1 arasında, örn: %25 için 0.25)
    N: Çekirdek sayısı
    """
    if seri_oran < 0 or seri_oran > 1:
        return "Hata: Seri oran 0 ile 1 arasında olmalıdır."
    
    # Formül: 1 / (S + ((1 - S) / N))
    parallel_oran = 1 - seri_oran
    hizlanma = 1 / (seri_oran + (parallel_oran / cekirdek_sayisi))
    return round(hizlanma, 4)

if __name__ == "__main__":
    print("--- Amdahl Yasası Hesaplayıcı ---")
    
    # Kullanıcıdan veri alma
    try:
        s_input = float(input("Uygulamanın seri kısmını girin (Örn: %25 için 0.25 yazın): "))
        n_input = int(input("İşlemci çekirdek sayısını girin (N): "))
        
        sonuc = amdahl_yasasi_hesapla(s_input, n_input)
        
        print(f"\nSonuçlar:")
        print(f"Seri Kısım (S): {s_input}")
        print(f"Paralel Kısım (1-S): {1 - s_input}")
        print(f"Çekirdek Sayısı (N): {n_input}")
        print("-" * 30)
        print(f"Tahmini Maksimum Hızlanma: {sonuc} kat")
        
        # Sonsuz Çekirdek durumunu kontrol etme,
        max_teorik = 1 / s_input
        print(f"Teorik Limit (Sonsuz Çekirdek olsa bile): {max_teorik} kat")
        
    except ValueError:
        print("Lütfen geçerli sayısal değerler giriniz.")