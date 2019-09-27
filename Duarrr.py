Hygiene = 0
Energy = 10
Fun = 0

print("SELAMAT DATANG DI PERMAINAN DE SIMS DUARRRR!!!!")
print("----------------------------------------------------")
print()

#MainMenu
def MainMenuAksi():
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



#Fungsi-fungsi yang digunakan
def tampilkanAtribut(): #Digunakan untuk menampilkan atribut terkini
    print("Ini adalah atribut terkini anda")
    print("")
    print("1. Hygiene = " + str(Hygiene))
    print("2. Energy = " + str(Energy))
    print("3. Fun = " + str(Fun))

def pilihTidur():
    print("Tidur apa nih???")
    print("----------------------------")
    print("")
    print("")
    print("1. Tidur Siang")
    print("2. Tidur Malam")
