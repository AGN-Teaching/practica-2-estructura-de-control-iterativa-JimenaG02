import random

#k = random.randint(3,15)
k=3
mensaje = str(input("Dame el mensaje a cifrar: "))

tamanio= len(mensaje)

cifrado =""


print("El desplazamiento fue de :",k)


for i in  range (0, tamanio):

    cambio = ord(chr(ord(mensaje[i])+k))
    if  cambio > ord("z"):
        cambio -= 26
        cifrado +=chr(cambio)

    else:
        cifrado += chr(ord(mensaje[i] ) + k )

print(str(cifrado))



