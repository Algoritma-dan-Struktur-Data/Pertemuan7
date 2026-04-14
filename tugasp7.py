def fibonacci(n):
    a, b = 1, 1
    hasil = []

    for i in range(n):
        hasil.append(a)
        a, b = b, a + b

    return hasil

while True:
    print("\nNIM GENAP")
    print("Pilihan menu:")
    print("1. Barisan Fibonacci")
    print("2. Perkalian (M x N)")
    print("0. Keluar")

    pilih = int(input("Pilih menu : "))

    if pilih == 1:
        jumlah = int(input("Masukkan jumlah suku : "))
        fibo = fibonacci(jumlah)

        print("Barisan fibonacci sebanyak", jumlah, "suku :")
        for angka in fibo:
            print(angka, end=", ")
        print()

    elif pilih == 2:
        M = int(input("Masukkan bilangan bulat (M) : "))
        N = int(input("Masukkan bilangan pengali (N) : "))

        pola = fibonacci(N)
        print("Pola fibonacci :", end=" ")
        for angka in pola:
            print(angka, end=" ")
        print()

        hasil = 0
        for i in range(N):
            hasil += M

        print("Hasil akhir :", M, "x", N, "=", hasil)

    elif pilih == 0:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")
