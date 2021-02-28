def printMatkulSmtIni(nomorSmt, listNamaMatkul):
    # Prosedur yang mencetak nama matkul yang dapat diambil pada semester ini ke layar
    print(f"Semester {nomorSmt} :", end="")
    matkulPertama = True
    for matkul in listNamaMatkul:
        if matkulPertama:
            print(f" {matkul}", end="")
            matkulPertama = False
        else:
            print(f", {matkul}", end="")
    print(".")

def printMenu():
    # Prosedur yang mencetak menu program
    print("")
    print("Daftar Perintah:")
    print("1. Lihat simpul dan sisi dari graf")
    print("2. Lihat hasil mata kuliah")
    print("3. Lihat ReadMe")
    print("4. Exit")