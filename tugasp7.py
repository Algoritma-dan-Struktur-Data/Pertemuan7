def fibonacci(n):
    a = 1
    b = 1
    i = 0
    hasil = []

    while i < n:
        hasil.append(a)
        c = a + b
        a = b
        b = c
        i += 1

    return hasil

while True:
    print("PILIHAN MENU\nNIM GENAP")
    print("Menu Pilihan:")
    print("1. Barisan Fibonacci")
    print("2. Perkalian N x M")
    print("0. Keluar")

    pilih = int(input("Pilih menu : "))

    if pilih == 1:
        jumlah = int(input("Masukkan jumlah suku : "))
        data = fibonacci(jumlah)

        print("Barisan fibonacci sebanyak", jumlah, "suku :")
        
        i = 0
        while i < len(data):
            print(data[i], end=", ")
            i += 1
        print()

    elif pilih == 2:
        angka = int(input("Masukkan suatu bilangan bulat : "))
        kali = int(input("Masukkan suatu bilangan pengali : "))

        pola = fibonacci(kali)

        print("Pola fibonacci :", end=" ")
        i = 0
        while i < len(pola):
            print(pola[i], end=" ")
            i += 1
        print()

        hasil = 0
        i = 0
        while i < kali:
            hasil += angka
            i += 1

        print(angka, "x", kali, "=", hasil)

    elif pilih == 0:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")