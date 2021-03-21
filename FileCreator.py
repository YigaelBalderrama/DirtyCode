import os
import sys

#-----DIEGOS REFACTORING-----#

def menu():
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 - Escribir contenido")
    print("\t2 - Guardar y Nombrar archivo ")
    print("\t3 - Abrir Ultimo Archivo")
    print("\t9 - Salir")


def main(n=''):
    user_text = ''
    while True:
        menu()
        menu_selection = input("inserta un numero valor (1-9)")
        if menu_selection == "1":
            print("")
            input("Has pulsado la opción 1...\nEscribe el contenido del texto(escribe '<>' para finalizar)")
            for console_line in sys.stdin:
                if console_line == '<>\n':
                    break
                for var in console_line.split():
                    user_text += var
        elif menu_selection == "2":
            print("")
            n =input("Has pulsado la opción 2...\nEscribe el nombre del archivo\n")
            file = open(f'{n}.txt', "w")
            file.write(user_text + os.linesep)
            file.close()
        elif menu_selection == "3":
            print("")
            input(f"Se abrira el archivo {n}.txt\npulsa una tecla para continuar")
            os.system(f"start {n}.txt")
        elif menu_selection == "9":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


if __name__ == "__main__":
    main()