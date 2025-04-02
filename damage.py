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
elif damage == 2:
    damage_amount = random.randint(10, 30)  # Rentang damage untuk Deduction
    print(f"Kamu menggunakan Deduction dan memberikan {damage_amount} damage!")
elif damage == 3:
    damage_amount = random.randint(15, 40)  # Rentang damage untuk Double Dagger
    print(f"Kamu menggunakan Double Dagger dan memberikan {damage_amount} damage!")
else:
    print("Skill tidak valid!")

# Tambahan: Menampilkan sisa HP monster (opsional)
monster_hp = 100  # Asumsi HP monster awal
monster_hp -= damage_amount if 'damage_amount' in locals() else 0  # Mengurangi HP monster
print(f"Sisa HP monster: {monster_hp}")
