# continue,break ,pass

# pass -> berfungsi sebagai dummy, tidak akan di jalankan atau di eksekusi

# angka = 0

# while angka < 5:
#     angka += 1

#     if angka == 3:
#         pass # ini tidak akan di eksekusi

#     print(angka)

#continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print (f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("oojo!")
        continue #akan membuat loop loncat ke aksi sebelumya

    print("beraksi") #aksi 2

print("selesai")

#progam selesai .
