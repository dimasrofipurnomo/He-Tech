import csv
import os
from tabulate import tabulate
from datetime import datetime, timedelta

def bersihkan_layar():
    os.system("cls")

def tampilkan_cover():
    art = """
                                    ██╗  ██╗███████╗              ████████╗███████╗ ██████╗██╗  ██╗    
                                    ██║  ██║██╔════╝              ╚══██╔══╝██╔════╝██╔════╝██║  ██║    
                                    ███████║█████╗      █████╗       ██║   █████╗  ██║     ███████║    
                                    ██╔══██║██╔══╝      ╚════╝       ██║   ██╔══╝  ██║     ██╔══██║    
                                    ██║  ██║███████╗                 ██║   ███████╗╚██████╗██║  ██║    
                                    ╚═╝  ╚═╝╚══════╝                 ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝                                                                                                          
    """
    print(art)

# ========================================================= REGISTRASI =========================================================
def registrasi_user():
    bersihkan_layar()
    print(''' 
                                            ==========================================
                                                            REGISTRASI USER
                                            ==========================================
          ''')

    while True:
        try:
            nama_lengkap = input("Masukkan Nama Lengkap: ")
            if not nama_lengkap:
                raise ValueError("Nama lengkap tidak boleh kosong.")
            else: 
                break
        except ValueError as error:
            print(f"Error: {error}")

    while True:
        try:
            username = input("Masukkan Username: ")
            if not username:
                raise ValueError("Username tidak boleh kosong.")
            elif len(username) < 5:
                raise ValueError("Username harus memiliki minimal 5 karakter.")
            
            try:
                with open("user/user.csv", "r", newline="") as file:
                    data_regis = csv.reader(file)
                    for registrasi_user in data_regis:
                        if registrasi_user and registrasi_user[0] == username:
                            raise ValueError("Username sudah digunakan. Masukkan username lain.")
            except FileNotFoundError:
                pass  
            break
        except ValueError as error:
            print(f"Error: {error}")

    while True:
        try:
            password = input("Masukkan Password: ")
            if not password:
                raise ValueError("Password tidak boleh kosong.")
            elif len(password) < 8:
                raise ValueError("Password harus memiliki minimal 8 karakter.")
            else:
                break
        except ValueError as error:
            print(f"Error: {error}")

    try:
        with open("admin/user.csv", "r") as file1, open("user/user.csv", "r") as file2:
            file1.read()
            file2.read()

        with open("admin/user.csv", "a", newline="") as file1, open("user/user.csv", "a", newline="") as file2:
            data_admin = csv.writer(file1)
            data_user = csv.writer(file2)

            data_admin.writerow([username, password, nama_lengkap])
            data_user.writerow([username, password, nama_lengkap])

        print(f"Selamat Registrasi User '{nama_lengkap}' Berhasil. Silakan login untuk melanjutkan")
    except Exception as error:
        print(f"Terjadi kesalahan saat menyimpan data: {error}")

# ======================================================== LOGIN USER ========================================================
def login_user():
    bersihkan_layar()
    print(''' 
                                            ==========================================
                                                            LOGIN USER
                                            ==========================================
          ''')

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if not username or not password:
        print("Username dan password tidak boleh kosong. Silakan coba lagi.")
        return

    try:
        with open("user/user.csv", "r") as file:
            data_login = csv.reader(file)
            next(data_login)  
            
            for login_user in data_login:
                if login_user[0] == username and login_user[1] == password:
                    print(f"Login berhasil. Selamat datang di Aplikasi He-Tech {username}.")
                    menu_user(username)
                    return

            print("Username atau password tidak ditemukan. Silakan coba lagi.")
    except FileNotFoundError:
        print("File user.csv tidak ditemukan. Pastikan data user tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ======================================================== LOGIN ADMIN ========================================================
def login_admin():
    bersihkan_layar()
    print(''' 
                                            ==========================================
                                                            LOGIN ADMIN
                                            ==========================================
          ''')

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if not username or not password:
        print("Username dan password tidak boleh kosong. Silakan coba lagi.")
        return

    try:
        with open("admin/admin.csv", "r") as file:
            data_admin = csv.reader(file)
            next(data_admin)  
            
            for login_admin in data_admin:
                if login_admin[0] == username and login_admin[1] == password:
                    print(f"Login berhasil. Selamat Datang Kembali {username}.")
                    menu_admin()
                    return

            print("Username atau password tidak ditemukan. Silakan coba lagi.")
    except FileNotFoundError:
        print("File admin.csv tidak ditemukan. Pastikan data admin tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ==================================================== DATA LOGIN USER =================================================
def tampilkan_login_user():
    bersihkan_layar()
    print(''' 
===========
 DATA USER
===========
    ''')
    try:
        with open("admin/user.csv", "r") as file:
            data_user = csv.reader(file)
            headers = next(data_user)  
            daftar_user = list(data_user)  

        if not daftar_user:
            print("Tidak ada data user yang tersedia.")
        else:
            print(tabulate(daftar_user, headers=headers, tablefmt='simple_grid'))

    except FileNotFoundError:
        print("File user.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ==================================================== DAFTAR HOTEL DAN KAMAR =================================================
def tampilkan_hotel():
    bersihkan_layar()
    print(''' 
========================
 DAFTAR HOTEL DAN KAMAR
========================
    ''')
    try:
        with open("admin/hotel.csv", "r") as file:
            data_hotel = csv.reader(file)
            headers = next(data_hotel)  
            daftar_hotel = list(data_hotel) 

        if not daftar_hotel:
            print("Tidak ada data hotel yang tersedia.")
        else:
            print(tabulate(daftar_hotel, headers=headers, tablefmt='simple_grid'))

    except FileNotFoundError:
        print("File hotel.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

def tampilkan_kamar():
    bersihkan_layar()
    try:
        with open("admin/kamar.csv", "r") as file:
            data_kamar = csv.reader(file)
            headers = next(data_kamar)  
            daftar_kamar = list(data_kamar) 

        if not daftar_kamar:
            print("Tidak ada data hotel yang tersedia.")
        else:
            print(tabulate(daftar_kamar, headers=headers, tablefmt='simple_grid'))

    except FileNotFoundError:
        print("File kamar.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ==================================================== KELOLA DATA HOTEL =================================================
def kelola_data_hotel():
    bersihkan_layar()
    print(''' 
===================
 KELOLA DATA HOTEL
===================
    ''')
    print ("""   
    1. TAMBAH DATA HOTEL
    2. EDIT DATA HOTEL
    3. HAPUS DATA HOTEL
    4. KEMBALI KE MENU ADMIN 
    """)
    while True :
        try :
            pilih = int(input("Pilih opsi: "))
            if pilih == 1 :
                bersihkan_layar()
                tambah_data_hotel()
            elif pilih == 2 :
                bersihkan_layar()
                edit_data_hotel()
            elif pilih == 3 :
                bersihkan_layar()
                hapus_data_hotel()
            elif pilih == 4 :
                bersihkan_layar()
                menu_admin()
            else :
                raise ValueError ("opsi yang nada pilih tidak tersedia")
        except ValueError as error:
            print(f"Terjadi kesalahan: {error}")
            continue

def tambah_data_hotel():
    bersihkan_layar()
    print(''' 
===================
 TAMBAH DATA HOTEL 
===================
    ''')
    tampilkan_hotel()
    try:
        id_hotel = int(input("Masukkan ID Hotel: "))
        nama_hotel = input("Masukkan Nama Hotel: ")
        lokasi = input("Masukkan Lokasi: ")
        kontak = input("Masukkan Kontak: ")
        deskripsi = input("Masukkan Deskripsi Hotel: ")

        with open("admin/hotel.csv", "a", newline="") as file:
            data_hotel = csv.writer(file)
            data_hotel.writerow([id_hotel, nama_hotel, lokasi, kontak, deskripsi])

        print(f"Hotel {nama_hotel} berhasil ditambahkan!")

        tambah_data_kamar(id_hotel, nama_hotel)

    except ValueError:
        print("Input tidak valid. Pastikan ID Hotel berupa angka.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

def tambah_data_kamar(id_hotel, nama_hotel):
    tampilkan_kamar()
    try:
        while True:
            print(f"Tambahkan kamar untuk Hotel {nama_hotel} (ID Hotel: {id_hotel})")
            id_kamar = int(input("Masukkan ID Kamar: "))
            tipe_kamar = input("Masukkan Tipe Kamar: ")
            harga = int(input("Masukkan Harga Kamar/Malam: "))
            fasilitas_kamar = input("Masukkan Fasilitas Kamar: ")
            jumlah_kamar = int(input("Masukkan Jumlah Kamar: "))
            kamar_tersedia = int(input("Masukkan Jumlah Kamar Tersedia: "))
            kapasitas_kamar = int(input("Masukkan Kapasitas Kamar: "))
            status = input("Masukkan Status Kamar (Tersedia/Tidak Tersedia): ")

            with open("admin/kamar.csv", "a", newline="") as file:
                data_kamar = csv.writer(file)
                data_kamar.writerow([
                    id_kamar, id_hotel, nama_hotel, tipe_kamar, harga,
                    fasilitas_kamar, jumlah_kamar, kamar_tersedia,
                    kapasitas_kamar, status
                ])
            
            print(f"Kamar {tipe_kamar} berhasil ditambahkan ke hotel {nama_hotel}!")

            lanjut = input("Tambah kamar lagi? (ya/tidak): ").lower()
            if lanjut != "ya":
                print(f"Proses penambahan kamar selesai untuk Hotel {nama_hotel}.")
                kelola_data_hotel()
                break
    except ValueError:
        print("Input tidak valid.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

def edit_data_hotel():
    bersihkan_layar()
    print(''' 
=================
 EDIT DATA HOTEL 
=================
    ''')
    tampilkan_hotel()

    try:
        id_hotel = input("Masukkan ID Hotel yang ingin diedit: ")

        with open("admin/hotel.csv", "r") as file:
            data_hotel = csv.reader(file)
            daftar_hotel = list(data_hotel)

        header_hotel = daftar_hotel[0]
        baris_hotel = daftar_hotel[1:]
        hotel_ditemukan = False

        for i, data in enumerate(baris_hotel):
            if data[0] == id_hotel:
                hotel_ditemukan = True
                print(f"Data hotel ditemukan: {data}")
                print("Masukkan data baru: (Kosongkan Jika Tidak Ingin Mengubah)")
                nama_hotel = input("Nama Hotel: ") or data[1]
                lokasi = input("Lokasi: ") or data[2]
                kontak = input("Kontak: ") or data[3]
                deskripsi = input("Deskripsi: ") or data[4]

                baris_hotel[i] = [id_hotel, nama_hotel, lokasi, kontak, deskripsi]
                with open("admin/hotel.csv", "w", newline="") as file:
                    data_hotel = csv.writer(file)
                    data_hotel.writerow(header_hotel)
                    data_hotel.writerows(baris_hotel)

                print(f"Data hotel {nama_hotel} berhasil diperbarui!")

                edit_data_kamar(id_hotel, nama_hotel)
                return

        if not hotel_ditemukan:
            print("Hotel dengan ID tersebut tidak ditemukan.")

    except FileNotFoundError:
        print("File hotel.csv tidak ditemukan.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

def edit_data_kamar(id_hotel, nama_hotel):
    tampilkan_kamar()
    print(f"Edit data kamar untuk Hotel {nama_hotel} (ID Hotel: {id_hotel})")
    
    try:
        with open("admin/kamar.csv", "r") as file:
            data_kamar = csv.reader(file)
            daftar_kamar = list(data_kamar)

        headers_kamar = daftar_kamar[0]
        baris_kamar =daftar_kamar[1:]

        id_kamar = input("Masukkan ID Kamar yang ingin diedit: ")
        kamar_teredit = False

        for j, kamar in enumerate(baris_kamar):
            if kamar[0] == id_kamar and kamar[1] == id_hotel:  
                print(f"Data kamar ditemukan: {kamar}")
                print("Masukkan data baru: (Kosongkan Jika Tidak Ingin Mengubah)")
                tipe_kamar = input("Tipe Kamar: ") or kamar[3]
                harga = input("Harga: ") or kamar[4]
                fasilitas_kamar = input("Fasilitas Kamar: ") or kamar[5]
                jumlah_kamar = input("Jumlah Kamar: ") or kamar[6]
                kamar_tersedia = input("Jumlah Kamar Tersedia: ") or kamar[7]
                kapasitas_kamar = input("Kapasitas Kamar: ") or kamar[8]
                status = input("Status: ") or kamar[9]

                baris_kamar[j] = [id_kamar, id_hotel, nama_hotel, tipe_kamar, harga, fasilitas_kamar, jumlah_kamar, kamar_tersedia, kapasitas_kamar, status]
                kamar_teredit = True
                break

        if kamar_teredit:
            with open("admin/kamar.csv", "w", newline="") as file:
                data_kamar = csv.writer(file)
                data_kamar.writerow(headers_kamar)
                data_kamar.writerows(baris_kamar)

            print(f"Kamar {id_kamar} berhasil diperbarui!")
        else:
            print(f"Kamar dengan ID {id_kamar} tidak ditemukan atau tidak terkait dengan hotel ini.")
            kelola_data_hotel()
            return

    except FileNotFoundError:
        print("File kamar.csv tidak ditemukan.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

def hapus_data_hotel():
    bersihkan_layar()
    print(''' 
==================
 HAPUS DATA HOTEL 
==================
    ''')
    tampilkan_hotel()

    try:
        id_hotel = input("Masukkan ID Hotel yang ingin dihapus: ")

        with open("admin/hotel.csv", "r") as file:
            data_hotel = csv.reader(file)
            daftar_hotel = list(data_hotel)

        headers_hotel = daftar_hotel[0]
        baris_hotel = daftar_hotel[1:]
        hotel_ditemukan = False

        baris_baru_hotel = []
        for hotel in baris_hotel:
            if hotel[0] == id_hotel:
                hotel_ditemukan = True
                print(f"Hotel ditemukan dan akan dihapus: {hotel}")
            else:
                baris_baru_hotel.append(hotel)

        if not hotel_ditemukan:
            print(f"Hotel dengan ID {id_hotel} tidak ditemukan.")
            return

        with open("admin/hotel.csv", "w", newline="") as file:
            data_hotel = csv.writer(file)
            data_hotel.writerow(headers_hotel)
            data_hotel.writerows(baris_baru_hotel)

        print(f"Data hotel dengan ID {id_hotel} berhasil dihapus!")

        tampilkan_kamar()

        with open("admin/kamar.csv", "r") as file:
            data_kamar = csv.reader(file)
            daftar_kamar = list(data_kamar)

        headers_kamar = daftar_kamar[0]
        baris_kamar = daftar_kamar[1:]

        baris_baru_kamar = [data_kamar_per_baris for data_kamar_per_baris in baris_kamar if data_kamar_per_baris[1] != id_hotel] 

        kamar_dihapus = len(baris_kamar) - len(baris_baru_kamar)
        if kamar_dihapus > 0:
            print(f"{kamar_dihapus} kamar terkait dengan ID Hotel {id_hotel} akan dihapus.")

        with open("admin/kamar.csv", "w", newline="") as file:
            data_kamar = csv.writer(file)
            data_kamar.writerow(headers_kamar)
            data_kamar.writerows(baris_baru_kamar)

        print(f"Data kamar terkait dengan ID Hotel {id_hotel} berhasil dihapus!")
        kelola_data_hotel()
        return

    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ================================================= PESAN KAMAR =================================================
def pesan_kamar(username):
    bersihkan_layar()
    print(''' 
=============
 PESAN KAMAR
=============
          ''')
    tampilkan_hotel()
    input("Tekan Enter untuk lihat daftar kamar ")
    tampilkan_kamar()
    
    try:
        id_kamar = int(input("Masukkan ID Kamar yang ingin dipesan: "))
        id_hotel = int(input("Masukkan ID Hotel yang ingin dipesan: "))
        tipe_kamar = input("Masukkan Tipe Kamar yang ingin dipesan: ").lower()  
        jumlah_kamar = int(input("Masukkan Jumlah Kamar yang ingin dipesan: "))
        jumlah_hari = int(input("Masukkan Jumlah Hari Menginap: "))  
    except ValueError:
        print("Data tidak valid!")
        return

    check_in = datetime.now()  
    check_in_str = check_in.strftime("%Y-%m-%d %H:%M:%S")

    check_out = check_in + timedelta(days=jumlah_hari)  
    check_out_str = check_out.strftime("%Y-%m-%d %H:%M:%S")

    with open("admin/kamar.csv", "r") as file:
        data_kamar = csv.reader(file)
        daftar_kamar = list(data_kamar)[1:]

    kamar_ditemukan = False
    total_pembayaran = 0
    for data_kamar in daftar_kamar:
        if int(data_kamar[0]) == id_kamar and int(data_kamar[1]) == id_hotel and data_kamar[3].lower() == tipe_kamar:
            jumlah_kamar_tersedia = int(data_kamar[7])  
            if jumlah_kamar <= jumlah_kamar_tersedia and data_kamar[9].strip().lower() == 'tersedia':
                kamar_ditemukan = True
                total_pembayaran = int(data_kamar[4]) * jumlah_kamar * jumlah_hari  

                data_kamar[7] = str(jumlah_kamar_tersedia - jumlah_kamar)

                try:
                    with open("admin/booking.csv", "a", newline="") as file1, open("user/riwayat pemesanan.csv", "a", newline="") as file2:
                        data_admin = csv.writer(file1)
                        data_user = csv.writer(file2)
                        data_admin.writerow([  
                            username, id_kamar, id_hotel, tipe_kamar, jumlah_kamar, 
                            jumlah_hari, check_in_str, check_out_str, 
                            total_pembayaran, 'Aktif'  
                        ])
                        data_user.writerow([  
                            username, id_kamar, id_hotel, tipe_kamar, jumlah_kamar, 
                            jumlah_hari, check_in_str, check_out_str, 
                            total_pembayaran, 'Aktif'  
                        ])
                except Exception as error:
                    print(f"Terjadi kesalahan saat menulis ke file booking.csv: {error}")
                    return

                try:
                    with open("admin/kamar.csv", "w", newline="") as file:
                        data_kamar = csv.writer(file)
                        data_kamar.writerow(['ID Kamar', 'ID Hotel', 'Nama Hotel', 'Tipe Kamar', 'Harga/Malam (Rp)', 'Fasilitas Kamar', 'Jumlah Kamar', 'Kamar Tersedia', 'Kapasitas Kamar', 'Status'])
                        data_kamar.writerows(daftar_kamar)
                except Exception as error:
                    print(f"Terjadi kesalahan saat menulis ke file kamar.csv: {error}")
                    return
                break

    if kamar_ditemukan:
        print(f"Pemesanan Kamar ID {id_kamar} Tipe Kamar {tipe_kamar} Jumlah Kamar {jumlah_kamar} Hotel ID {id_hotel} berhasil.")
        print(f"Durasi Menginap: {jumlah_hari} hari. Total Pembayaran: {total_pembayaran}")
        pembayaran_dan_ulasan(username, id_kamar, id_hotel, tipe_kamar, jumlah_kamar, jumlah_hari, total_pembayaran)
    else:
        print("Kamar tidak ditemukan atau sudah tidak tersedia.")

def pembayaran_dan_ulasan(username, id_kamar, id_hotel, tipe_kamar, jumlah_kamar, jumlah_hari, total_pembayaran):
    bersihkan_layar()
    print('''
============
 PEMBAYARAN
============
          ''')
    metode_pembayaran = input("Masukkan Metode Pembayaran (Cash): ")
    if metode_pembayaran.lower() != 'cash':
        print("Metode pembayaran tidak valid!")
        return

    tanggal_pembayaran = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("admin/transaksi.csv", "a", newline="") as file:
        data_transaksi = csv.writer(file)
        data_transaksi.writerow([username, id_kamar, id_hotel, tipe_kamar, jumlah_kamar, tanggal_pembayaran, total_pembayaran, 'Lunas'])

    try:
        with open("admin/booking.csv", "r") as file:
            data_booking = csv.reader(file)
            daftar_booking = list(data_booking)  

        if not daftar_booking or len(daftar_booking) == 1:  
            print("Tidak ada data pemesanan untuk diperbarui.")
            return

        headers = daftar_booking[0]  
        data = daftar_booking[1:]  

        for booking in data:
            if (booking[0] == username and 
                int(booking[1]) == id_kamar and 
                int(booking[2]) == id_hotel and
                str(booking[3]) == tipe_kamar and
                int(booking[4]) == jumlah_kamar and
                int(booking[5]) == jumlah_hari and
                float(booking[8]) == total_pembayaran):
                booking[9] = 'Selesai'

        with open("admin/booking.csv", "w", newline="") as file:
            data_booking = csv.writer(file)
            data_booking.writerow(headers)  
            data_booking.writerows(data)  

    except FileNotFoundError:
        print("File booking.csv tidak ditemukan.")
        return
    except IndexError:
        print("Data dalam file booking.csv tidak lengkap atau rusak.")
        return
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")
        return

    print(f"Pembayaran berhasil! Transaksi untuk Kamar ID {id_kamar} Tipe Kamar {tipe_kamar} Jumlah Kamar {jumlah_kamar} Jumlah Hari {jumlah_hari} Hotel ID {id_hotel} selesai.")

    print('''
================
 BERIKAN ULASAN
================
          ''')
    try:
        rating = int(input("Masukkan Rating (1-5): "))
        if rating < 1 or rating > 5:
            raise ValueError("Rating harus di antara 1 dan 5.")
    except ValueError as error:
        print(f"Kesalahan: {error}")
        return

    komentar = input("Masukkan Komentar: ")
    tanggal_ulasan = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("admin/review.csv", "a", newline="") as file:
        data_review = csv.writer(file)
        data_review.writerow([username, id_kamar, id_hotel, rating, komentar, tanggal_ulasan])

    print("Ulasan berhasil diberikan.")

# ================================================= RIWAYAT PEMESANAN ================================================
def riwayat_pemesanan():
    bersihkan_layar()
    print('''
===================
 RIWAYAT PEMESANAN 
===================
          ''')
    try:
        with open("user/riwayat pemesanan.csv", "r") as file:
            data_riwayat_transaksi = csv.reader(file)
            headers = next(data_riwayat_transaksi)
            daftar_riwayat_transaksi = list(data_riwayat_transaksi) 

        if not daftar_riwayat_transaksi:
            print("Tidak ada riwayat pemesanan yang ditemukan.")
        else:
            print(tabulate(daftar_riwayat_transaksi, headers=headers, tablefmt='grid'))

    except FileNotFoundError:
        print("File riwayat pemesanan.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ================================================= DAFTAR PEMESANAN =================================================
def lihat_pemesanan():
    bersihkan_layar()
    print('''
==================
 DAFTAR PEMESANAN 
==================
          ''')
    try:
        with open("admin/booking.csv", "r") as file:
            data_booking = csv.reader(file)
            headers = next(data_booking)
            daftar_booking = list(data_booking) 

        if not daftar_booking:
            print("Tidak ada pemesanan yang ditemukan.")
        else:
            print(tabulate(daftar_booking, headers=headers, tablefmt='grid'))

    except FileNotFoundError:
        print("File booking.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ================================================= DAFTAR ULASAN USER =================================================
def lihat_ulasan():
    bersihkan_layar()
    print('''
====================
 DAFTAR ULASAN USER 
====================
          ''')
    try:
        with open("admin/review.csv", "r") as file:
            data_review = csv.reader(file)
            headers = next(data_review)
            daftar_review = list(data_review) 

        if not daftar_review:
            print("Tidak ada ulasan yang ditemukan.")
        else:
            print(tabulate(daftar_review, headers=headers, tablefmt='grid'))

    except FileNotFoundError:
        print("File review.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ====================================================== DAFTAR TRANSAKSI ======================================================
def lihat_transaksi():
    bersihkan_layar()
    print('''
==================
 DAFTAR TRANSAKSI 
==================
          ''')
    try:
        with open("admin/transaksi.csv", "r") as file:
            data_transaksi = csv.reader(file)
            headers = next(data_transaksi)
            daftar_transaksi = list(data_transaksi) 

        if not daftar_transaksi:
            print("Tidak ada transaksi yang ditemukan.")
        else:
            print(tabulate(daftar_transaksi, headers=headers, tablefmt='grid'))

    except FileNotFoundError:
        print("File transaksi.csv tidak ditemukan. Pastikan file tersedia.")
    except Exception as error:
        print(f"Terjadi kesalahan: {error}")

# ====================================================== TAMPILAN AWAL ======================================================
def tampilan_awal():
    tampilkan_cover()

    while True:
        print(''' 
                                            ==========================================
                                                          TAMPILAN AWAL
                                            ==========================================
                                                        1. REGISTRASI
                                                        2. LOGIN SEBAGAI USER
                                                        3. LOGIN SEBAGAI ADMIN
                                                        4. LOG OUT
                                            ==========================================
              ''')
        
        pilihan = input("PILIIH UNTUK LANJUT: ")
        
        if pilihan == '1':
            registrasi_user()
        elif pilihan == '2':
            username = login_user()
            if username:
                menu_user(username)
        elif pilihan == '3':
            if login_admin():
                menu_admin()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            print("Pilihan tidak valid. Coba lagi. ")

# ===================================================== DASHBOARD ADMIN =====================================================
def menu_admin():
    while True:
        print('''
                                            ==========================================
                                                         DASHBOARD ADMIN
                                            ==========================================
                                                    1. LIHAT DATA LOGIN USER
                                                    2. LIHAT DAFTAR HOTEL
                                                    3. KELOLA DATA HOTEL
                                                    4. LIHAT DATA PEMESANAN
                                                    5. LIHAT DATA TRANSAKSI
                                                    6. LIHAT ULASAN USER
                                                    7. LOG OUT
                                            ==========================================
          ''')
        
        pilihan = input("PILIH MENU: ")
        
        if pilihan == '1':
            bersihkan_layar()
            tampilkan_login_user()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_admin()
        if pilihan == '2':
            bersihkan_layar()
            tampilkan_hotel()
            input("Tekan Enter untuk lihat daftar kamar ")
            bersihkan_layar()
            tampilkan_kamar()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_admin()
        elif pilihan == '3':
            bersihkan_layar()
            kelola_data_hotel()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_admin()
        elif pilihan == '4':
            bersihkan_layar()
            lihat_pemesanan()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_admin()
        elif pilihan == '5':
            bersihkan_layar()
            lihat_transaksi()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_admin()
        elif pilihan == '6':
            bersihkan_layar()
            lihat_ulasan()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_admin()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi ini")
            tampilan_awal()
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# ===================================================== DASHBOARD USER =====================================================
def menu_user(username):
    while True:
        print('''
                                            ==========================================
                                                        DASHBOARD USER
                                            ==========================================
                                                    1. LIHAT DAFTAR HOTEL
                                                    2. PESAN KAMAR
                                                    3. LIHAT RIWAYAT PEMESANAN
                                                    4. LIHAT ULASAN HOTEL
                                                    5. LOG OUT
                                            ==========================================
          ''')
        
        pilihan = input("PILIH MENU: ")
        
        if pilihan == '1':
            bersihkan_layar()
            tampilkan_hotel()
            input("Tekan Enter untuk lihat daftar kamar ")
            bersihkan_layar()
            tampilkan_kamar()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_user(username)
        elif pilihan == '2':
            bersihkan_layar()
            pesan_kamar(username)
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_user(username)
        elif pilihan == '3':
            bersihkan_layar()
            riwayat_pemesanan()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_user(username)
        elif pilihan == '4':
            bersihkan_layar()
            lihat_ulasan()
            input("Tekan Enter untuk kembali ke menu ")
            bersihkan_layar()
            menu_user(username)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi ini")
            tampilan_awal()
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
    
if __name__ == "__main__":
    tampilan_awal()
