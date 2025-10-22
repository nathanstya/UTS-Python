setoran1 = int(input("Masukkan setoran pertama: "))
setoran2 = int(input("Masukkan setoran kedua: "))
setoran3 = int(input("Masukkan setoran ketiga: "))

if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid! Semua setoran harus lebih dari 0.")
else:
   
    total = setoran1 + setoran2 + setoran3
    print(f"Total setoran = {total}")

    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")
