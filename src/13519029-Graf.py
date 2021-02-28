import importlib
SIMPUL = importlib.import_module("13519029-Simpul")
SISI = importlib.import_module("13519029-Sisi")

class Graf:
    # Atribut
    # simpul2 : array of simpul
    # sisi2 : array of sisi
    # jmlsimpul, jmlsisi : integer
    def __init__(self):
        # Constructor
        self.simpul2 = []
        self.jmlSimpul = 0
        self.sisi2 = []
        self.jmlSisi = 0
    def InputSimpul(self, namaSimpul):
        # Prosedur yang menambahkan simpul ke graf jika simpul belum ada di graf.
        if self.CariSimpulDgnNama(namaSimpul) == None:
            simpul = SIMPUL.Simpul(namaSimpul)
            self.simpul2.append(simpul)
            self.jmlSimpul += 1
    def InputSisi(self, namaSimpulAwal, namaSimpulAkhir):
        # Prosedur yang menambahkan sisi ke graf jika sisi belum ada di graf. 
        # Jika simpul pada sisi belum ada sebelumnya, akan diberi pesan error.
        simpulAwal = self.CariSimpulDgnNama(namaSimpulAwal)
        simpulAkhir = self.CariSimpulDgnNama(namaSimpulAkhir)
        if (simpulAwal != None and simpulAkhir != None):
            sisi = SISI.Sisi(simpulAwal,simpulAkhir)
            self.sisi2.append(sisi)
            self.jmlSisi += 1
        else:
            print("Simpul pada sisi belum dibuat!")
    def CariSimpulDgnNama(self, namasimpul):
        # Fungsi yang mencari simpul bernama "namasimpul" pada listSimpul, mengembalikan None jika tidak ada.
        for i in self.simpul2:
            if i.nama == namasimpul:
                return i
        return None
    def DerajatMasuk(self, namaSimpul):
        # Fungsi yang menghitung derajat masuk pada sebuah simpul.
        banyak = 0
        for i in self.sisi2:
            if i.simpulAkhir.nama == namaSimpul:
                banyak += 1
        return banyak
    def listNamaSimpulDerajatMasukNol(self):
        # Fungsi yang mengembalikan sebuah list berisi semua nama simpul yang berderajat masuk nol.
        listNamaSimpul = []
        for simpul in self.simpul2:
            if self.DerajatMasuk(simpul.nama) == 0:
                listNamaSimpul.append(simpul.nama)
        return listNamaSimpul
    def HapusSimpul(self, namaSimpul):
        # Prosedur yang menghapus simpul bernama "namaSimpul" pada graf beserta sisi2nya jika ada.
        ketemu = False
        for i in range(0,self.jmlSimpul):
            if self.simpul2[i].nama == namaSimpul or ketemu:
                ketemu = True
                if i == self.jmlSimpul-1:
                    self.simpul2.pop(i)
                else:
                    self.simpul2[i] = self.simpul2[i+1]
        if ketemu:
            i = 0
            while i < self.jmlSisi:
                if self.sisi2[i].simpulAwal.nama == namaSimpul or self.sisi2[i].simpulAkhir.nama == namaSimpul:
                    self.HapusSisi(self.sisi2[i].simpulAwal.nama,self.sisi2[i].simpulAkhir.nama)
                else:
                    i += 1
            self.jmlSimpul -= 1
    def HapusSemuaSimpul(self, listNamaSimpul):
        # Prosedur yang menghapus semua simpul yang namanya tertera pada listNamaSimpul.
        for namaSimpul in listNamaSimpul:
            self.HapusSimpul(namaSimpul)
    def HapusSisi(self, namaSimpulAwal, namaSimpulAkhir):
        # Prosedur yang menghapus sisi yang diinput pada graf jika ada.
        ketemu = False
        for i in range(0,self.jmlSisi):
            if (self.sisi2[i].simpulAwal.nama == namaSimpulAwal and self.sisi2[i].simpulAkhir.nama == namaSimpulAkhir) or ketemu:
                ketemu = True
                if i == self.jmlSisi-1:
                    self.sisi2.pop(i)
                else:
                    self.sisi2[i] = self.sisi2[i+1]
        if ketemu:
            self.jmlSisi -= 1      
    def PrintGraf(self):
        # Prosedur yang mencetak isi graf ke layar.
        print(f"Banyak simpul : {self.jmlSimpul}")
        for i in self.simpul2:
            print(i.nama)
        print(f"Sisi : {self.jmlSisi}")
        for i in self.sisi2:
            print(i.simpulAwal.nama + "-" + i.simpulAkhir.nama)
    def IsiGrafDariFile(self, file):
        # Prosedur yang mengisi graf dengan data mata kuliah dari file.
        namaMatkul = ""
        fileperbaris = file.readlines()
        for baris in fileperbaris:
            namaSimpulPertama = ""
            for huruf in baris:
                if namaSimpulPertama == "": 
                    if huruf != ',' and huruf != '.' and huruf != ' ' and huruf != '\n':
                        namaMatkul += huruf
                    elif huruf == ',' or huruf == '.':
                        namaSimpulPertama = namaMatkul
                        self.InputSimpul(namaMatkul)
                        namaMatkul = ""
                else:
                    if huruf != ',' and huruf != '.' and huruf != ' ' and huruf != '\n':
                        namaMatkul += huruf
                    elif huruf == ',' or huruf == '.':
                        self.InputSimpul(namaMatkul)
                        self.InputSisi(namaMatkul,namaSimpulPertama)
                        namaMatkul = ""
