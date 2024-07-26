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
        
def start():
    while True:
        menu = int(input("menu:\n1. Tambah barang\n2. Check barang\n3. Kembali: "))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
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