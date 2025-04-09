#Perulangan (Loop)

#for kondisi :
#aksi

#ini dengan list
angka_list = [1,5,5,4,5,5]
print(angka_list)

for i in angka_list:
    print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

#ini dengan range

angka_range = range(11)

for i in angka_range:
    print(f"i sekarang {i}")

print("akhir dari program 2 \n")
#ini range juga

angka_range = range(2,8)

for i in angka_range:
    print(f"ini adalah i sekarang {i}")
print("akhir dari program 3 \n")

#ini adalah string

data_str = "ini yaazna"

for i in data_str:
    print(i)
print("akhir dari program 4 \n")
