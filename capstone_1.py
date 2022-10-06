# Menu Cantik untuk Stock Buah
listMarket = [
    {
        'Kode' : 'Fru01',
        'Nama' : 'Apel',
        'Stock' : 20,
        'Asal' : 'Jepang',
        'Harga' : 10000
    },
    {
        'Kode' : 'Fru02',
        'Nama' : 'Jeruk',
        'Stock' : 15,
        'Asal' : 'Medan',
        'Harga' : 15000
    },
    {
        'Kode' : 'Fru03',
        'Nama' : 'Anggur',
        'Stock' : 25,
        'Asal' : 'Australia',
        'Harga' : 20000
    }
]

# Function Simpel
def divider ():
    print('----------------------------------------------------------------')

def printBuah(kodeIndex):
    print('Kode   \t|Nama    \t|Stock   \t|Asal   \t|Harga')
    print('{}  \t|{}   \t|{}     \t|{}   \t|{}'.format(listMarket[kodeIndex]['Kode'], listMarket[kodeIndex]['Nama'],listMarket[kodeIndex]['Stock'],listMarket[kodeIndex]['Asal'], listMarket[kodeIndex]['Harga']))


# List untuk Menu Awal
listMenu = ['1. Menampilkan Daftar Buah', '2. Menambah Buah', '3. Mengubah Data Buah', '4. Menghapus Buah' ,'5. Exit Program']
listMenu1 = ['1. Menampilkan Seluruh Buah', '2. Menampilkan Buah Tertentu', '3. Kembali ke Menu Utama']
listMenu2 = ['1. Tambah Data Buah','2. Kembali ke Menu Utama']
listMenu3 = ['1. Ubah Data Buah', '2. Kembali ke Menu Utama']
listMenu4 = ['1. Menghapus Data Buah', '2. Kembali ke Menu Utama']

# While membuat program terus looping sampai dipilihnya menu 5
while True:
    for i in listMenu:
        print(i)
    inputMenu = str(input('Silahkan Pilih Menu yang Diinginkan : '))
    divider()
# Menu 1 - Menampilkan Stock Buah
    if inputMenu == '1':
        while True:
            for i in listMenu1:
                print(i)
            inputMenu1 = str(input('Silahkan Pilih Menu yang Diinginkan : '))
            # Menu 1 Sub 1 - Menampilkan Semua Stock Buah
            if inputMenu1 == '1':
                if len(listMarket) == 0:
                    print('------------Tidak Ada Data------------')
                else:
                    print('Kode   \t|Nama    \t|Stock   \t|Asal       \t|Harga')
                    for i in range(len(listMarket)):
                        print('{}  \t|{}   \t|{}     \t|{}   \t|{}'.format(listMarket[i]['Kode'], listMarket[i]['Nama'],listMarket[i]['Stock'],listMarket[i]['Asal'], listMarket[i]['Harga']))
                    divider()
            # Menu 1 Sub 2 - Menampilkan Buah yang Dipilih
            elif inputMenu1 == '2':
                if len(listMarket) == 0:
                    print('------------Tidak Ada Data------------')
                else :
                    inputMenu1Sub2 = str(input('Silahkan Masukan Kode Buah : ')).capitalize()
                    print(f'Data Buah {inputMenu1Sub2}')
                    listTrue = []
                    for i in range(len(listMarket)):
                        listTrue.append(inputMenu1Sub2 == listMarket[i]['Kode'])
                    if True in listTrue :
                        indexBuah = listTrue.index(True)
                        printBuah(indexBuah)
                        divider()
                    else :
                        print('------------Tidak Ada Data------------')
                        divider()
            # Menu 1 Sub 3 - Kembali ke Menu Sebelum
            elif inputMenu1 == '3':
                print('Kembali Ke Menu Utama')
                divider()
                break
            else:
                print('Masukan Angka Menu yang Benar')
                divider()
# Menu 2 - Menambah Stock Buah
    elif inputMenu == '2':
        while True: 
            for i in listMenu2:
                print(i)
            inputMenu2 = str(input('Silahkan Pilih Menu yang Diinginkan : '))
            # Menu 2 Sub 1 - Menambah Stock Buah
            if inputMenu2 == '1':
                inputMenu2Sub1 = str(input('Masukan Kode Buah Baru : ')).capitalize()
                listTrue = []
                for i in range(len(listMarket)):
                    listTrue.append(inputMenu2Sub1 == listMarket[i]['Kode'])
                if True in listTrue :# Kalau Data sudah ada(True), akan ditolak
                    print('Data Sudah ada, Mohon Masukan Kode Buah Lain')
                    divider()
                else :# Kalau enggak ada(False semua list), akan masuk
                    tambahBuah = (input('Masukan Nama Buah : ')).capitalize()
                    tambahStock = (input('Masukan Stock Buah : '))
                    tambahAsal = (input('Masukan Asal Buah : ')).capitalize()
                    if len(tambahAsal) < 9:
                        tambahAsal = tambahAsal + ' '*(9-len(tambahAsal))
                    tambahHarga = (input('Masukan Harga Buah : '))
                    while True: # Akan Putar Terus sampai diberikan Jawaban Y/N
                        simpanDataMenu2Sub1 = str(input('Apakah Data Mau Disimpan?(Y/N) : ')).upper()
                        if simpanDataMenu2Sub1 == 'Y':
                            listMarket.append({'Kode' : inputMenu2Sub1,'Nama' : tambahBuah, 'Stock' : tambahStock,'Asal' : tambahAsal, 'Harga' : tambahHarga})
                            print('Data Tersimpan')
                            divider()
                            break
                        elif simpanDataMenu2Sub1 == 'N':
                            print('Data Tidak Disimpan')
                            divider()
                            break
                        else :
                            print('Mohon Masukan Y/N Saja')
            elif inputMenu2 == '2':# Menu 2 Sub 2 - Kembali
                print('Kembali Ke Menu Utama')
                divider()
                break
            else :
                print('Masukan Angka Menu yang Benar')
                divider()
    elif inputMenu == '3': # Menu 3 - Meng Update Stock Buah
        while True: 
            for i in listMenu3:
                print(i)
            inputMenu3 = str(input('Silahkan Pilih Menu yang Diinginkan : '))
            if inputMenu3 == '1': # Menu 3 Sub 1 - Update Data Buah
                inputMenu3Sub1 = str(input('Masukan Kode Buah yang ingin Diubah : ')).capitalize()
                listTrue = []
                for i in range(len(listMarket)):
                    listTrue.append(inputMenu3Sub1 == listMarket[i]['Kode'])
                if True in listTrue: # Kalo ada (True), Akan update
                    indexBuahUpdate = listTrue.index(True)
                    printBuah(indexBuahUpdate)
                    while True: # Looping sampai dapat Y/N (Bagian Lanjut Update)
                        inputLanjutUpdate = input('Apakah Mau Lanjut Update (Y/N) : ').capitalize()
                        if inputLanjutUpdate == 'Y':
                            while True: # Looping (Bagian Tanya Column yang ingin diubah)
                                inputMenu3Sub1Ubah = input('Masukan Column apa Yang Ingin di Ubah : ').capitalize()
                                if inputMenu3Sub1Ubah in ['Nama','Asal','Harga','Stock']:
                                    inputUpdateStockStr = (input('Masukan Data yang Baru : ')).capitalize()
                                    while True : # Looping (Bagian Tanya setelah masukan colum dan data)
                                        inputLanjutUpdate2 = input(f'Apakah {inputMenu3Sub1Ubah} Ingin Diubah (Y/N) : ').capitalize()
                                        if inputLanjutUpdate2 ==  'Y':
                                            print(f'{inputMenu3Sub1Ubah} Updated')
                                            divider()
                                            listMarket[indexBuahUpdate][f'{inputMenu3Sub1Ubah}'] = inputUpdateStockStr
                                            break
                                        elif inputLanjutUpdate2 == 'N':
                                            print(f'{inputMenu3Sub1Ubah} Tidak Di Update')
                                            break
                                        else:
                                            print('Mohon Masukan Y/N Saja')
                                    break
                                elif inputMenu3Sub1Ubah == 'Kode': # Klo mau Ubah Kode Buah, Jika kode buah sama, maka akan ditolak
                                    inputUpdateStockStr = (input('Masukan Data yang Baru : ')).capitalize()
                                    listTrue = []
                                    for i in range(len(listMarket)):
                                        listTrue.append(inputUpdateStockStr == listMarket[i]['Kode'])
                                    if True in listTrue :
                                        print('Kode Buah Sudah ada di buah lain, mohon gunakan Kode Unik lainnya')
                                    else :
                                        inputLanjutUpdate2 = input(f'Apakah {inputMenu3Sub1Ubah} Ingin Diubah (Y/N) : ').capitalize()
                                        if inputLanjutUpdate2 ==  'Y':
                                            print(f'{inputMenu3Sub1Ubah} Updated')
                                            divider()
                                            listMarket[indexBuahUpdate][f'{inputMenu3Sub1Ubah}'] = inputUpdateStockStr
                                            break
                                        elif inputLanjutUpdate2 == 'N':
                                            print(f'{inputMenu3Sub1Ubah} Tidak Di Update')
                                            break
                                        else:
                                            print('Mohon Masukan Y/N Saja')
                                else:
                                    print(f'Column {inputMenu3Sub1Ubah} Tidak Ada, Mohon Masukan Nama Column yang Benar')
                            break
                        elif inputLanjutUpdate == 'N':
                            print('Data tidak Jadi Diupdate')
                            divider()
                            break
                        else :
                            print('Mohon Masukan Y/N Saja')
                else:
                    print('Data Tidak Ada')
                    divider()
            # Menu 3 Sub 2 - Kembali
            elif inputMenu3 == '2':
                print('Kembali Ke Menu Utama')
                divider()
                break
            else :
                print('Masukan Angka Menu yang Benar')
                divider()
# Menu 4 - Men Delete Stock Buah
    elif inputMenu == '4':
        while True:
            for i in listMenu4:
                print(i)
            inputMenu4 = str(input('Silahkan Pilih Menu yang Diinginkan : '))
            if inputMenu4 == '1':
                inputDelete = str(input('Masukan Kode Buah yang Ingin Di Delete : ')).capitalize()
                listTrue = []
                for i in range(len(listMarket)):
                    listTrue.append(inputDelete == listMarket[i]['Kode'])
                if True in listTrue: # Delete Data jika ada (True)
                    indexBuahDelete = listTrue.index(True)
                    printBuah(indexBuahDelete)
                    divider()
                    while True:
                        lanjutDelete = input('Apakah Data Buah ingin Di Delete (Y/N) : ').capitalize()
                        if lanjutDelete == 'Y':
                            print('Data Deleted')
                            del listMarket[indexBuahDelete]
                            break
                        elif lanjutDelete == 'N':
                            print('Data Tidak Di Delete')
                            break
                        else:
                            print('Mohon Masukan Y/N Saja')
                else : # Enggak ada Data
                    print('Data Tidak Ada')
            elif inputMenu4 == '2':
                print('Kembali ke Menu Utama')
                divider()
                break
            else:
                print('Masukan Angka Menu yang Benar')
                divider()
# Menu 5 - Keluar
    elif inputMenu == '5':
        print("Selamat Tinggal")
        break
    else :
        print('Menu yang anda pilih tidak ada, mohon untuk memilih menu yang benar')
