# Import library  yang akan digunakan
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# Inisialisasi fungsi 
def cetak(a):
    if (a+1)%2==0:
       print(a+1, "Genap - ID proses", getpid())
    else:
       print(a+1, "Ganjil - ID proses", getpid())
    sleep(1)

# Buat inputan untuk melakukan perulangan
batas=int(input("Masukkan batas perulangan: "))

# Sekuensial
sekuensial_awal = time()
print("Sekuensial")
for a in range(batas):
    cetak(a)
sekuensial_akhir = time()

# Multiprocessing dengan Kelas Process
process_awal = time()
print("multiprocessing.Process")
for a in range(batas):
    p=Process(target=cetak, args=(a, ))
    p.start()
    p.join()
process_akhir = time()

# Multiprocessing dengan Kelas Pool
pool_awal = time()
pool = Pool()
print("multiprocessing.Pool")
pool.map(cetak, range(0,batas))
pool.close()
pool_akhir = time()

# Membandingkan waktu eksekusi
print("Waktu eksekusi sekuensial : ", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process : ", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool : ", pool_akhir - pool_awal, "detik")
