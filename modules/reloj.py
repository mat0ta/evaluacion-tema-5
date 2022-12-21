import time
import os

def reloj():
    hora = time.strftime("%H:%M:%S")
    return hora

def main():
    while True:
        print(reloj())
        time.sleep(1)
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")

if __name__ == "__main__":
    main()