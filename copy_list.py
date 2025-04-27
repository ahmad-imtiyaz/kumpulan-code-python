# Teknik Manipulasi List

a = ["pitik", "bebek", "kucing", "anjing", "ikan"]
print(f"List awal: {a}")

b = a # pass by reference
print(f"List b: {b}")

# kita akan merubah member dari a

#ini akan merubah kedua list
a[0] = "sapi"
b.sort()
print(f"List a: {a}")
print(f"List b: {b}")

# addres dari kedua list a dan b
print(f"Alamat a: {id(a)}")
print(f"Alamat b: {id(b)}")

## menduplikat list dengan copy()

print("Mendupikasi list dengan a.copy()")
c = a.copy() # full duplikat

print(f"addrees a = {hex(id(a))}")
print(f"addrees b = {hex(id(b))}")
print(f"addrees c = {hex(id(c))}")

print(f"List a: {a}")
print(f"List b: {b}")
print(f"List c: {c}")

print("Kita ubah data 0")
c[0] = "kambing"

print(f"List a: {a}")
print(f"List b: {b}")
print(f"List c: {c}")

print("Kita ubah data 1")
a[1] = "kucing"

print(f"List a: {a}")
print(f"List b: {b}")
print(f"List c: {c}")

