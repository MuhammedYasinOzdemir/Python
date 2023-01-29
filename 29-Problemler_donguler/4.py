"""Problem 4¶
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
    """
toplam = 0
while True:
    sayi = input("sayi: ")
    if sayi == "q":
        break
    try:
        toplam += int(sayi)
    except ValueError:
        print("lutfen sayi giriniz")
print("\nToplam:{}".format(toplam))
