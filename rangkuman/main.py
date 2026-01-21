import keamanan as aman
flag = False

while 0 < 1:
    print("ketik (mulai) untuk menjalakan")
    mulai = input(" "*10).lower()
    if mulai == "mulai":
        flag = True
        print("="*20,"selamat datang!","="*20)
        print("="*10,"ketik (1) daftar (2) login (3) exsit","="*10)
        break
    else:
        print("ketik yang benar")
    
menu = ["daftar akun", "login akun"]
#logika Utama
login = False
while flag:
    input_user = input().lower()
    
    
    if input_user == "1":
        print("selama datang di pendaftaran")
        daftar = aman.sistem_daftar()
        
    elif input_user == "2":
        print("login akun kamu untuk masuk")
        login = aman.sistem_keamanan()
        
        if login == True:
            print("menu")
            print(login)
        elif login == False:
            flag = False
            print(login
            print("gagal masuk")
            
    elif input_user == "3":
        break
    else:
        print("ada yang salah")