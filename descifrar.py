# Recibir el mensaje cifrado completo
mensaje_cifrado_completo = input("Dame el mensaje cifrado completo: ")

# Extraer k del final
letra_k = mensaje_cifrado_completo[-1]

# Convertir la letra a k (número)
k = ord(letra_k) - ord('A') + 1

# Extraer el mensaje cifrado sin k
cifrado = mensaje_cifrado_completo[:-1]
tamanio = len(cifrado)

descifrado = ""

for i in range(0, tamanio):
    if cifrado[i].isalpha():
        cambio = ord(cifrado[i]) - k
        if cifrado[i].islower() and cambio < ord('a'):  # Minúsculas
            cambio += 26
        elif cifrado[i].isupper() and cambio < ord('A'):  # Mayúsculas
            cambio += 26
        descifrado += chr(cambio)
    else:
        descifrado += cifrado[i]  # No descifrar caracteres que no son letras

print("El desplazamiento fue de:", k)
print("Mensaje descifrado:", descifrado)
