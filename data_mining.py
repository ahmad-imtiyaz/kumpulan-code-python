import pandas as pd
import os
print("Current working directory:", os.getcwd())

# Load dataset
df = pd.read_csv("d:/LATIHAN/email_spam_indo.csv")

# Cetak nama kolom untuk memastikan kolom yang tersedia dalam dataset
print("Kolom dalam dataset:", df.columns)

# Pastikan nama kolom sesuai
# Misalnya: kolom teks = "text", kolom label = "label"
# Gantilah jika nama kolom berbeda

# Ubah semua teks menjadi huruf kecil untuk pencocokan yang konsisten
df['Kategori'] = df['Kategori'].str.lower()
df['Pesan'] = df['Pesan'].astype(str).str.lower()

# Hitung jumlah kata "gratis" pada email spam
spam_gratis_count = df[df['Kategori'] == 'spam']['Pesan'].str.count(r'\bgratis\b').sum()

# Hitung jumlah kata "gratis" pada email ham
ham_gratis_count = df[df['Kategori'] == 'ham']['Pesan'].str.count(r'\bgratis\b').sum()

print(f'Jumlah kata "gratis" dalam email SPAM: {spam_gratis_count}')
print(f'Jumlah kata "gratis" dalam email HAM: {ham_gratis_count}')
