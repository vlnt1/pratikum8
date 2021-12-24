x={}
print("================================================================================")
print("|\t\t\tProgram Input Nilai Mahasiswa\t\t\t\t|")
print("================================================================================")
class mahasiswa():
    def tambah():
        print("Tambah Data")
        nama = input("Masukkan Nama Mahasiswa   : ")
        nim = input("Masukkan NIM              : ")
        tugas = int(input("Masukkan Nilai Tugas      : "))
        uts = int(input("Masukkan Nilai UTS        : "))
        uas = int(input("Masukkan Nilai UAS        : "))
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        x[nama] = nim , tugas, uts , uas , akhir
        print("---------------------------------------------------------------------------------")
    def lihat():
        if x.items():
            print("---------------------------------------------------------------------------------")
            print("\n                               DAFTAR NILAI MAHASISWA                    ")
            print("---------------------------------------------------------------------------------")
            print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
            print("---------------------------------------------------------------------------------")
            i = 0                                                                         
            for b in x.items():                                                             
                 i += 1
                 print("| {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} | {5:7f}   |"
                    . format ( b [ 0 ][: 14 ], b [ 1 ][ 0 ], b [ 1 ][ 1 ], b [ 1 ][ 2 ], b [ 1 ][ 3 ], b [ 1 ][ 4 ] , no = i ))
            print("---------------------------------------------------------------------------------")
        else :
            print("---------------------------------------------------------------------------------")
            print("\n                               DAFTAR NILAI MAHASISWA                    ")
            print("---------------------------------------------------------------------------------")
            print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
            print("---------------------------------------------------------------------------------")
            print("|                                TIDAK ADA DATA                                 |")
            print("---------------------------------------------------------------------------------")
    def hapus():
        print ( "Hapus Data" )
        nama = input("Masukkan Nama Mahasiswa   : ")
        if  nama in  x . keys ():
            del  x [ nama ]
            print("---------------------------------------------------------------------------------")
            print("\t\t\t\tDATA {} TELAH DIHAPUS!" .format(nama))
            print("---------------------------------------------------------------------------------")
        else :
            print ( "Nama {0} Tidak Ditemukan" . format ( nama ))
    def ubah():
        print ( "Ubah Data" )
        nama = input("Masukkan Nama Mahasiswa   : ")
        if nama in  x . keys ():
            nim = input("Masukkan NIM              : ")
            tugas = int(input("Masukkan Nilai Tugas      : "))
            uts = int(input("Masukkan Nilai UTS        : "))
            uas = int(input("Masukkan Nilai UAS        : "))
            akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
            x[nama] = nim , tugas, uts , uas , akhir
        else :
            print ( "Nama{0} Tidak Ditemukan" . format(nama ))
while True:
    c = input("L)ihat, T)ambah, U)bah, H)apus, K)eluar : ")
    if c.lower() == "l":
        mahasiswa.lihat()
    elif c.lower() == "t":
        mahasiswa.tambah()
    elif c.lower() == "u":
        mahasiswa.ubah()
    elif c.lower() == "h":
        mahasiswa.hapus()
    elif c.lower() == "k":
        print()
        print("---------------------------------------------------------------------------------")
        print("                                 PROGRAM TELAH SELESAI                    ")
        print("---------------------------------------------------------------------------------")
    else:
        CRED = '\033[91m'
        CEND = '\033[0m'
        print(CRED + "KODE YANG ANDA MASUKKAN SALAH!\nSILAHKAN INPUT ULANG KODE YANG BENAR." + CEND)