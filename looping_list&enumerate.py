# looping dari list

# for loop
print("for loop")
kumpulan_angka = [1, 2, 3, 4, 5]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["andi", "budi", "caca", "dani", "euis"]

for nama in peserta:
    print(f"nama = {nama}") 

# for loop dan range
print("\nfor loop dan range")
kumpulan_angka = [1, 2, 3, 4, 5]

panjaang = len(kumpulan_angka)

for i in range(panjaang):
    print(f"angka = {kumpulan_angka[i]}")

# while loop
print("\nwhile loop")
kumpulan_angka = [1, 2, 3, 4, 5]

panjaang = len(kumpulan_angka)
i = 0

while i < panjaang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1  

# list comprehension
print("\nlist comprehension")
data = ["yazna",2,6,1,"pencilgon"]

[print(f"data = {i}") for i in data]

angka = [1, 2, 3, 4, 5]

angka_kuadrat = [i**2 for i in angka]
print(f"\nangka kuadrat = {angka_kuadrat}")   


#enumerate
print("\nenumerate")
data_list = ["yazna",2,6,1,"pencilgon"]

for index, data in enumerate(data_list):
    print(f"index ke = {index} data = {data}")