import random

# Generar un número aleatorio entre 3 y 15 para el desplazamiento
k = random.randint(3,15)

mensaje = str(input("Dame el mensaje a cifrar: "))

tamanio= len(mensaje)

cifrado =""


for i in  range (0, tamanio):
    if mensaje[i].isalpha():
        cambio = ord(mensaje[i]) + k
        if mensaje[i].islower() and cambio > ord('z'):  # Minúsculas
            cambio -= 26
        elif mensaje[i].isupper() and cambio > ord('Z'):  #Mayúsculas
            cambio -= 26
        cifrado += chr(cambio)
    else:
        cifrado += mensaje[i]  # No cifrar caracteres que no son letras

# Convertir k en una letra del alfabeto (A=1, B=2, ...)
letra_k = chr(ord('A') + k - 1)
mensaje_cifrado = cifrado+letra_k

print("El desplazamiento fue de :",k)

print("Mensaje cifrado con el desplazamiento:", mensaje_cifrado)
