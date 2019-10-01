#Project The Sims Simulator
#Tugas Besar 1 TBFO

Cara menjalankan:

<Cara 1>
1. Git pull repository ini/download zipnya
2. Buka folder dist
3. Buka folder RediNadiaTBFO
4. Buka folder RediNadiaTBFO.exe

<Cara 2>
1. Git pull repository ini/download zipnya
2. Buka terminal di folder RediNadiaTBFO (folder yang ada di zip) ~/[Tempat repository ditarik atau zipnya diekstrak]/
3. Eksekusi RediNadiaTBFO.py dengan mengetik "python RediNadiaTBFO.py"

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
