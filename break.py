# Break

angka = 0

while angka < 10:
    angka += 2
    print(f"angka sekarang -> {angka}")

    if angka == 6:
        print("berhenti")
        break

    # print("lanjut")

# print("progam selesai")

data_int = int(input("Hitung nyampe = "))

angka = 0

while True:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == data_int:
        print(f"Sutop")
        break

    print("lanjut")

print("akhir progam")

