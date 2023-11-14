from prettytable import PrettyTable

def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    return nilai_akhir

# Inisialisasi list untuk menyimpan data
data_mahasiswa = []

while True:
    # Meminta input data
    nomor_induk = input("Masukkan nomor induk mahasiswa: ")
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS:"))

    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    # Menambahkan data ke dalam list
    data_mahasiswa.append({
        'Nomor Induk': nomor_induk,
        'Nama': nama,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

    # Menanyakan apakah ingin menambahkan data lagi
    jawaban = input("Tambahkan data lagi? (y/t): ")
    if jawaban.lower() != 'y':
        break

# Membuat tabel menggunakan PrettyTable
tabel = PrettyTable()
tabel.field_names = ["No. Induk", "Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"]

# Menambahkan data ke dalam tabel
for mahasiswa in data_mahasiswa:
    tabel.add_row([
        mahasiswa['Nomor Induk'],
        mahasiswa['Nama'],
        mahasiswa['Tugas'],
        mahasiswa['UTS'],
        mahasiswa['UAS'],
        mahasiswa['Nilai Akhir']
    ])

# Menampilkan tabel
print("\nDaftar Nilai Mahasiswa:")
print(tabel)
