## --- LIST ---

# Kumpulan data numbers
data_angka = [1,3,5,6]
print(data_angka)

# Kumpulan data string
data_string = ["ruby-chan","ayumi-chan","shiki-chan"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, True, True, False]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1, "doki", "suki", True, False, "Garamamraram", 100]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # format range (star,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list pake for loop,list comporehension
list_pake_for = [i ** 2 for i in range(1,10)]
print(list_pake_for)

# membuat list pake for if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

# membuat Bilangan Genap
list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

# Bilangan Ganjil
list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)
