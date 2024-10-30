class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
#membuat class persegi panjang
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    #menghitung keliling persegi panjang

    def luas(self):
        return self.panjang * self.lebar
    #menghitung luas persegi panjang

    def __str__(self):
        return f"Persegi panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"
    #membuat _str_

def main():
    try:   
        panjang = int(input("Masukkan panjang persegi panjang (cm): "))
        lebar = int(input("Masukkan lebar persegi panjang (cm): "))

        if panjang <= 0 or lebar <= 0:
            print("Nilai panjang dan lebar harus lebih dari 0")
        else:
            persegi_panjang = PersegiPanjang(panjang, lebar)
            print(persegi_panjang)  
            print("Keliling:", persegi_panjang.keliling(), "cm")  
            print("Luas:", persegi_panjang.luas(), "cm²")
    except ValueError:
        print("Input harus berupa angka yang valid.")          

if __name__ == "__main__":
    main()
    #membuat konstruktornya