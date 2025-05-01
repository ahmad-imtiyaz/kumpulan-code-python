import random

def main():
    print("Selamat datang di permainan angka keberuntungan!")
    print("Pilih angka: 1, 2, atau 3")

    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan not in [1, 2, 3]:
        print("Pilihan tidak valid. Silakan pilih angka 1, 2, atau 3.")
        return

    probabilitas = random.random()

    if probabilitas < 0.5:
        print(f"Selamat! Anda memilih angka {pilihan} dan Anda menang!")
    else:
        print(f"Sayang sekali, Anda memilih angka {pilihan} dan Anda kalah. Coba lagi!")

if __name__ == "__main__":
    main()