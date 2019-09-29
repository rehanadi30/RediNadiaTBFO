#Project The Sims Simulator
#Creator: Rehan dan Nadia

#Nama Pembuat 1: Rehan Adi Satrya
#NIM Pembuat 1: 13518061

#Nama Pembuat 2: Putri Nadia Salsabila
#NIM Pembuat 2: 13518094
#------------------------------------------------------------------------------------------------------------------------------------

import subprocess, platform #buat bersihin terminal

#Kondisi awal permainan - kondisi: Bangun tidur
Hygiene = 0 #Bangun tidur ku terus mandi
Energy = 10 #Bangun tidur sih harusnya seger
Fun = 0 #Kok dia bangun tidur sedih sih :(


#MainMenu
def MainMenu():
    while (not(isFinished000() or isFinished151515()) ):
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
        inputPemain = str(input("Masukkan nomor berapa yang anda inginkan: "))
        if (inputPemain == 1):
            bersihinTerminal()
            pilihTidur()
        elif (inputPemain == 2):
            bersihinTerminal()
            pilihMakan()
        elif (inputPemain == 3):
            bersihinTerminal()
            pilihMinum()
        elif (inputPemain == 4):
            bersihinTerminal()
            pilihBuangAir()
        elif (inputPemain == 5):
            bersihinTerminal()
            pilihKeKafe()
        elif (inputPemain == 6):
            bersihinTerminal()
            pilihMedSos()
        elif (inputPemain == 7):
            bersihinTerminal()
            pilihKomputer()
        elif (inputPemain == 8):
            bersihinTerminal()
            pilihMandi()
        elif (inputPemain == 9):
            bersihinTerminal()
            pilihCuciTangan()
        elif (inputPemain == 10):
            bersihinTerminal()
            pilihRadio()
        elif (inputPemain == 11):
            bersihinTerminal()
            pilihMembaca()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("-----------------------------------------------------------------------")
            print("")
            MainMenu()

def bersihinTerminal():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #Biar terminal bersih 
    else: #Linux and Mac
        print("\033c", end="")

#kondisi permainan
def isFinished000(): #Kalo kalah A.K.A 0 semua huhu :(
    global Energy, Hygiene, Fun
    return ((Energy == 0) and (Hygiene == 0) and (Fun == 0))

def isFinished151515(): #Kalo menang A.K.A 15 semua HOREEEEE :)
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


#Fungsi-fungsi yang mempengaruhi atribut

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
    a = int(input("Masukkan kode keinginan: "))
    if (a == 1):
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
    elif (a == 2):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            MainMenu()
    elif (a == 3):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
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
    a = int(input("Masukkan kode keinginan: "))
    if (a == 1):
        if ((Energy + 5) <= 15):
            Energy = Energy + 5
            bersihinTerminal()
            MainMenu()
            
        else:
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 2):
        if ((Energy + 10) <= 15):
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 3):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 4):
        bersihinTerminal()
        MainMenu()
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("----------------------------------------")
        print(" ")
        print(" ")
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
    a = int(input("Masukkan kode keinginan: "))
    if (a == 1): #Minum Air
        if ((Hygiene) >= 5):
            Hygiene = Hygiene - 5
            bersihinTerminal()
            MainMenu()
            
        else:
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 2): #Minum Kopi
        if ((Energy + 5) <= 15) and (Hygiene >= 10):
            Energy = Energy + 5
            Hygiene = Hygiene - 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 3): #Minum Jus
        if (((Energy + 10) <= 15) and (Hygiene >= 5)):
            Energy = Energy + 10
            Hygiene = Hygiene - 5
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 4):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()

def pilihBuangAir(): #Buat Buang Air 
    global Energy, Hygiene
    bersihinTerminal()
    print("Gede keci???")
    print("----------------------------")
    print("")
    print("")
    print("1. Kencing")
    print("2. BAB")
    print(" ")
    print ("3. Kembali ke Main Menu")
    a = int(input("Masukkan kode keinginan: "))
    if (a == 1):
        if (Hygiene >= 5):
            Hygiene = Hygiene + 5
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("")
            print("")
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 2):
        if ((Hygiene + 10) <= 15) and (Energy >= 5):
            Energy = Energy - 5
            Hygiene = Hygiene + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 3):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
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
        print("----------------------------------------")
        print(" ")
        print(" ")
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
        print("----------------------------------------")
        print(" ")
        print(" ")
        MainMenu()

def pilihKomputer(): #Buat nubes kali bray
    global Hygiene, Fun, Energy
    if (Fun == 0):
            Fun = Fun + 15
    else:
        bersihinTerminal()
        print("Aksi tidak valid")
        print("----------------------------------------")
        print(" ")
        print(" ")
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
        print("----------------------------------------")
        print(" ")
        print(" ")
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
        print("----------------------------------------")
        print(" ")
        print(" ")
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
        print("----------------------------------------")
        print(" ")
        print(" ")
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
    a = int(input("Masukkan kode keinginan: "))
    if (a == 1):
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
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 2):
        if ((Energy >= 5) and (Fun <= 5)):
            Energy = Energy - 5
            Fun = Fun + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()
    elif (a == 3):
        bersihinTerminal()
        MainMenu()
    else:
            bersihinTerminal()
            print("Aksi tidak valid")
            print("----------------------------------------")
            print(" ")
            print(" ")
            MainMenu()



#------------------------------------------------------------------------------------------------------------

#ALGORITMA PERMAINAN

print("SELAMAT DATANG DI PERMAINAN THE SIMS SIMULATOR DUARRRR!!!!")
print("----------------------------------------------------")
print(" ")
print(" ")

MainMenu() #START GAME
print("Permainan Selesai") #END OF THE GAME