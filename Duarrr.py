import subprocess, platform #buat bersihin terminal




#MainMenu
def MainMenu():
    print("SELAMAT DATANG DI PERMAINAN DE SIMS DUARRRR!!!!")
    print("----------------------------------------------------")
    print(" ")
    print(" ")
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
    inputPemain = int(input("Masukkan nomor berapa yang anda inginkan: "))
    if (inputPemain == 1):
        bersihinTerminal()
        pilihTidur()


def bersihinTerminal():
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate() #Biar terminal bersih 
    else: #Linux and Mac
        print("\033c", end="")


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
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            MainMenu()
    elif (a == 3):
        bersihinTerminal()
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
        if ((Energy + 10) <= 15):
            Energy = Energy + 5
            bersihinTerminal()
            MainMenu()
            
        else:
            print("Aksi tidak valid")
            MainMenu()
    elif (a == 2):
        if ((Energy + 15) <= 15):
            Energy = Energy + 10
            bersihinTerminal()
            MainMenu()
        else:
            bersihinTerminal()
            print("Aksi tidak valid")
            MainMenu()
    elif (a == 3):
        if ((Energy + 15) <= 15):
            Energy = Energy + 15
            MainMenu()
        else:
            bersihinTerminal
            print("Aksi tidak valid")
            MainMenu()

def pilihMinum():
    

#------------------------------------------------------------------------------------------------------------

#ALGORITMA PERMAINAN
Hygiene = 0
Energy = 10
Fun = 0

bersihinTerminal
MainMenu()