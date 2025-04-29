data_0 =[2,5]
data_1 =[3,4,2]

data_list_biasa = [1,2,3,4]

print(f"list biasa: {data_list_biasa}")

list_2d = [data_0, data_1]

print(f"list 2d: {list_2d}")

#contoh penggunaan

peserta_0 = ["andi", 20, "laki-laki"]
peserta_1 = ["budi", 21, "laki-laki"]   
peserta_2 = ["cici", 22, "perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama: {peserta[0]}")
    print(f"Umur: {peserta[1]}")
    print(f"Jenis Kelamin: {peserta[2]}")
    print("-----\n")

# dengan refrence

list_copy = list_peserta.copy()
print(f"list copy = {list_copy}")
peserta_0[0] = "doni"
print(f"list copy = {list_copy}")
print(f"list peserta = {list_peserta}")