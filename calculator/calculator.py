# Hesap makinesi fonksiyonları (Calculator functions)

def toplama(sayilar):  # sayilar = numbers
    return sum(sayilar)

def cikarma(sayilar):  # sayilar = numbers
    sonuc = sayilar[0]  # sonuc = result
    for s in sayilar[1:]:
        sonuc -= s
    return sonuc

def carpma(sayilar):  # sayilar = numbers
    sonuc = 1  # sonuc = result
    for s in sayilar:
        sonuc *= s
    return sonuc

def bolme(sayilar):  # sayilar = numbers
    sonuc = sayilar[0]  # sonuc = result
    for s in sayilar[1:]:
        if s == 0:
            return "Hata: Sıfıra bölme yapılamaz. / Error: Division by zero."
        sonuc /= s
    return sonuc

def us_alma(sayilar):  # sayilar = numbers (exponentiation)
    sonuc = sayilar[0]  # sonuc = result
    for s in sayilar[1:]:
        sonuc **= s
    return sonuc

def mod_alma(sayilar):  # sayilar = numbers
    sonuc = sayilar[0]  # sonuc = result
    for s in sayilar[1:]:
        sonuc %= s
    return sonuc

def ortalama(sayilar):  # sayilar = numbers
    return sum(sayilar) / len(sayilar)

def min_bul(sayilar):  # sayilar = numbers
    return min(sayilar)

def max_bul(sayilar):  # sayilar = numbers
    return max(sayilar)

# Kullanıcıdan sayı listesi alma fonksiyonu
# Function to get a list of numbers from the user
def sayi_listesi_al():  # sayi_listesi = number_list
    sayilar = []  # sayilar = numbers
    print("Sayıları girin (bitirmek için boş bırakın):")
    print("Enter numbers (leave empty to finish):")
    while True:
        giris = input("> ")  # giris = input
        if giris == "":
            break
        try:
            sayi = float(giris)  # sayi = number
            sayilar.append(sayi)
        except ValueError:
            print("Geçersiz giriş. Lütfen sayı girin. / Invalid input. Please enter a number.")
    return sayilar

# Ana fonksiyon / Main function
def main():
    # İşlem seçeneği sözlüğü / Operation mapping
    islemler = {  # islemler = operations
        '+': toplama,
        '-': cikarma,
        '*': carpma,
        '/': bolme,
        '^': us_alma,
        '%': mod_alma,
        'avg': ortalama,
        'min': min_bul,
        'max': max_bul
    }

    print("Kapsamlı Python Hesap Makinesi")
    print("Comprehensive Python Calculator")
    print("İşlem seçenekleri: +, -, *, /, ^, %, avg, min, max")
    print("Available operations: +, -, *, /, ^, %, avg, min, max")

    while True:
        islem = input("Yapmak istediğiniz işlemi seçin (çıkmak için 'q'): ")  # islem = operation
        if islem == 'q':
            print("Çıkılıyor... / Exiting...")
            break
        if islem not in islemler:
            print("Geçersiz işlem. / Invalid operation.")
            continue

        sayilar = sayi_listesi_al()

        if len(sayilar) < 2 and islem not in ['avg', 'min', 'max']:
            print("En az iki sayı girmelisiniz. / You must enter at least two numbers.")
            continue

        sonuc = islemler[islem](sayilar)  # sonuc = result
        print("Sonuç: / Result:", sonuc)

# Program doğrudan çalıştırıldığında main fonksiyonunu başlat
# Start the main function when the script is run directly
if __name__ == "__main__":
    main()
