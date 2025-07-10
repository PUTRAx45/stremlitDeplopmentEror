#Definiskan kelas
class mobile:
    #konstruktur untuk inisialisai objek
    def_init_(self merk,model,tahun):
        self.merk = mrk
        self.model=model
        self.tahun=tahun
    #metode untuk menampilkan informasi mobil
        def info(self):
            return f"{self.merk}{self.model}({self.tahun})"
        #metode untuk menyalakan mesin mobil
        def nyalakan_mesin(self):
            return f"mesin {self.merk}{self.model}menyala!"
        #metode untuk mematikan mesin mobil
        def matikan_mesin(self):
            return f"Mesin{self.merk}{self.model}mati."
        #Buat objek dari kelas mobil
        mobil1 = mobil ("toyota","accord",2021)
        mobil2 = mobil("honda","fuso",2017)
        #panggil metode info untuk melihat informasi mobil
        print(mobil1.info())
        print(mobil2.info())
        #panggil metode nyalaan_mesin dan Matikan_mesin
        print(mobil1.nyalakan_mesin())
        print(mobil2.matikan_mesin())
        
