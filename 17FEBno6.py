class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def info(self):
        print(f'nama : {self.nama}')
        print(f'umur : {self.umur} tahun')
        
def main():    
    nama = input('masukkan nama : ')        
    umur = int(input('masukkan umur : '))

    orang = Manusia(nama, umur)
    orang.info()
    
if __name__ == "__main__":
    main()
