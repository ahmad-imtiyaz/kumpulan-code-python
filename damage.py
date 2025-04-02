import random

print("Kamu akan menghadapi monster pertama!")
print("Pilih skill yang akan digunakan:")
print("1. Skill Absolute Slash")
print("2. Skill Deduction")
print("3. Skill Double Dagger")

damage = int(input("Mau pakai skill berapa = "))

if damage == 1:
    damage_amount = random.randint(20, 50)  # Rentang damage untuk Absolute Slash
    print(f"Kamu menggunakan Absolute Slash dan memberikan {damage_amount} damage!")
