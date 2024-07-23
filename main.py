from libs import welcome, exit_program
from games import cuypay
from tools import warung

def main():
    welcome()
    menu()
    
def menu():
    user_option = int(input(f'silahkan pilih menu\n1. Games cuypay\n2. Warung mini\n3. Exit program\n\nsilahkan pilih: '))
    
    if user_option == 1:
        cuypay.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print("hanya boleh yang di sediakan di menu! ")
 

if __name__ == '__main__':
    main()

