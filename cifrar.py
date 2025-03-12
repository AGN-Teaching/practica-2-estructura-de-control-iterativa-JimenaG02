# Plantilla cifrar.py
# Plantilla cifrar.py
import random

k = random.randint(3,15)

mensaje = str(input("Dame el mensaje a cifrar: "))

tamanio= len(mensaje)

cifrado =""

print("El desplazamiento fue de :",k)

for i in  range (0, tamanio):

    cifrado += chr(ord(mensaje[i] ) + k )

print(str(cifrado))

