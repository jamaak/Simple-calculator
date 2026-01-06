def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        raise ZeroDivisionError("Pembagian dengan nol")
    return a / b


def main():
    while True:
        print("\n===== KALKULATOR SEDERHANA =====")
        print("1) Penjumlahan")
        print("2) Pengurangan")
        print("3) Perkalian")
        print("4) Pembagian")
        print("5) Keluar")

        try:
            pilihan = int(input("Pilih (1-5): ").strip())
        except ValueError:
            print("Input tidak valid, masukkan angka 1-5.")
            continue

        if pilihan == 5:
            print("Terima kasih. Keluar.")
            break

        if pilihan not in (1, 2, 3, 4):
            print("Pilihan tidak tersedia.")
            continue

        try:
            x = float(input("Masukkan bilangan pertama: "))
            y = float(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("Input bilangan tidak valid.")
            continue

        try:
            if pilihan == 1:
                hasil = tambah(x, y)
                op = "+"
            elif pilihan == 2:
                hasil = kurang(x, y)
                op = "-"
            elif pilihan == 3:
                hasil = kali(x, y)
                op = "*"
            elif pilihan == 4:
                hasil = bagi(x, y)
                op = "/"

            print(f"Hasil: {x} {op} {y} = {hasil}")
        except ZeroDivisionError:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")


if __name__ == "__main__":
    main()


