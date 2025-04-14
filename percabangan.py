# Latihan Perulangan Membuat Segitiga

sisi = 9

# 1. Menggunakan For

# Dummy Variable
print("Awal For")
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

print("Akhir For\f") 

# 2. Menggunakan While

print("Awal While")
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

print("Akhir While\f")

# 3. Hanya Ganjil Saja

print("Awal While")
count = 1
while True:
    if (count%2):
        # Print Jika Ganjil
        print("*" * count)
        count += 1
    else:
        # Akan Kembali Ke Atas Jika Ganjil
        count += 1
        continue

    # Akan Break Jika Count Melebihi Sisi
    if count > sisi:
        break

print("Akhir While\f")
