import main
from services import db
def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = input('harga barang: ')
    
    stok_barang = int(input('stok barang: '))
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)

def check():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
kode #{kode_barang}
{nama_barang} | Rp.{harga_barang}
stok {stok_barang}''')
        
def update():
    kode_barang = input('Masukkan kode barang yang ingin diupdate: ')
    
    # Prompt user for new values
    nama_barang = input('Masukkan nama barang baru (tekan Enter untuk melewati): ')
    harga_barang = input('Masukkan harga barang baru (tekan Enter untuk melewati): ')
    stok_barang = input('Masukkan stok barang baru (tekan Enter untuk melewati): ')

    # Convert inputs to appropriate types or None
    nama_barang = nama_barang if nama_barang else None
    harga_barang = int(harga_barang) if harga_barang else None
    stok_barang = int(stok_barang) if stok_barang else None

    # Call the update method from the db module
    db.update_item(kode_barang, nama_barang, harga_barang, stok_barang)

    db.update_item(kode_barang, nama_barang, harga_barang, stok_barang)
    print(f'Barang dengan kode {kode_barang} telah diupdate.')
    print("With parameters:", (nama_barang, harga_barang, stok_barang, kode_barang))
        
def delete():
    kode_barang = int(input('Masukkan kode barang yang ingin dihapus: '))
    db.delete_item(kode_barang)
    print(f'Barang dengan kode {kode_barang} telah dihapus.')

def start():
    while True:
        menu = int(input("menu:\n1. Tambah barang\n2. Check barang\n3. Kembali: "))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
            menu_warung = int(input("\n1. update barang\n2. delete barang\n3. kembali ke menu utama: "))
            if menu_warung == 1:
                update()
                
            elif menu_warung == 2:
                delete()
            elif menu_warung == 3:
                main.menu()
        elif menu == 3:
            main.menu()
        else:
            break
            
       
        play_again = input("kembali ke menu utama? [y/n]")
       
        if play_again == "y":
            main.menu()
            break
        
if __name__ == '__main__':
    start()