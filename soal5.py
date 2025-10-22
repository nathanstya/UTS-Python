# presensi_uts.py
import csv
import json
import logging
from pathlib import Path
from typing import List, Dict

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "presensi.csv"
JSON_PATH = DATA_DIR / "ringkasan.json"

SAMPLE_ROWS: List[Dict[str, str]] = [
    {"nim": "230101001", "nama": "Ani",   "hadir_uts": "1"},
    {"nim": "230101002", "nama": "Budi",  "hadir_uts": "0"},
    {"nim": "230101003", "nama": "Caca",  "hadir_uts": "1"},
]


def main():
    # 1) Pastikan folder data ada
    try:
        DATA_DIR.mkdir(exist_ok=True)
    except Exception as e:
        logging.error("Gagal membuat/mengakses folder '%s': %s", DATA_DIR, e)
        return

    # 2) Menulis CSV (header + 3 baris)
    try:
        logging.info("Mulai menulis CSV ke '%s' ...", CSV_PATH)
        with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nim", "nama", "hadir_uts"])
            writer.writeheader()
            for row in SAMPLE_ROWS:
                writer.writerow(row)
        logging.info("CSV berhasil ditulis.")
    except Exception as e:
        logging.error("Gagal menulis CSV: %s", e)
        return

    # 3) Membaca kembali CSV, hitung total/hadir/persentase
    try:
        logging.info("Membaca CSV dari '%s' ...", CSV_PATH)
        with CSV_PATH.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        total = len(rows)
        hadir = 0
        for r in rows:
            try:
                hadir += int(r.get("hadir_uts", "0"))
            except ValueError:
                # jika nilai bukan integer, anggap hadir = 0 untuk baris itu
                logging.warning("Nilai hadir_uts tidak valid untuk NIM %s: %s", r.get("nim"), r.get("hadir_uts"))
        persentase = (hadir / total * 100) if total > 0 else 0.0

        ringkasan = {
            "total_mahasiswa": total,
            "jumlah_hadir": hadir,
            "persentase_hadir": round(persentase, 2)
        }

        logging.info("Pembacaan CSV selesai. Total=%d, Hadir=%d, Persentase=%.2f%%", total, hadir, persentase)
    except FileNotFoundError:
        logging.error("File CSV tidak ditemukan: %s", CSV_PATH)
        return
    except Exception as e:
        logging.error("Gagal membaca atau memproses CSV: %s", e)
        return

    # 4) & 5) Menyimpan ringkasan ke JSON dengan proteksi try/except dan logging
    try:
        logging.info("Menyimpan ringkasan ke '%s' ...", JSON_PATH)
        with JSON_PATH.open("w", encoding="utf-8") as f:
            json.dump(ringkasan, f, indent=2, ensure_ascii=False)
        logging.info("Ringkasan berhasil disimpan.")
    except Exception as e:
        logging.error("Gagal menyimpan ringkasan ke JSON: %s", e)
        return

    # Tampilkan ringkasan singkat di akhir (opsional)
    print("\nRingkasan presensi:")
    print(json.dumps(ringkasan, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()