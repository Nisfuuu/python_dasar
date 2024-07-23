import main

def start():
    while True:
        print("ini warung apps!")
        harga = int(input("total: "))
        print(harga)
        play_again = input("kembali ke menu utama? [y/n]")
       
        if play_again == "y":
            main.menu()
            break
        
if __name__ == '__main__':
    start()