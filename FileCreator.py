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

def writeText(user_text):
    print("")
    input("Has pulsado la opción 1...\nEscribe el contenido del texto(escribe '<>' para finalizar)\n")
    for console_line in sys.stdin:
        if console_line == '<>\n':
            break
        for text_line in console_line.split():
            user_text += text_line
    return user_text

def saveNewTxtFile(user_text):
    print("")
    file_name =input("Has pulsado la opción 2...\nEscribe el nombre del archivo\n")
    file = open(f'{file_name}.txt', "w")
    file.write(user_text + os.linesep)
    file.close()
    return file_name

def openLastFileUsed(file_name):
    print("")
    input(f"Se abrira el archivo {file_name}.txt\npulsa una tecla para continuar")
    os.system(f"start {file_name}.txt")

def main(file_name=''):
    user_text = ''
    while True:
        menu()
        menu_selection = input("inserta un numero valor (1-9)")
        if menu_selection == "1":
            user_text = writeText(user_text)
        elif menu_selection == "2":
            file_name = saveNewTxtFile(user_text)
        elif menu_selection == "3":
            openLastFileUsed(file_name)
        elif menu_selection == "9":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


if __name__ == "__main__":
    main()