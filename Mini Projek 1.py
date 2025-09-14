print("Catatan Pengeluaran Keuangan Harian Mahasiswa")
print("Nama: Mohammed Rifqy Syahdi")
print("NIM: 2509116037")
print("Kelas: Sistem Informasi A '2025")

#input uang awal
uang_awal = int(input("Masukkan uang sangu awal bulan (Rp): "))

#Menu pilihan
print("Pilih menu:")
print("1. Tambah Pengeluaran & Tampilkan Pengeluaran")
print("2. Tampilkan Semua Pengeluaran & Sisa Uang")
print("3. Keluar")

#list kosong
riwayat_pengeluaran = []

while True:
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1": #kondisi 1
        tanggal = input("Masukan Tanggal (DD-MM-YYYY): ")
        kategori = input("Kategori pengeluaran: ")
        jumlah = int(input("Jumlah pengeluaran (Rp): "))
        riwayat_pengeluaran.append([tanggal, kategori, jumlah])
        print("Pengeluaran berhasil dicatat.")
        print("Pengeluaran:")
        print(tanggal, "|", kategori, "\t|", jumlah)
        print("Total pengeluaran: Rp", jumlah)

    elif pilihan == "2": #kondisi 2
        if not riwayat_pengeluaran:
            print("Belum ada pengeluaran yang dicatat.")
        else:
            print("Riwayat semua pengeluaran:")
            total = 0
            for tanggal, kategori, jumlah in riwayat_pengeluaran:  
                print(tanggal, "|", kategori, "\t|", jumlah)
                total += jumlah
            print("Total pengeluaran: Rp", total)
            sisa_uang = uang_awal - total
            print("Sisa uang: Rp", sisa_uang)

    elif pilihan == "3": #kondisi 3
        print("Terima kasih telah menggunakan program ini.")
        break
        
    else: #kondisi lain
        print("Pilihan tidak valid.")
        break

