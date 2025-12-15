# İşletim Sistemleri - Hafta 10: Thread ve Process Çalışmaları

**Öğrenci Adı:** Şehri Sena Demirbaş 
**Ders:** İşletim Sistemleri  
**Konu:** Thread (İş Parçacığı), Multiprocessing (Çoklu İşlemci) ve Amdahl Yasası

Bu depo, 10. hafta ders sunumunda yer alan konuların pekiştirilmesi amacıyla hazırlanan 3 temel uygulama ve Amdahl Yasası hesaplayıcısını içermektedir.

---

## 📂 İçerik ve Açıklamalar

### 1. Çoklu Programlama (Threading)
**Dosya:** `1_coklu_programlama.py`

Bu uygulama, tek bir işlemci üzerinde **eşzamanlılık (concurrency)** kavramını simüle eder. `threading` kütüphanesi kullanılarak iki fonksiyon aynı anda başlatılmıştır.

* **Gözlem:** İşletim sistemi, işlemciyi threadler arasında çok hızlı paylaştırdığı için çıktılar karışık bir sırada gelir.
* **Teorik Bağlam:** Sunumda belirtildiği gibi; threadler aynı işlemin kaynaklarını (kod, veri, dosyalar) paylaşırlar. Bu yöntem, I/O (giriş/çıkış) bekleyen işlemler için performans artışı sağlar.

### 2. Çoklu İşlemci (Multiprocessing)
**Dosya:** `2_coklu_islemci.py`

Bu uygulama, modern çok çekirdekli sistemlerin gücünü kullanarak **paralellik (parallelism)** kavramını gösterir. `multiprocessing` kütüphanesi kullanılmıştır.

* **Gözlem:** Her işlem için işletim sistemi tarafından farklı bir `PID` (Process ID) atanmıştır. Bu, işlemlerin birbirinden bağımsız bellek alanlarında ve farklı çekirdeklerde fiziksel olarak aynı anda çalıştığını kanıtlar.
* **Teorik Bağlam:** Çok çekirdekli sistemlerde her çekirdek işletim sistemi için ayrı bir CPU olarak görülür. Bu sayede gerçek paralellik sağlanır.

### 3. Karşılaştırma (Thread vs Process)
**Dosya:** `3_karsilastirma.py`

Thread ve Process arasındaki yapısal farkı `PID` (Process ID) ve `Thread ID` üzerinden analiz eden çalışmadır.

* **Sonuç:** Thread kullanımında PID'ler aynı kalırken (kaynak paylaşımı), Process kullanımında her işlemin PID'si farklıdır (izole bellek).
* **Çıkarım:** İşlem (Process) oluşturmak, Thread oluşturmaktan daha maliyetlidir ancak tam izolasyon sağlar[cite: 46].

### 4. Amdahl Yasası Hesaplayıcı
**Dosya:** `4_amdahl_yasasi.py`

Çok çekirdekli bir sisteme geçiş yapıldığında elde edilebilecek maksimum teorik hızlanmayı hesaplayan yazılımdır.

* **Kullanılan Formül:** `Hızlanma <= 1 / (S + ((1-S) / N))`
    * *S:* Seri (paralelleştirilemeyen) kısım oranı
    * *N:* Çekirdek sayısı
***Not:** Amdahl yasasına göre, çekirdek sayısını sonsuza kadar artırsak bile, hızlanma her zaman seri kısımla sınırlı kalacaktır

---

## 🚀 Nasıl Çalıştırılır?

Bilgisayarınızda Python yüklü olmalıdır. Terminal veya Komut İstemi'ni açarak ilgili dosyanın bulunduğu dizine gidin:

```bash
# Thread örneğini çalıştırmak için:
python 1_coklu_programlama.py

# Amdahl yasası hesaplayıcısı için:
python 4_amdahl_yasasi.py