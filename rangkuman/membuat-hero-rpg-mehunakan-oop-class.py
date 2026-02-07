import time
#belajar memahami class dan membuat class sederhana, mengikuti konsep game RPG.
#ini class untuk hero
class Hero:
    #ini atribut hero
    def __init__(self, nama, darah=0, kerusakan=0):
        self.exsp = 0
        self.nama = nama
        self.darah = darah
        self.mana = 100
        self.kerusakan = 50 + kerusakan
        self.level = 1
        self.mana_regen1 = self.mana
        self.darah_regen = self.darah
        
    #ini method untuk hero meyerang monster
    def serangan(self, monster):
        if self.kerusakan > 0:
            print(f"{self.nama} meyerang {monster.nama}!")
            monster.terima_serangan_hero(self, self.kerusakan)
        else:
           print(f"{self.nama} tidak meyerang {monster.nama}")
           monster.terima_serangan_hero(self, self.kerusakan)
    #ternyata untuk memanggil fungsi di class lain wajib cantumkan nama argumen dan pake DOT (.) kasih nama atribut class yang mau kita berkomunikasi!. haha walaupun ini konyol, tapi! saya sangat senang bisa memahami nya:)
    
    #ini method skill hero
    def skil_hero(self, monster):
         kerusakan_skill = 150
         level_hero = 1
         if self.level > level_hero:
             kerusakan_skill += int(self.kerusakan * (50/100))
             level_hero += 1
         if self.mana > 30:
             print(f"{self.nama} mengunakan jurus api!")
             self.mana -= 30
             monster.terima_serangan_hero(self, kerusakan_skill)
         else:
             print ("mana kamu habis!")    
         
    #ini method untuk mana Hero
    def mana_regen(self):
        if self.mana < self.mana_regen1:
            self.mana += int (self.kerusakan * (5/100))
            #saya mau pake while seperti method hp Regen, tapi dilihat dari hasil nya saya lihat gak jadi. hahahah
            print("mana Regen aktif")
             
    #ini method menerima serangan dari monster 
    def terima_seragan_monster(self, kerusakan):
        darah = self.darah
        self.darah -= kerusakan
        if self.darah <= 0:
            print(f"{self.nama} menerima hit {kerusakan}, {self.nama} mati!")
        elif self.darah < darah:
            print(f"{self.nama} menerima hit {kerusakan} sisa darah {self.darah}")
        else:
            print("kamu tidak menyerang") 
            
    #ini method untuk hp Regen hero
    def hp_regen_hero(self):
        if self.darah < self.darah_regen:
            self.darah += int (self.darah * (2/100))
            #saya pake while dan time.sleep membuat Regen itu seperti di game, saya membayangkan dimana ketika Hero diam darah nya nambah seperti itu lah yang saya pikirkan. tapi sayang sekali ketikan kode di exskusi nunggu while di dalam fungsi ini selesai dulu baru while utama jalan . 
            #hahaha ternyata tidak bisa dalam 1 waktu 2 while jalan, konyol sekali. Mukin hal begituan ada di while khusus di engine game, malah saya praktekkan di while biasa. sungguh konyol.
            #jadi ya saya ganti aja ke if biasa, Regen nya aktif jika kode nya di eksekusi aja.
            print("hp Regen aktif")
                       
        
    #ini method untuk naik level Hero
    def naik_level(self, monster):
        exsp = 100
        if monster.darah <= 0:
            self.exsp += int(monster.darah_utuh * (20/100))
        if self.exsp >= exsp:
                self.level += 1
                self.darah += int(self.exsp * (40/100))
                self.mana += int(self.exsp * (20/100))
                self.kerusakan += int(self.exsp * (10/100))
                print(f"selamat kamu naik level {self.level}")
                #untuk mereset exsp ke 0
                self.exsp -= exsp
                #ini menambah kapasitas exsp
                exsp += 100    
        
    #ini method menampilkan info Hero
    def info_hero(self):
        print(f"level: {self.level}")
        print(f"exsp: {self.exsp}")
        print(f"nama : {self.nama}")
        print(f"darah: {self.darah}")
        print(f"mana : {self.mana}")
        print(f"kerusakan: {self.kerusakan}")
    
    #ini method untuk bolean Hero
    def hidup(self):
        return self.darah > 0    
        
#ini class untuk monster       
class Monster:
    #ini atribut untuk monster
    def __init__(self, nama, darah=0, kerusakan=0):
        self.nama = nama
        self.darah = darah
        self.darah_utuh = self.darah
        self.kerusakan_monster = 20 + kerusakan
    
    #ini method menerima serangan dari hero
    def terima_serangan_hero(self, hero, terima_kerusakan):
        self.darah -= terima_kerusakan
        if self.darah <= 0:
            print(f"{self.nama} menerima hit {terima_kerusakan}, {self.nama} mati!")
        elif self.darah < self.darah_utuh:
            print(f"{self.nama} menerima hit {terima_kerusakan} sisa darah {self.darah}")
            print(f"{self.nama} menyerang {hero.nama}!")
            hero.terima_seragan_monster(self.kerusakan_monster)
        else:
            print(f"{self.nama} Zzzzz")    
        
        #return self.darah < self.darah_monster #ini akan melempar nilai True
        
    #ini method menampilkan info monster   
    def info_monster(self):
        print(f"nama: {self.nama}")
        print(f"darah: {self.darah}")
        print(f"kerusakan: {self.kerusakan_monster}")
    
    #ini method untuk bolean monster
    def hidup(self):
        return self.darah > 0

#ini fungsi untuk battle loop
def pertarungan(pelayer, musuh):
    ronde = 1
    while ronde > 0:
        print(f"ronde:{ronde}")
        print(f"nama:{pelayer.nama} {" "*2} vs {" "*2} nama:{musuh.nama}")
        print(f"darah:{pelayer.darah}{" "*15}darah:{musuh.darah}")
        print(f"mana:{pelayer.mana}")
        input_user = input("(1)Seragan dasar (2)mengunakan skill: ")
        
        if input_user == "1":
            pelayer.serangan(musuh)
            ronde += 1
        elif input_user == "2":
            pelayer.skil_hero(musuh)
            ronde += 1
        else:
            print("mohon input yang benar")
                    
        if not musuh.hidup():
            pelayer.naik_level(musuh)
            return "kamu menang!"
        elif not pelayer.hidup():
            return "kamu kalah!"

hero = Hero(nama="alucard", darah=200, kerusakan=150)
goblin1 = Monster("minion", darah=400, kerusakan=10)
goblin2 = Monster("minion", darah=400, kerusakan=10)
bos = Monster("bos lord", darah=600, kerusakan=30)


 #ini loping sederhana, untuk Tess logic class
while 0 > 0:
   
    print("")
    print("kamu masuk di goa...")
    time.sleep(0.5)
    print("kamu berada di persimpangan")
    hero.hp_regen_hero()
    hero.mana_regen()
    hero.info_hero()
    user = input("ketik (1)lurus (2)kanan (3)kiri (4)Exsit: ")
    
    if user == "1":
        print(" kamu jalan lurus.... ")
        time.sleep(0.5)
        if goblin1.darah <= 0:
            print(f" maaf {goblin1.nama} sudah tidak ada!")
            continue
        print(f"kamu ketemu monster {goblin1.nama} dan kamu bertarung!")
        print ("menyiapkan pertarungan....")
        time.sleep(1)
        arena = pertarungan(hero, goblin1)
        print(arena)
        
    elif user == "2":
        print(" kamu jalan kanan.... ")
        time.sleep(0.5)
        if goblin2.darah <= 0:
            print(f" maaf {goblin2.nama} sudah tidak ada!")
            continue
        print(f"kamu ketemu monster {goblin2.nama} dan kamu bertarung!")
        print ("menyiapkan pertarungan....")
        time.sleep(1)
        arena = pertarungan(hero, goblin2)
        print(arena)
    
    elif user == "3":
        print(" kamu jalan kiri.... ")
        time.sleep(1)
        if bos.darah <= 0:
            print(f" maaf {bos.nama} sudah tidak ada!")
            continue
        print(f"kamu ketemu monster {bos.nama} dan kamu bertarung!")
        print ("menyiapkan pertarungan....")
        time.sleep(1)
        arena = pertarungan(hero, bos)
        print(arena)
        
    elif user == "4":
         print("yakin mau keluar dari game?")
         user = input("(ya/no)?: ").lower()
         if user == "ya":
             print("kamu keluar dari game")
             break
      
    else:
        print("mohon input yang benar")
    
    if not hero.hidup():
        print("game over")
        break
    elif not bos.hidup():
        print("selamat kamu berhasil menamatkan game ini!")
        break
               
#print(hero1.__dict__)
#print(goblin.__dict__)
#print(goblin.hidup())
#print(hero1.hidup())            
            
#pelajaran yang saya dapatkan disini
#1 jika class 1 ingin berkomunikasi dengan class 2 harus melalui argumen method
#2 jika kita  ingin 2 class saling interaksi dan kita ingin memanipulasi nila yang ada class wajib pake method yang ada di argumen.
#contoh: nama Argumen di method kasih DOT dan nama atribut yang ada di class yang mau kita komunikasi.
# saya masih harus bersabar dan terus bertanya dan belajar