data_angka = [1,2,4,5,7,2,8,9,2,1,6,0,1,4,8,2,3,6]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah data angka 4 = {jumlah_data_4}")
print(f"jumlah data angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["Syilvia", "Pencilgon", "Amanetoa", "Kei"]

print (f"data = {data}")

index_pencilgon =data.index("Pencilgon")
index_kei =data.index("Kei")
print (f"index si Pencilgon = {index_pencilgon}")
print (f"index si Kei = {index_kei}")

# mengurutkan list
print (f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print (f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print (f"data di reverse = \n{data_angka} \n{data}")