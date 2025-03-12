# Plantilla descifrar.py

mensaje = str(input("Dame el mensaje cifrado: "))
k=int(input("¿Cual fue el desplazamiento?: "))

tamanio= len(mensaje)

descifrado =""


for i in  range (0, tamanio):

    descifrado += chr(ord(mensaje[i] ) - k )

print(str(descifrado))
