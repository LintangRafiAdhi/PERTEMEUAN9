# Buat list dengan 5 elemen
list_a = [10, 20, 30, 40, 50]

# Akses list
# Tampilkan elemen ke 3
print("Elemen ke-3:", list_a[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen ke-2 sampai ke-4:", list_a[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", list_a[-1])

# Ubah elemen list
# Ubah elemen ke 4 dengan nilai lainnya
list_a[3] = 45
print("Setelah mengubah elemen ke-4:", list_a)

# Ubah elemen ke 4 sampai dengan elemen terakhir
list_a[3:] = [50, 60, 70]
print("Setelah mengubah elemen ke-4 sampai terakhir:", list_a)

# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_b = list_a[:2]
print("List B:", list_b)

# Tambah list B dengan nilai string
list_b.append("Hello")
print("List B setelah tambah string:", list_b)

# Tambah list B dengan 3 nilai
list_b.extend([1, 2, 3])
print("List B setelah tambah 3 nilai:", list_b)

# Gabungkan list B dengan list A
list_c = list_a + list_b
print("List setelah menggabungkan list A dan B:", list_c)
