import json
import os 

#membuat sistem data base
data_base = "data_base.json"

#fungsi cek data di file
def ambil_data():
    if not os.path.exists(data_base):
        return {}
    try:
        with open(data_base, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("data belom ada di file")
        return {}

#fungsi simpan data di file
def simpan_data(simpan):
    with open(data_base, "w") as file:
        json.dump(simpan, file, indent=4)

#menambah data awal di file ke variabel
data_awal = ambil_data()

#cek apakah data sudah ada di file
if not data_awal:
    data_awal = {"id_user": {"profil": {"username": "admin", "password": "123","menu_makanan": ["ayam goreng", "nasi goreng", "es teh"]}}}
    simpan_data(data_awal) #data disimpan

#membuat sistem daftar dan login

#membuat sistem daftar
def sistem_daftar():
    
    data_daftar = ambil_data()
    
    nama_user = input("masukan nama: ").lower()
    password_user = input("masukan password: ").lower()
    
    #cek apakah user pernah daftar
    user_udah_ada = False
    for id_user, ambil_username in data_daftar.items():
        if ambil_username["profil"]["username"] == nama_user:
            user_udah_ada = True
            break
    if user_udah_ada:
        print("nama kamu sudah ada")
        return False
    else:
        #menambah key baru di data base
        add_id = f"id_user{len(data_daftar) + 1}"
        data_daftar[add_id] = {"profil": {"username": nama_user, "password": password_user,"menu_makanan": ["ayam goreng", "nasi goreng", "es teh"]
}}
        simpan_data(data_daftar)
        print("kamu sudah terdaftar")
        return True
         #fungsi ini berakhir disini!

#membuat sistem login
def sistem_login():
    data_login = ambil_data()
    
    nama_user = input("masukan nama: ").lower()
    password_user = input("masukan password: ").lower()
    #megambil key di database
    for id_user, ambil_id_user in data_login.items():
        #ambil nilai password
        if ambil_id_user["profil"]["username"] == nama_user:
            #memasuki nilai password ke varibel
            ambil_nilai_sandi = ambil_id_user["profil"]["password"]
            
            #mebandikan nilai sandi di database dengan input sandi user
            if ambil_nilai_sandi == password_user:
                print("login berhasil")
                return True
            else:
                print("password salah!")
                return False
                
    print("username dan password tidak ada")
    return False
    #fungsi ini berakhir disini

#membuat sistem keamana
def sistem_keamanan():
    nomor = 3
    #loping keamnan
    while nomor > 0:
            nomor -= 1
            user = sistem_login()
            
            if user == True:
                print("akses di terima")
                return True
            else:
                print(f"kesempata login kamu cuma (3) sisa {nomor}")
                
   #kasih nilai False jika user salah input 3 x             
    print("ada akses yang mencurigakan")
    return False
 
    
#membuat sistem loping sederha untuk megetes logic fungsi apakah berjalan dengan baik.   
daftar = sistem_daftar()
number = 5
while number > 0:
    if daftar:
        login = sistem_keamanan()
        print(login)
        number -= 1
        if login == False:
            break