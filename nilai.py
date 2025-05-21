def cek_kkm(nilai, kkm = 75):
    if nilai >= kkm:
        return "Selamat! Nilai Anda sudah mencapai atau melebihi KKM."
    else:
        return "Maaf, nilai Anda belum mencapai KKM."

def main():
    print("Program Cek KKM")
    try:
        nilai = float(input("Masukkan nilai Anda: "))
        hasil = cek_kkm(nilai)
        print(hasil)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()
