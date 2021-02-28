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