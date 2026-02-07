#saya pengen minum kopi, pas sekali saya melihat ada kopi di meja 2 SASET.
#gimana cara saya implementasikan ke komputer supaya dia paham instruksi dari saya? oke saya akan coba!


import time
kopi = 1
dapur = False
api = False

print("kamu berada di ruang tamu memegang 1 kopi saset!")
saya = input (f"kemana kamu akan pergi? (dapur/kamar/keluar?): ").lower()
if saya == "dapur":
    print(f"kamu sekarang berada di dapur membawa {kopi} kopi saset!")
    dapur = True
elif saya == "kamar":
    print(f"sekarang kamu berada di kamar tidur membawa {kopi} kopi saset!")
else:
    print("kamu keluar dari rumah")
if dapur:
   print("kamu melihat ternyata di dapur tidak ada air panas!")
   saya2 = input("ambil air dingin dan panaskan (ya/no)?: ").lower()
   
   if saya2 == "ya":
       print("kamu mengambil air dingin...")
       time.sleep(2)
       print("kamu menuangkan air dingin ke tempat pemanas...!")
       time.sleep(1)
       api = True
       
   else:
       print("tidak jadi karena tidak ada air")

if api:
    print("apakah kamu ingin menyalakan api?")
    api_input = input("(ya/no): ").lower()
    
    if api_input == "ya":
        for i in range(kopi):
            print("kamu menyalakan api...")
            time.sleep(0.5)
            print("air sendang di masak...")
            time.sleep(5)
            print ("air sudah masak!")
        
        saya3 = input("apakah kamu ingin menyeduh air ke kopi nya? (ya/no): ").lower()
        
        if saya3 == "ya":
            print("kamu menyeduhkan air panas ke kopi!...")
            time.sleep(2.5)
            print("kopi kamu udah jadi, selamat menikmati:) ")
        else:
            print("nanti aja")
    else:
        print("kompor nya gak mau idup!")       