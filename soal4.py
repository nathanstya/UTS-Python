def jadwal_hari(hari):
    """Menampilkan jadwal kuliah berdasarkan hari yang dicek satu per satu dari list."""
    jadwal = {
        "Senin": ["Teknik Digital"],
        "Selasa": ["Pemograman Python"],
        "Rabu": ["Metopen"],
        "Kamis": ["Pengantar IOT"],
        "Jumat": ["Libur"]
    }

    # Mengecek apakah hari ada di dalam jadwal
    if hari in jadwal:
        print(f"Jadwal kuliah hari {hari}:")
        for mata_kuliah in jadwal[hari]:
            print("-", mata_kuliah)
    else:
        print("Hari tidak ditemukan dalam jadwal.")


# ===== Contoh Pemanggilan Fungsi =====
jadwal_hari("Senin")
print()
jadwal_hari("Rabu")
