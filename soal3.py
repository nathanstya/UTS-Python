
def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung biaya pengiriman berdasarkan 
    kota, berat, dan opsi asuransi.
    """
    tarif_dasar = {
        "Semarang": 10000,
        "Bandung": 12000,
        "Surabaya": 15000,
        "Yogyakarta": 13000
    }

    if kota not in tarif_dasar:
        return "Kota tidak tersedia."

    ongkir = tarif_dasar[kota] + ( 2000 * berat_kg )
    if asuransi:
        ongkir += 3000

    return ongkir


# 🔹 Contoh pemanggilan fungsi:
print(hitung_ongkir(3, "Semarang"))           # Tanpa asuransi
print(hitung_ongkir(2, "Surabaya", True))    # Dengan asuransi