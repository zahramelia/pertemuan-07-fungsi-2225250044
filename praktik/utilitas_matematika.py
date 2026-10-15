
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def baca_nonnegatif():
    while True:
        try:
            n = int(input("Masukkan bilangan bulat nonnegatif: "))
            if n >= 0:
                return n
            print("Bilangan harus nonnegatif.")
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        print("Luas =", luas_persegi_panjang(p, l))

    elif pilihan == "2":
        a = float(input("Alas: "))
        t = float(input("Tinggi: "))
        print("Luas =", luas_segitiga(a, t))

    elif pilihan == "3":
        n = baca_nonnegatif()
        print("Jumlah =", jumlah_n(n))

    elif pilihan == "4":
        n = baca_nonnegatif()
        print("Faktorial =", faktorial(n))

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
