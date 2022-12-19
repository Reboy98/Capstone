# capstn

listKontak = {
    'cn1': {
        'Nama Depan': 'Rahmad',
        'Nama Belakang' : 'peratama',
        'No Telepon' : '6205566383383',
        'Company': 'Dsi',
        'Alamat' : 'Cibubur'
    },

    'cn2':{
        'Nama Depan': 'Aji',
        'Nama Belakang' : 'Sulaiman' ,
        'No Telepon' : '6281919383383',
        'Company': 'Maju',
        'Alamat' : 'Depok'
    },

    'cn3':{
        'Nama Depan' : 'Adi', 
        'Nama Belakang': 'Muhargia',
        'No Telepon' : '6289629910011',
        'Company' : 'Ubud',
        'Alamat': 'Medan',
    }
}

#menampilkan data
def dataKontak () :
    while True:
        menu1 = int(input('''
            
                         Contact 
            1. Tampilkan seluruh kontak
            2. Cari Kontak
            3. Kembali ke menu utama
            Pilih menu yang ingin dijalankan : '''))
        if menu1 == 1 :
            print('''

                                         Daftar Nomor Kontak 

                Nama Depan\t| Nama Belakang\t| No Telepon\t| Company\t \t| Alamat ''')

            for i in listKontak:
                print(f"{i}\t{listKontak[i]['Nama Depan']}\t\t\t| {listKontak[i]['Nama Belakang']}\t|{listKontak[i]['No Telepon']}\t|{listKontak[i]['Company']}\t\t\t|{listKontak[i]['Alamat']}\t")
            if len(listKontak)==0:
                print('    Kontak Tidak Ditemukan     ')

        elif menu1 == 2 :
            print('     Cari Kontak    ')
            cari = input('Search: ').title() 
            if listKontak == {} :
                    print ('kontak tidak ditemukan')
                    dataKontak()
            else:        
                for k,v in listKontak.items():
                    for m in v.values():
                        if m == cari:
                            print(' Nama Depan\t| Nama Belakang\t| No Telepon\t\t| Company\t| Alamat')
                            print(f"{k}\t| {listKontak[k]['Nama Depan']} \t| {listKontak[k]['Nama Belakang']} \t| {listKontak[k]['No Telepon']}\t\t| {listKontak[k]['Company']}\t\t| {listKontak[k]['Alamat']}")

        elif menu1 == 3 :
            menu()
            break
        else:
            print('Pilih Menu Yang Ingin Dijalankan')

#menambah data 
def tambahKontak():
    while True:
        menu2 = int(input('''

                     Tambah Kontak 
            1. Tambah Kontak Baru 
            2. Kembali ke menu utama
            
            Pilih menu yang ingin dijalankan : '''))
        if menu2 == 1 :
            kode = input('Cek No Telepon : ') # Apakah tersedia atau tidak?
            count = 0 # Untuk mengecek nomornya sudah terdaftar atau belum
            for v in listKontak.values():
                for m in v.values():  
                    if m == kode :
                        count += 1
            if count > 0:
                print('No Sudah Terdaftar')
            else: # Apabila belum terdaftar makan input data dibawah
                print('Nomor belum terdaftar.\nSilahkan masukkan data yang ingin ditambahkan \n')
                namaDepan = input('Nama Depan : ').title()
                namaBelakang = input('Nama Belakang : ').title()
                noTelepon= input('No Telepon : ').title()
                Company = input('Company : ').title()
                Alamat = input('Alamat: ').title()
                
                for k in listKontak.keys(): # Untuk mengupdate kode id (cth:cn3)
                    pass
                kode_blkg = int(k[-1]) + 1
                kode_id = k[:2] + str(kode_blkg)
                
                while True:
                    ask = input('Apakah data yang anda masukan telah benar (y/t) :').lower()
                    if (ask.lower() == 'y'):
                        listKontak.update({
                            kode_id:{
                                'Nama Depan': namaDepan,
                                'Nama Belakang' : namaBelakang,
                                'No Telepon': noTelepon,
                                'Company' : Company,
                                'Alamat' : Alamat
                            }})
                        print('Data tersimpan')
                        break
                    elif (ask == 't'):
                        break
        elif menu2 == 2 :
            menu()
            break
        else :
            print('Pilih Menu Yang Ingin Dijalankan')
            

# #mengedit data
def editKontak():  
    while True:
        menu3 = int(input('''
                       Mengubah Data Kontak           
                1. Edit Kontak
                2. Kembali ke menu utama
                Pilih menu yang ingin dijalankan :  '''))
        
        if menu3 == 1 :
            Kode_id = input('Masukkan kode id: ')
            count = 0
            for k in listKontak.keys():
                if Kode_id == k:
                    count += 1
                    print(f"Berikut datanya:\n{k}\t| {listKontak[k]['Nama Depan']}\t| {listKontak[k]['Nama Belakang']}\t\t| {listKontak[k]['No Telepon']} \t| {listKontak[k]['Company']} \t| {listKontak[k]['Alamat']}\t")

                    kategori = input('Data Yang Ingin Anda Edit: ').title()
                    for k,v in listKontak.items():
                        for n in v.keys():
                            if k == Kode_id and n == kategori:
                                nilai = input('Masukkan Data Yang Ingin Diubah:').title()
                                while True:
                                    ask = input('Apakah data yang anda masukan telah benar (y/t) :').lower()
                                    if (ask == 'y'):
                                        listKontak[k][n] = nilai
                                        print('Data Telah Tersimpan')
                                        break
                                    elif (ask == 't'):
                                        pass
                                    else:
                                        print('Apakah Anda Yakin (y/n) ')
            if count == 0:
                print('Data tidak ditemukan!')

        elif menu3 == 2 :
            menu()
            break
        else :
            print('Pilih Menu Yang Ingin Yang Ingin Dijalankan')

#menghapus data
def hapusKontak():
    while True:
        menu4 = int(input('''
                         Menghapus Data Kontak           
            1. Hapus Kontak
            2. Kembali ke menu utama
            Pilih menu yang ingin dijalankan : '''))
        if menu4 == 1 :
            hapus = input('Nama Kontak Yang Ingin Dihapus: ').title()
            count = 0
            listKontak2 = listKontak.copy() # Agar iterating nya bukan di dictionary defaultnya, supaya tidak terjadi error
            for k,v in listKontak2.items():
                for m in v.values(): 
                    if m == hapus:
                        count += 1
                        print(f"Berikut datanya:\n{k}\t| {listKontak[k]['Nama Depan']}\t| {listKontak[k]['Nama Belakang']}\t\t| {listKontak[k]['No Telepon']} \t| {listKontak[k]['Company']} \t| {listKontak[k]['Alamat']}\t")
                        while True:
                            ask = input('apakah anda yakin hapus Kontak ini? (y/t) :').lower()
                            if ask == 'y':
                                del listKontak[k]
                                print('Kontak Berhasil Dihapus')
                                break
                            elif (ask == 't'):
                                break
                            else:
                                print('Apakah anda yakin (y/n)')
                
            if count == 0:
                print('Kontak Tidak Ditemukan')

        elif menu4 == 2:
            menu()
            break
        else:
            print('Pilih Menu Yang Ingin Dijalankan')


#menampilkan menu
def menu(): 
    while True:
        pil = int(input( '''
        \n                Contact                \n
        Menu :
        1. Tampilkan Daftar Kontak
        2. Tambah Kontak Baru
        3. Edit Kontak
        4. Hapus Kontak
        5. Exit 
        
        Pilih Menu yang ingin dijalankan :  '''))

        if pil == 1 :
            dataKontak()
            break
        elif pil == 2 :
            tambahKontak()
            break
        elif pil == 3 :
            editKontak()
            break
        elif pil == 4 :
            hapusKontak()
            break
        elif pil == 5 :
            print ('\n\t Terima Kasih \n ')
            break
        else :
            print('\n\t\t Menu Tidak Tersedia!\n ')
menu()