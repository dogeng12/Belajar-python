data_base = {}
flag = False

#membuat sistem daftar
def sistem_daftar():
    nama_user = input("masukan nama: ").lower()
    password_user = input("masukan password: ").lower()
    #cek apakah user pernah daftar
    if nama_user in data_base:
        print("maaf kamu sudah terdaftar")
    else:
        data_base[nama_user] = password_user
        print(f"pendaftaran berhasil")

#membuat sistem login
def sistem_login():
    nama_user = input("masukan nama: ").lower()
    password_user = input("masukan password: ").lower()
    #megambil key di database
    key = data_base.get(nama_user)
    
    if password_user == key:
        print("login berhasil")
        return True
    else:
        print("login gagal")
        return False
#sistem_login()

#membuat sistem keamana
def sistem_keamanan():
    nomor = 0
    #loping keamanan
    while nomor < 5:
            nomor += 1
            user = sistem_login()
            
            if user == True:
                print("akses di terima")
                return True
            if nomor > 3:
                print("ada akses yang mencurigakan")
                return False

print("ketik (mulai) untuk menjalakan")
mulai = input(" "*10).lower()

if mulai == "mulai":
    flag = True
    print("="*20,"selamat datang!","="*20)
    print("="*10,"ketik (1) daftar (2) login (3) exsit","="*10)
else:
    print("ketik yang benar")

#logika Utama
login = False
while flag:
    input_user = input().lower()
    
    
    if input_user == "1":
        print("selama datang di pendaftaran")
        daftar = sistem_daftar()
        
    elif input_user == "2":
        print("login akun kamu untuk masuk")
        login = sistem_keamanan()
        
        if login == True:
            print("menu")
            print(login)
        elif login == False:
            flag = False
            print(login)
        else:
            print("gagal masuk")
            
    elif input_user == "3":
        break
    else:
        print("ada yang salah")
