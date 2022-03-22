# Encriptado de archivos de texto

def encriptar(texto):
    print('El texto a encriprtar es: ' + texto)
    textoFinal = ''
    # recorre cada letra del texto
    for letra in texto:
        # obtiene el codigo ascii de cada letra
        ascii = ord(letra)
        # suma 2 a cada codigo ascii
        ascii += 2
        # reemplazo el texto por el codigo ascii + 2 de cada letra
        textoFinal += chr(ascii)
    return textoFinal

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)
    archivo = open(rutaArchivo, 'w') 
    archivo.write(textoEncriptado)
    archivo.close()

    print('El archivo se encripto correctamente')

# Desencriptado de archivo

def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinal = ''   
    
    for letra in texto:
        ascii = ord(letra)
        ascii -= 2
        textoFinal += chr(ascii)
    return textoFinal

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)
    archivo = open(rutaArchivo, 'w') 
    archivo.write(textoDesencriptado)
    archivo.close()
    print('El archivo se desencripto correctamente')

# Implementacion

respuesta = input('Presione "E" para encriptar , o "D" para desencriptar, o "salir" para salir >> ')

index = 1
while index == 1:
    if respuesta == 'e' or respuesta == 'E':
        rutaArchivo = input('Ingrese la ruta del archivo >> ')
        encriptarArchivo(rutaArchivo) 
        respuesta = input('Presione "E" para encriptar , o "D" para desencriptar, o "salir" para salir >> ')
    elif respuesta == 'd' or respuesta == 'D':
        rutaArchivo = input('Ingrese la ruta del archivo >> ')
        desencriptarArchivo(rutaArchivo)    
        respuesta = input('Presione "E" para encriptar , o "D" para desencriptar, o "salir" para salir >> ')
    elif respuesta == 'salir':
        print('Hasta pronto!!')
        index = 0
    elif respuesta != 'd' or respuesta != 'D' or respuesta != 'e' or respuesta != 'E' or respuesta != 'salir':
        print('Ingrese un valor correcto')
        respuesta = input('Presione "E" para encriptar , o "D" para desencriptar, o "exit" para salir >> ')  
    

# Ruta de prueba
#  F:/Cristian/prueba.txt

