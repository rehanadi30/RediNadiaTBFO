#Project The Sims Simulator
#Tugas Besar 1 TBFO

""" 
PEMBUAT:
Nama1: Rehan Adi Satrya
NIM1: 13518061
Kelas: K01

Nama2: Putri Nadia Salsabilah
NIM2: 13518094
Kelas: K01

Mata Kuliah:
Teori Bahasa Formal dan Otomata - IF2124

Definisi program:
Program adalah sebuah simulator kehidupan yang memiliki konsep mirip dengan permainan The Sims. Seperti yang kita ketahui, 
The Sims adalah sebuah permainan yang mengharuskan sim kita tetap hidup dengan cara melakukan berbagai hal yang realistis alias ada di dunia nyata 
seperti tidur, makan, dan buang air

"""
#Fungsi-fungsi yang digunakan
"""
def MainMenu():
    I.S. Program dijalankan/aksi baru saja diberikan
    F.S. program menampilkan atribut terkini, menu, dan meminta masukan sesuai aksi yang diinginkan 

def bersihinTerminal():
    I.S. terminal dalam keadaan sembarang
    F.S. semua tulisan yang tercetak di terminal sebelum fungsi ini dipanggil terhapus

def isFinished000():
    mengembalikan benar ketika Hygiene, Fun, dan Energy bernilai 0

def isFinished151515():
    mengembalikan benar ketika Hygiene, Fun, dan Energy bernilai 15

def tampilkanAtribut():
    I.S. -
    F.S. nilai atribut terkini tercetak di layar
-------------------------------------------------------------------------------------------------------------------------------------
def pilihTidur():
    I.S. pemain memasukkan input perintah untuk tidur
    F.S. mengubah nilai atribut sesuai jenis tidur yang dipilih. Jika setelah diubah, atribut tidak menyalahi aturan
    1. Tidur siang : +10 Energy
    2. Tidur malam : +15 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihMakan():
    I.S. pemain memasukkan input perintah untuk makan
    F.S. mengubah nilai atribut sesuai jenis makanan yang dipilih. Jika setelah diubah, atribut tidak menyalahi aturan
    1. Hamburger : +5 Energy
    2. Pizza : +10 Energy
    3. Steak and Beans : +15 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihMinum():
    I.S. pemain memasukkan input perintah untuk minum
    F.S. mengubah nilai atribut sesuai jenis minuman yang dipilih. Jika setelah diubah, atribut tidak menyalahi aturan
    1. Air : -5 Hygiene
    2. Kopi : +5 Energy; -5 Hygiene
    3. Jus : +10 Energy; -5 Hygiene
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihBuangAir():
    I.S. pemain memasukkan input perintah untuk buang air
    F.S. mengubah nilai atribut jika setelah diubah sesuai jenis buang airnya, atribut tidak menyalahi aturan
    1. Buang air kecil: +5 Hygiene
    2. Buang air besar: +10 Hygiene; -5 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihKeKafe():
    I.S. pemain memasukkan input perintah untuk besosialisasi ke kafe
    F.S. mengubah nilai atribut jika setelah diubah, atribut tidak menyalahi aturan
    Perubahan: +15 fun; -10 energy; -5 hygiene
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihMedSos():
    I.S. pemain memasukkan input perintah untuk bermain media sosial
    F.S. mengubah nilai atribut jika setelah diubah, atribut tidak menyalahi aturan
    Perubahan: +10 fun; -10 energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihKomputer():
    I.S. pemain memasukkan input perintah untuk bermain komputer
    F.S. mengubah nilai atribut jika setelah diubah, atribut tidak menyalahi aturan
    Perubahan: +15 Fun; -10 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihMandi():
    I.S. pemain memasukkan input perintah untuk mandi
    F.S. mengubah nilai atribut jika setelah diubah, atribut tidak menyalahi aturan
    Perubahan: +15 Hygiene; -5 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihCuciTangan():
    I.S. pemain memasukkan input perintah untuk cuci tangan
    F.S. mengubah nilai atribut jika setelah diubah, atribut tidak menyalahi aturan
    Perubahan: +5 Hygiene 
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihRadio():
    I.S. pemain memasukkan input perintah untuk mendengarkan musik di radio
    F.S. mengubah nilai atribut jika setelah diubah, atribut tidak menyalahi aturan
    Perubahan: +10 Fun; -5 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan

def pilihMembaca():
    I.S. pemain memasukkan input perintah untuk membaca
    F.S. mengubah nilai atribut sesuai jenis bacaan yang dipilih jika setelah diubah, atribut tidak menyalahi aturan
    1. Koran: +5 Fun; -5 Energy
    2. Novel: +10 Fun; -5 Energy
    atau mencetak "Aksi tidak valid" dan kembali ke menu awal jika tidak memenuhi aturan


"""



#------------------------------------------------------------------------------------------------------------------------------------

import subprocess, platform #buat bersihin terminal

#Kondisi awal permainan - kondisi: Bangun tidur
Hygiene = 0 #Bangun tidur ku terus mandi
Energy = 10 #Bangun tidur sih harusnya seger
Fun = 0 #Kok dia bangun tidur sedih sih :(


#MainMenu
def MainMenu():
    while(not (isFinished000() or isFinished151515() )):
        tampilkanAtribut()
        print (" ")
        print (" ")
        print("Pilih aksi yang diinginkan")
        print("1. Tidur")
        print("2. Makan")
        print("3. Minum")
        print("4. Buang Air")
        print("5. Bersosialisasi ke Kafe")
        print("6. Bermain Media Sosial")
        print("7. Bermain Komputer")
        print("8. Mandi")
        print("9. Cuci Tangan")
        print("10. Mendengarkan Musik di Radio")
        print("11. Membaca")
        inputPemain = str(input("Kamu mau ngapain??? "))
        if (inputPemain == ('1')):
            bersihinTerminal()
            pilihTidur()
        elif (inputPemain == ("Tidur")):
            bersihinTerminal()
            pilihTidur()
        elif (inputPemain == ("tidur")):
            bersihinTerminal()
            pilihTidur()
        elif (inputPemain == ('2')):
            bersihinTerminal()
            pilihMakan()
        elif (inputPemain == ("Makan")):
            bersihinTerminal()
            pilihMakan()
        elif (inputPemain == ("makan")):
            bersihinTerminal()
            pilihMakan()
        elif (inputPemain == ('3')):
            bersihinTerminal()
            pilihMinum()
        elif (inputPemain == ("Minum")):
            bersihinTerminal()
            pilihMinum()
        elif (inputPemain == ("minum")):
            bersihinTerminal()
            pilihMinum()
        elif (inputPemain == ('4')):
            bersihinTerminal()
            pilihBuangAir()
        elif (inputPemain == ("Buang Air")):
            bersihinTerminal()
            pilihBuangAir()
        elif (inputPemain == ("buang air")):
            bersihinTerminal()
            pilihBuangAir()
        elif (inputPemain == ('5')):
            bersihinTerminal()
            pilihKeKafe()
        elif (inputPemain == ("Bersosialisasi ke Kafe")):
            bersihinTerminal()
            pilihKeKafe()
        elif (inputPemain == ("bersosialisasi ke kafe")):
            bersihinTerminal()
            pilihKeKafe()
        elif (inputPemain == ('6')):
            bersihinTerminal()
            pilihMedSos()
        elif (inputPemain == ("Bermain Media Sosial")):
            bersihinTerminal()
            pilihMedSos()
        elif (inputPemain == ("bermain media sosial")):
            bersihinTerminal()
            pilihMedSos()
        elif (inputPemain == ('7')):
            bersihinTerminal()
            pilihKomputer()
        elif (inputPemain == ("Komputer")):
            bersihinTerminal()
            pilihKomputer()
        elif (inputPemain == ("komputer")):
            bersihinTerminal()
            pilihKomputer()
        elif (inputPemain == ('8')):
            bersihinTerminal()
            pilihMandi()
        elif (inputPemain == ("Mandi")):
            bersihinTerminal()
            pilihMandi()
        elif (inputPemain == ("mandi")):
            bersihinTerminal()
            pilihMandi()
        elif (inputPemain == ('9')):
            bersihinTerminal()
            pilihCuciTangan()
        elif (inputPemain == ("Cuci Tangan")):
            bersihinTerminal()
            pilihCuciTangan()
        elif (inputPemain == ("cuci tangan")):
            bersihinTerminal()
            pilihCuciTangan()
        elif (inputPemain == ('10')):
            bersihinTerminal()
            pilihRadio()
        elif (inputPemain == ("Mendengarkan Musik di Radio")):
            bersihinTerminal()
            pilihRadio()
        elif (inputPemain == ("mendengarkan musik di radio")):
            bersihinTerminal()
            pilihRadio()
        elif (inputPemain == ('11')):
            bersihinTerminal()
            pilihMembaca()
        elif (inputPemain == ("Membaca")):
            bersihinTerminal()
            pilihMembaca()
        elif (inputPemain == ("membaca")):
            bersihinTerminal()
            pilihMembaca()
        elif(inputPemain == "Keluar"):
            global Hygiene, Fun, Energy
            Hygiene = 15
            Fun = 15
            Energy = 15
        elif(inputPemain == "keluar"):
            Hygiene = 15
            Fun = 15
            Energy = 15
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()

def bersihinTerminal():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #Biar terminal bersih 
    else: #Linux and Mac
        print("\033c", end="")

#kondisi permainan
def isFinished000():
    global Energy, Hygiene, Fun
    return ((Energy == 0) and (Hygiene == 0) and (Fun == 0))

def isFinished151515():
    global Energy, Hygiene, Fun
    return ((Energy == 15) and (Hygiene == 15) and (Fun == 15))


#-------------------------------------------------------------------------------------------------------------------------------------------------------

#Fungsi-fungsi yang digunakan
def tampilkanAtribut(): #Digunakan untuk menampilkan atribut terkini
    print("Ini adalah atribut terkini anda")
    print("")
    print("1. Hygiene = " + str(Hygiene))
    print("2. Energy = " + str(Energy))
    print("3. Fun = " + str(Fun))

def pilihTidur(): #Buat Tidur 
    global Energy
    bersihinTerminal()
    print("Tidur apa nih???")
    print("----------------------------")
    print("")
    print("")
    print("1. Tidur Siang")
    print("2. Tidur Malam")
    print(" ")
    print ("3. Kembali ke Main Menu")
    a = str(input("Masukkan kode keinginan: "))
    if (a == ('1')):
        if (((Energy) + 10) <= 15):
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("")
            print("")
            MainMenu()
    elif (a == ("Tidur Siang")):
        if (((Energy) + 10) <= 15):
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("")
            print("")
            MainMenu()
    elif (a == ("tidur siang")):
        if (((Energy) + 10) <= 15):
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("")
            print("")
            MainMenu()
    elif (a == '2'):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "Tidur Malam"):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "tidur malam"):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == '3'):
        bersihinTerminal()
        MainMenu()
    elif (a == "Kembali"):
        bersihinTerminal()
        MainMenu()
    elif (a == "kembali"):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()

def pilihMakan(): #Buat Makan
    global Energy
    bersihinTerminal()
    print("Makan pake apa nih???")
    print("----------------------------")
    print("")
    print("")
    print("1. Hamburger")
    print("2. Pizza")
    print("3. Steak and Beans")
    print(" ")
    print ("4. Kembali ke sub-menu")
    a = str(input("Mau makan apa?? "))
    if (a == ("1" and "hamburger" and "Hamburger")):
        if ((Energy + 5) <= 15):
            Energy = Energy + 5
            bersihinTerminal()
            MainMenu()
            
        else:
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == ("2" and "Pizza" and "pizza")):
        if ((Energy + 10) <= 15):
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == ("3" and "Steak and Beans" and "steak and beans")):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            MainMenu()
    elif (a == ("4" and "Kembali" and "kembali")):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()

def pilihMinum(): #Buat Minum
    global Energy, Hygiene
    bersihinTerminal()
    print("Minum pake apa nih???")
    print("----------------------------")
    print("")
    print("")
    print("1. Air")
    print("2. Kopi")
    print("3. Jus")
    print(" ")
    print ("4. Kembali ke sub-menu")
    a = str(input("Mau minum apa?? "))
    if (a == "Air"): #Minum Air
        if ((Hygiene) >= 5):
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
            
        else:
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "air"): #Minum Air
        if ((Hygiene) >= 5):
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
        else:
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == '2'): #Minum Kopi
        if ((Energy + 5) <= 15) and (Hygiene >= 10):
            Energy = Energy + 5
            Hygiene = Hygiene - 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == "Kopi"): #Minum Kopi
        if ((Energy + 5) <= 15) and (Hygiene >= 10):
            Energy = Energy + 5
            Hygiene = Hygiene - 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == "kopi"): #Minum Kopi
        if ((Energy + 5) <= 15) and (Hygiene >= 10):
            Energy = Energy + 5
            Hygiene = Hygiene - 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == '3'): #Minum Jus
        if (((Energy + 10) <= 15) and (Hygiene >= 5)):
            Energy = Energy + 10
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == "Jus"): #Minum Jus
        if (((Energy + 10) <= 15) and (Hygiene >= 5)):
            Energy = Energy + 10
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == "jus"): #Minum Jus
        if (((Energy + 10) <= 15) and (Hygiene >= 5)):
            Energy = Energy + 10
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            bersihinTerminal()
            MainMenu()
    elif (a == '4'):
        bersihinTerminal()
        MainMenu()
    elif (a == "Kembali"):
        bersihinTerminal()
        MainMenu()
    elif (a == "kembali"):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()

def pilihBuangAir(): #Buat Buang Air 
    global Energy, Hygiene
    bersihinTerminal()
    print("Gede keci???")
    print("----------------------------")
    print("")
    print("")
    print("1. Buang Air Kecil")
    print("2. Buang Air Besar")
    print(" ")
    print ("3. Kembali ke Main Menu")
    a = str(input("Masukkan kode keinginan: "))
    if (a == '1'):
        if (Hygiene <= 10):
            Hygiene = Hygiene + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "Kencing"):
        if (Hygiene <= 10):
            Hygiene = Hygiene + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "kencing"):
        if (Hygiene <= 10):
            Hygiene = Hygiene + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "Buang Air Kecil"):
        if (Hygiene <= 10):
            Hygiene = Hygiene + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == '2'):
        if ((Hygiene + 10) <= 15) and (Energy >= 5):
            Energy = Energy - 5
            Hygiene = Hygiene + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "BAB"):
        if ((Hygiene + 10) <= 15) and (Energy >= 5):
            Energy = Energy - 5
            Hygiene = Hygiene + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "bab"):
        if ((Hygiene + 10) <= 15) and (5 <= Energy):
            Energy = Energy - 5
            Hygiene = Hygiene + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "Buang Air Besar"):
        if ((Hygiene + 10) <= 15) and (5 <= Energy):
            Energy = Energy - 5
            Hygiene = Hygiene + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == '3'):
        bersihinTerminal()
        MainMenu()
    elif (a == "Kembali"):
        bersihinTerminal()
        MainMenu()
    elif (a == "kembali"):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()

def pilihKeKafe(): #Buat Nongki ke Kafe bray
    global Fun, Hygiene, Energy
    if ((Fun == 0) and (Energy >= 10) and (Hygiene >= 5)):
            Energy = Energy - 10
            Fun = Fun + 15
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("--------------------------------------------------------------------------")
        print("")
        print("")
        MainMenu()

def pilihMedSos(): #Buat mainan medsos
    global Hygiene, Fun, Energy
    if ((Fun <= 5) and (Energy >= 10)):
            Energy = Energy - 10
            Fun = Fun + 10
            bersihinTerminal()
            MainMenu()
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("--------------------------------------------------------------------------")
        print("")
        print("")
        MainMenu()

def pilihKomputer(): #Buat nubes kali bray
    global Hygiene, Fun, Energy
    if ((Fun == 0) and (Energy >= 10)):
            Fun = Fun + 15
            Energy = Energy - 10
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("--------------------------------------------------------------------------")
        print("")
        print("")
        MainMenu()

def pilihMandi(): #Buat mandi
    global Hygiene, Energy
    if ((Hygiene == 0) and (Energy >= 5)):
            Energy = Energy - 5
            Hygiene = Hygiene + 15
            bersihinTerminal()
            MainMenu()
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("--------------------------------------------------------------------------")
        print("")
        print("")
        MainMenu()

def pilihCuciTangan(): #Buat cuci tangan
    global Hygiene
    if (Hygiene <= 10):
            Hygiene = Hygiene + 5
            bersihinTerminal()
            MainMenu()
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("--------------------------------------------------------------------------")
        print("")
        print("")
        MainMenu()

def pilihRadio(): #Buat mainan medsos
    global Fun, Energy
    if ((Fun <= 5) and (Energy >= 5)):
            Energy = Energy - 5
            Fun = Fun + 5
            bersihinTerminal()
            MainMenu()
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("--------------------------------------------------------------------------")
        print("")
        print("")
        MainMenu()

def pilihMembaca(): #Buat membaca
    global Energy, Fun
    bersihinTerminal()
    print("Mau baca apa nih???")
    print("----------------------------")
    print("")
    print("")
    print("1. Koran")
    print("2. Novel")
    print(" ")
    print ("3. Kembali ke Main Menu")
    a = str(input("Masukkan kode keinginan: "))
    if (a == ("Koran")):
        if ((Energy >= 5) and (Fun <= 10)):
            Energy = Energy - 5
            Fun = Fun + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == ("koran")):
        if ((Energy >= 5) and (Fun <= 10)):
            Energy = Energy - 5
            Fun = Fun + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == ('1')):
        if ((Energy >= 5) and (Fun <= 10)):
            Energy = Energy - 5
            Fun = Fun + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == ("Novel")):
        if ((Energy >= 5) and (Fun <= 5)):
            Energy = Energy - 5
            Fun = Fun + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == ("novel")):
        if ((Energy >= 5) and (Fun <= 5)):
            Energy = Energy - 5
            Fun = Fun + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == ('2')):
        if ((Energy >= 5) and (Fun <= 5)):
            Energy = Energy - 5
            Fun = Fun + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()
    elif (a == "Kembali"):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("--------------------------------------------------------------------------")
            print("")
            print("")
            MainMenu()



#------------------------------------------------------------------------------------------------------------

#ALGORITMA PERMAINAN

#Permainan dimulai
bersihinTerminal
print("SELAMAT DATANG DI PERMAINAN THE SIMS SIMULATOR DUARRRR!!!!")
print("----------------------------------------------------")
print(" ")
print(" ")
MainMenu()


#Permainan selesai
bersihinTerminal()
print("Permainan Selesai!!")
print("")
print("")
iseng = str(input("Press Enter to Exit"))