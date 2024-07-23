import socket
from time import sleep

PC_NAME = socket.gethostname()

def welcome():
    print(f"selamat datang {PC_NAME}")
    
def exit_program():
    print("program akan di hentikan")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("goodby world")
       
    
if __name__ == '__main__':
    welcome()
    exit_program()