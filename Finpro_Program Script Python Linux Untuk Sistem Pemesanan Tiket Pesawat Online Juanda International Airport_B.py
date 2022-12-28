
# List Jadwal Penerbangan Pesawat
print ("--------------------------------------------------------------------------------------")
print ("|     JADWAL PENERBANGAN PESAWAT JUANDA INTERNATIONAL AIRPORT SURABAYA HARI INI      |")
print ("--------------------------------------------------------------------------------------")
print ("| Kode penerbangan | Tujuan    | Berangkat | Tiba      | Harga Tiket    | Maskapai   |")
print ("--------------------------------------------------------------------------------------")
print ("| B11		   | Bali      | 06.00 WIB | 07.13 WIB | Rp. 455.000    | Lion Air   |")
print ("| B12              | Bali      | 06.05 WIB | 07.20 WIB | Rp. 560.000    | Garuda IND |")
print ("| K11              | Kupang    | 08.00 WIB | 10.16 WIB | Rp. 780.000    | Lion Air   |")
print ("| K12              | Kupang    | 08.20 WIB | 10.45 WIB | Rp. 890.000    | Sriwijaya  |")
print ("| Jk1              | Jakarta   | 10.00 WIB | 11.12 WIB | Rp. 550.000    | Air Asia   |")
print ("| JK2              | Jakarta   | 11.05 WIB | 12.18 WIB | Rp. 750.000    | Batik Air  |")
print ("| Y11              | Samarinda | 13.25 WIB | 15.58 WIB | Rp. 1.150.000  | Garuda IND |")
print ("| Y12              | Samarinda | 14.00 WIB | 16.12 WIB | Rp. 950.000    | CITILINK   |")
print ("| G11              | Jogja     | 16.00 WIB | 17.15 WIB | Rp. 550.000    | Lion Air   |")
print ("| G12              | Jogja     | 16.23 WIB | 17.35 WIB | Rp. 750.000    | Lion Air   |")
print ("| S11              | Semarang  | 17.00 WIB | 17.45 WIB | Rp. 450.000    | Lion Air   |")
print ("| S12              | Semarang  | 18.00 WIB | 18.55 WIB | Rp. 550.000    | Batik Air  |")
print ("| P11              | Jayapura  | 16.00 WIB | 19.25 WIB | Rp. 1.950.000  | Air Asia   |")
print ("| R11              | Singapore | 16.00 WIB | 19.85 WIB | Rp. 1.450.000  | Garuda IDN |")
print ("| M11              | Maluku    | 18.00 WIB | 19.55 WIB | Rp. 1.000.000  | CITILINK   |")
print ("| L11              | LOMBOK    | 19.00 WIB | 20.15 WIB | Rp. 850.000    | Lion Air   |")
print ("| D11              | DUBAI     | 19.10 WIB | 6.15 WIB  | Rp. 15.550.000 | Garuda IDN |")
print ("| T11              | Tokyo     | 21.00 WIB | 07.15 WIB | Rp. 10.000.000 | Qatar Air  |")
print ("| SS1              | SEOUL     | 22.00 WIB | 08.15 WIB | Rp. 20.000.000 | Seoul Air  |")
print ("| SY1              | SYDNEY    | 16.00 WIB | 23.15 WIB | Rp. 4.000.000  | Air Asia   |")
print ("| KK1              | MEKKAH    | 06.00 WIB | 20.15 WIB | Rp. 17.000.000 | Garuda IDN |")
print ("| NW1              | NEW YORK  | 07.00 WIB | 23.15 WIB | Rp. 30.000.000 | USA Air    |")
print ("--------------------------------------------------------------------------------------")


# Input data pembeli 
print ("--------------------------------------------------------------------------------------")
print ("| Masukkan Biodata Untuk Pemesanan Tiket Pesawat                                     |")
print ("--------------------------------------------------------------------------------------")

NIK = input("Masukkan Nomor Kependudukan Anda : ")
Nama = input("Masukkan Nama Lengkap : ")
Alamat = input("Masukkann Alamat Anda : ")
HP = input("Masukkan Nomor Handphone Anda: ")
Tujuan = input("Masukkan Kode Tujuan penerbangan: ")
tujuan = []  	
maskapai =  []
harga = []
waktu = []
tiba =  []

# Kode python program untuk pemilihan kode pesawt
if Tujuan == "B11" :
	tujuan.append("Bali")
	maskapai.append("Lion Air")
	waktu.append("06.00 WIB")
	tiba.append("07.17 WIB") 
	harga = 455000
elif Tujuan == "B12" :
	tujuan.append("Bali")
	maskapai.append("Garuda Indonesia")
	waktu.append("06.05 WIB")
	tiba.append("07.20 WIB")
	harga = 560000
elif Tujuan == "K11" :
	tujuan.append("Kupang")
	maskapai.append("Lion Air")
	waktu.append("08.00 WIB")
	tiba.append("10.16 WIB")
	harga = 780000
elif Tujuan ==  "K12" :
	tujuan.append("Kupang")
	maskapai.append("Sriwijaya Air")
	waktu.append("08.20 WIB")
	tiba.append("10.45 WIB")
	harga = 890000
elif Tujuan ==  "Jk1" :
	tujuan.append("Jakarta")
	maskapai.append("Air Asia")
	harga = 550000
	waktu.append("10.00 WIB")
	tiba.append("11.12 WIB")
elif Tujuan ==  "Jk2" :
	tujuan.append("Jakarta")
	maskapai,append("Batik Air")
	waktu.append("11.05 WIB")
	tiba.append("12.18 WIB")
	harga = 750000
elif Tujuan ==  "Y11" :
	tujuan.append("Samarinda")
	harga = 1150000
	waktu.append("13.25 WIB")
	tiba.append("15.58 WIB")
	maskapai.append("Garuda Indoensia")
elif Tujuan ==  "Y12" :
	tujuan.append("Samarinda")
	waktu.append("14.00 WIB")
	tiba.append("16.12 WIB")
	harga = 950000
	maskapai.append("CITILINK")
elif Tujuan ==  "G11" :
	tujuan.append("Jogja")
	maskapai.append("Lion Air")
	waktu.append("16.00 WIB")
	tiba.append("17.15 WIB")
	harga = 550000
elif Tujuan ==  "G12" :
	tujuan.append("Jogja")
	maskapai.append("Lion Air")
	waktu.append("16.23 WIB")
	tiba.append("17.35 WIB")
	harga = 750000
elif Tujuan ==  "S11" :
	tujuan.append("Semarang")
	maskapai.append("Lion AIr")
	harga = 450000
	waktu.append("17.00 WIB")
	tiba.append("17.45 WIB")
elif Tujuan ==  "S12" :
	tujuan.append("Semarang")
	harga = 550000
	waktu.append("18.00 WIB")
	tiba.append("18.55 WIB")
	maskapai.append("Batik Air")
elif Tujuan ==  "P11" :
	tujuan.append("Jayapura")
	harga = 1950000
	maskapai.append("Air Asia")
	waktu.append("16.00 WIB")
	tiba.append("19.25 WIB")
elif Tujuan ==  "R11" :
	tujuan.append("Singapore")
	harga = 1450000
	waktu.append("16.00 WIB")
	tiba.append("19.55 WIB")
	maskapai.append("Garuda Indonesia")
elif Tujuan ==  "M11" :
	tujuan.append("Maluku")
	harga = 1000000
	waktu.append("18.00 WIB")
	tiba.append("19.55 WIB")
	maskapai.append("CITILINK")
elif Tujuan ==  "L11" :
	tujuan.append("Lombok")
	maskapai.append("Lion Air")
	waktu.append("19.00 WIB")
	tiba.append("20.15 WIB")
	harga = 850000
elif Tujuan ==  "D11" :
	tujuan.append("Dubai")
	maskapai.append("Garuda Indonesia")
	waktu.append("19.10 WIB")
	tiba.append("06.15 WIB")
	harga = 15550000
elif Tujuan ==  "T11" :
	tujuan.append("Tokyo")
	harga = 10000000
	maskapai.append("Qatar Air")
	waktu.append("21.00 WIB")
	tiba.append("07.15 WIB")
elif Tujuan ==  "SS1" :
	tujuan.append("SEOUL")
	harga = 20000000
	waktu.append("22.00 WIB")
	tiba.append("08.15 WIB")
	maskapai.append("SEOUL Air")
elif Tujuan ==  "SY1" :
	tujuan.append("SYDNEY")
	harga = 4000000
	maskapai.append("Air Asia")
	waktu.append("16.00 WIB")
	tiba.append("23.15 WIB")
elif Tujuan ==  "KK1" :
	tujuan.append("MEKKAH")
	harga = 17000000
	maskapai.append("Garuda Indonesia")
	waktu.append("06.00 WIB")
	tiba.append("20.15 WIB")
elif Tujuan ==  "NW1" :
	tujuan.append("NEW YORK")
	maskapai.append("USA Air")
	waktu.append("07.00 WIB")
	tiba.append("23.15")
	harga = 30000000
else : 
	tujuan.append("Kode Salah / Tidak tersedia dalam jadwal penerbangan kami")

#Perhitungan harga tiket berdasarkan jumlah beli dan pajak pembelian tiap tiket
jumlah = int(input("Jumlah Tiket yang dibeli : "))
Total = int(jumlah*harga)
pajak = int(0.05*Total)
Bayar = Total+pajak


# Detail Pemesanan Tiket
print("-----------------------------------------------------------------------------------")
print("|     DETAIL PEMESANAN TIKET PESAWAT ONLINE JUANDA INTERNATIONAL AIRPORT          |")
print("-----------------------------------------------------------------------------------")
print("|   Nomor Kependudukan Penumpang  :", NIK)                               
print("|   Nama Penumpang                :", Nama)
print("|   Alamat Penumpang              :", Alamat)
print("|   Nomor Handphone               :", HP)
print("|   Kode Pemesanan  yang di pilih :", Tujuan)
print("|   Jam Keberangkatan pesawat     :", waktu)
print("|   Jam tiba pesawat              :", tiba)
print("|   Tujuan Penumpang              :", tujuan)
print("|   Jumlah Pemesanan Tiket        :", jumlah)
print("------------------------------------------------------------------------------------")
print("|                            DETAIL PEMBAYARAN                                     |")
print("------------------------------------------------------------------------------------")
print("|   Harga Tiket : Rp.",harga)
print("|   PPN 5%:", pajak)
print("------------------------------------------------------------------------------------")
print("|           Pembayaran Tiket Pesawat Juanda International Airport                  |")
print("------------------------------------------------------------------------------------")
print("|   Jumlah yang harus dibayarkan: Rp.", Bayar)
Pembayaran = int(input("Masukkan Pembayaran Anda: Rp."))
Kembalian_pembayaran = Pembayaran-Bayar
print("|   Uang Kembalian : Rp.", Kembalian_pembayaran)
print("------------------------------------------------------------------------------------")


print("-----------------------------------------------------------------------------------------")
print("-   Terima Kasih Pemesanan Tiket anda telah Berhasil diproses                           -")
print("-   Pastikan Anda Datang tepat waktu sesuai jadwal yang dipilih                         -")
print("-   Enjoy  Your Flight and Stay Safe                                                    -")
print("-   Hormat Kami, JUANDA INTERNATIONAL AIRPORT SURABAYA                                  -")
print("-   Alamat, Jl. Ir. H. Juanda, Betro, Kec. Sedati, Kabupaten Sidoarjo, Jawa Timur 61253 -")
print("-----------------------------------------------------------------------------------------")
