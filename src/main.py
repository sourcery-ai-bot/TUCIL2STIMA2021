from Graf import *
from FungsiLain2 import *

# INISIALISASI
graf = Graf()
nomorSmt = 0

# ALGORITMA UTAMA

# menerima input file txt yang sudah sesuai dan mengisi graf berdasarkan file yang diberikan. 
# file txt diletakkan di folder "test".
graf.IsiGrafDariFile(open("../test/"+str(input("Masukkan nama file (ex: dummy.txt): ")),'r'));

# looping sampai semua matakuliah diselesaikan atau sudah terambil 8 semester.
while graf.simpul2 != [] and nomorSmt < 8: 
    nomorSmt += 1

    # looping setiap simpul, nama simpul yang tidak memiliki sisi masuk dimasukkan ke listMatkulSemIni.
    listMatkulSemIni = graf.listNamaSimpulDerajatMasukNol()
    
    # hapus semua simpul mata kuliah yang sudah diambil semester ini.
    graf.HapusSemuaSimpul(listMatkulSemIni)

    # print matkul yang dapat diambil semester ini.
    printMatkulSmtIni(nomorSmt, listMatkulSemIni)
