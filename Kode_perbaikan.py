# Konstanta
DISKON_TINGGI = 0.2
DISKON_SEDANG = 0.1
DISKON_RENDAH = 0.05

BATAS_TINGGI = 100000
BATAS_SEDANG = 50000


def hitung_total_harga(harga, jumlah):
    return harga * jumlah


def hitung_diskon(total_harga):
    if total_harga > BATAS_TINGGI:
        return total_harga * DISKON_TINGGI
    elif total_harga > BATAS_SEDANG:
        return total_harga * DISKON_SEDANG
    else:
        return total_harga * DISKON_RENDAH


def get_status_member(is_member):
    return "Member" if is_member else "Non Member"


def hitung_total_bayar(total_harga, diskon):
    return total_harga - diskon


# Program utama
data_harga = [10000, 20000, 30000]
jumlah_barang = 2
is_member = True

for harga in data_harga:
    total = hitung_total_harga(harga, jumlah_barang)
    diskon = hitung_diskon(total)
    total_bayar = hitung_total_bayar(total, diskon)
    status = get_status_member(is_member)

    print("Total Harga:", total)
    print("Diskon:", diskon)
    print("Total Bayar:", total_bayar)
    print("Status:", status)
    print("-" * 20)