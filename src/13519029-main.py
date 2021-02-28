import importlib  
GRAF = importlib.import_module("13519029-Graf")
FUNGSILAIN2 = importlib.import_module("13519029-FungsiLain2")

# INISIALISASI
graf = GRAF.Graf()
nomorSmt = 0
exit = False
# ALGORITMA UTAMA

# menerima input file txt yang sudah sesuai dan mengisi graf berdasarkan file yang diberikan. 
# file txt diletakkan di folder "test".
graf.IsiGrafDariFile(open("../test/"+str(input("Masukkan nama file (ex: dummy.txt): ")),'r'));

# looping sampai semua matakuliah diselesaikan atau sudah terambil 8 semester.
while not exit:
    FUNGSILAIN2.printMenu()
    print("")
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan==1:
        # Menampilkan simpul dan sisi graf
        print("")
        graf.PrintGraf()
    elif pilihan==2:
        # Menampilkan hasil rencana kuliah
        print("")
        while graf.simpul2 != [] and nomorSmt < 8: 
            nomorSmt += 1

            # looping setiap simpul, nama simpul yang tidak memiliki sisi masuk dimasukkan ke listMatkulSemIni.
            listMatkulSemIni = graf.listNamaSimpulDerajatMasukNol()
            
            # hapus semua simpul mata kuliah yang sudah diambil semester ini.
            graf.HapusSemuaSimpul(listMatkulSemIni)

            # print matkul yang dapat diambil semester ini.
            FUNGSILAIN2.printMatkulSmtIni(nomorSmt, listMatkulSemIni)
    elif pilihan==3:
        # Menampilkan Readme
        print("")
        print("""Program ini mensorting kumpulan mata kuliah yang dapat diambil untuk setiap semesternya menggunakan Algoritma Topological Sort.
Pendekatan yang digunakan adalah memasukkan semua mata kuliah sebagai simpul dalam graf dan sisinya sebagai relasi prerequisitenya.""")
    elif pilihan==4:
        # Exit
        exit = True
        print("")
        print("Selamat tinggal!")
    else:
        # Menampilkan pesan Error
        print("")
        print("Input tidak valid, silakan masukkan pilihan ulang!")
