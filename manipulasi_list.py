# Memanipulasi Data List

# Index 0(-3)  1(-2)  2(-1)
data = ["kam", "kem", "cam"]

# mengambil data dari list ini
data_0 = data[0]
print (f"data pertama (index 0) = {data_0}")

data_tearkhir = data[-1]
print(f"data terakhir adalah = {data_tearkhir}")

data_kam = data[-3]
print (f"data kam = {data_kam}")

# mengambil info jumlah data list
panjang_data = len(data)
print (f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1,"ron")
print(f"data setelah ditambah = \n{data}")

# menambah di akhir list
data.append("jero")
print(f"data setelah ditambah lagi = \n{data}")

# menambah list dengan list
data_baru = ["i", "you", "we"]
data.extend(data_baru)
print(f"gabungan data = \n{data}")

# merubah data
# kita ubah data 2 menjadi kaiser
data[2] = "kaiser"
print (f"data rubah = \n{data}")

# meremove data

data.remove("cam")
print (f"data remove = \n{data}")
# data.remove ("Cam") akan error karena huruf nya harus sama

#meremove data paling akhir
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print (data_akhir)
