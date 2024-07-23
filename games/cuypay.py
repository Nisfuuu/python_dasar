import random
import main

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4 #goa kosong

        cuypay_posisi = random.randint(1, 4)

        goa = goa_kosong.copy() #goa copy goa kosong
        goa[cuypay_posisi - 1] = "[0_0]"
        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        print(goa_kosong)
        pilihan_user = int(input("di mana tikus berada? pilih 1-4  "))

        if pilihan_user == cuypay_posisi:
            print(f"selamat anda menang🏆\n{goa}")
        else:
            print(f"coba lagi..(T_T), cuypay ada di baris {cuypay_posisi}\n{goa}")
        play_again = input("apakah ingin mengulangi gamenya? [y/n]")
        if play_again == "n":
            main.menu()
            break
if __name__ == '__main__':
    start()