# Comprehensive Python Calculator

This project is a comprehensive Python calculator capable of performing basic mathematical operations. It takes a list of numbers from the user and returns the result based on the selected operation.

## Features

* **Addition:** Adds all the entered numbers.
* **Subtraction:** Subtracts all subsequent numbers from the first number.
* **Multiplication:** Multiplies all the entered numbers.
* **Division:** Divides the first number by all subsequent numbers. Checks for division by zero errors.
* **Exponentiation:** Raises the first number to the power of the subsequent numbers.
* **Modulo:** Returns the modulo of the first number with respect to the subsequent numbers.
* **Average:** Calculates the average of the entered numbers.
* **Find Minimum:** Finds the smallest number among the entered numbers.
* **Find Maximum:** Finds the largest number among the entered numbers.
* **User-Friendly Interface:** Allows users to easily enter numbers and operations.
* **Error Handling:** Handles invalid inputs and division by zero errors.

## How to Use

1.  Download this Python file (with the `.py` extension) to your computer.
2.  Open a terminal or command prompt and navigate to the directory where the file is located.
3.  Run the following command:
    ```bash
    python filename.py
    ```
    (Here, `filename.py` is the name of the file you downloaded.)
4.  The program will ask you to select the operation you want to perform. Enter one of the operation options (`+, -, *, /, ^, %, avg, min, max`). Press `q` to exit.
5.  After selecting an operation, the program will prompt you to enter the numbers. Press Enter after each number. Leave an empty line (just press Enter) to finish entering numbers.
6.  The program will display the result based on the operation you selected.
7.  You can enter another operation option to perform a new calculation.

## Functions

* `toplama(sayilar)`: Returns the sum of a list of numbers.
* `cikarma(sayilar)`: Returns the difference of a list of numbers (subtracted from the first number).
* `carpma(sayilar)`: Returns the product of a list of numbers.
* `bolme(sayilar)`: Returns the division of a list of numbers (the first number divided by the others). Returns an error message for division by zero.
* `us_alma(sayilar)`: Returns the result of raising the first number to the power of the other numbers.
* `mod_alma(sayilar)`: Returns the modulo of the first number with respect to the other numbers.
* `ortalama(sayilar)`: Returns the average of a list of numbers.
* `min_bul(sayilar)`: Returns the smallest number in a list of numbers.
* `max_bul(sayilar)`: Returns the largest number in a list of numbers.
* `sayi_listesi_al()`: Takes numbers from the user and creates a list.
* `main()`: Manages the main program loop, prompts the user for operation selection and number input, and then displays the result.

## Contributions

Contributions are welcome! You can create pull requests for bug fixes, new features, or improvements.



# Kapsamlı Python Hesap Makinesi

Bu proje, temel matematiksel işlemleri gerçekleştirebilen kapsamlı bir Python hesap makinesidir. Kullanıcıdan bir sayı listesi alır ve seçilen işleme göre sonucu döndürür.

## Özellikler

* **Toplama:** Girilen tüm sayıları toplar.
* **Çıkarma:** İlk sayıdan sonraki tüm sayıları çıkarır.
* **Çarpma:** Girilen tüm sayıları çarpar.
* **Bölme:** İlk sayıyı sonraki tüm sayılara böler. Sıfıra bölme hatasını kontrol eder.
* **Üs Alma:** İlk sayının sonraki sayılarla üssünü alır.
* **Mod Alma:** İlk sayının sonraki sayılara göre modunu alır.
* **Ortalama:** Girilen sayıların ortalamasını hesaplar.
* **Minimum Bulma:** Girilen sayılar arasındaki en küçük sayıyı bulur.
* **Maksimum Bulma:** Girilen sayılar arasındaki en büyük sayıyı bulur.
* **Kullanıcı Dostu Arayüz:** Kullanıcıdan sayıları ve işlemleri kolayca girmesini sağlar.
* **Hata Yönetimi:** Geçersiz girişleri ve sıfıra bölme hatalarını ele alır.

## Nasıl Kullanılır

1.  Bu Python dosyasını (`.py` uzantılı) bilgisayarınıza indirin.
2.  Bir terminal veya komut istemi açın ve dosyanın bulunduğu dizine gidin.
3.  Aşağıdaki komutu çalıştırın:
    ```bash
    python dosya_adı.py
    ```
    (Burada `dosya_adı.py` indirdiğiniz dosyanın adıdır.)
4.  Program size yapmak istediğiniz işlemi soracaktır. İşlem seçeneklerinden birini girin (`+, -, *, /, ^, %, avg, min, max`). Çıkmak için `q` tuşuna basın.
5.  İşlem seçtikten sonra, program sizden sayıları girmenizi isteyecektir. Her sayıyı girdikten sonra Enter tuşuna basın. Sayı girişini bitirmek için boş bir satır bırakın (sadece Enter tuşuna basın).
6.  Program, seçtiğiniz işleme göre sonucu gösterecektir.
7.  Yeni bir işlem yapmak için tekrar bir işlem seçeneği girebilirsiniz.

## Fonksiyonlar

* `toplama(sayilar)`: Bir sayı listesinin toplamını döndürür.
* `cikarma(sayilar)`: Bir sayı listesinin farkını döndürür (ilk sayıdan diğerleri çıkarılır).
* `carpma(sayilar)`: Bir sayı listesinin çarpımını döndürür.
* `bolme(sayilar)`: Bir sayı listesinin bölümünü döndürür (ilk sayı diğerlerine bölünür). Sıfıra bölme durumunda hata mesajı verir.
* `us_alma(sayilar)`: İlk sayının diğer sayılarla üssünü döndürür.
* `mod_alma(sayilar)`: İlk sayının diğer sayılara göre modunu döndürür.
* `ortalama(sayilar)`: Bir sayı listesinin ortalamasını döndürür.
* `min_bul(sayilar)`: Bir sayı listesindeki en küçük sayıyı döndürür.
* `max_bul(sayilar)`: Bir sayı listesindeki en büyük sayıyı döndürür.
* `sayi_listesi_al()`: Kullanıcıdan sayıları alarak bir liste oluşturur.
* `main()`: Ana program döngüsünü yönetir, kullanıcıdan işlem seçmesini ve sayıları girmesini ister, ardından sonucu görüntüler.

## Katkılar

Katkılarınız memnuniyetle karşılanır! Hata düzeltmeleri, yeni özellikler veya iyileştirmeler için çekme istekleri oluşturabilirsiniz.
