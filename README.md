[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eZ_U6wFI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18658412)
# Práctica 2. Estructura de control iterativa
Autora: Jimena Garcia
# Cifrar.py

Este programa utiliza el el cifrado César una técnica de cifrado que desplaza cada letra del mensaje original un número fijo de posiciones en el alfabeto. En este caso, el desplazamiento "k" se genera aleatoriamente entre 3-15 y este se incluye en el mensaje cifrado de manera oculta al final.

El programa genera un número aleatorio k entre 3 y 15, que representa el número de posiciones que se desplazarán las letras del mensaje.
El mensaje ingresado por el usuario se cifra desplazando cada letra k posiciones en el alfabeto.
  - Si el desplazamiento hace que una letra salga del rango del alfabeto (por ejemplo, "x" con un desplazamiento de 3), el alfabeto se "reinicia".     Esto significa que después de "z" se vuelve a "a"
  - Los caracteres que no son letras (como espacios, números o signos de puntuación) no se cifran.
El valor de k se convierte en una letra del alfabeto (por ejemplo, k = 3 → C).
    - 3 -> C
    - 4 -> D
    - 5 -> E
    - 6 -> F
    - 7 -> G
    - 8 -> H
    - 9 -> I
    - 10 -> J
    - 11 -> K
    - 12 -> L
    - 13 -> M
    - 14 -> N
    - 15 -> O

Esta letra se agrega al final del mensaje cifrado, de modo que el receptor pueda extraerla y usarla para descifrar el mensaje.

## Implementacion en Phyton

La implementación del algoritmo en Python se realizó de la siguiente manera:

1. **Generación del desplazamiento k**:
   - Se utiliza la función `random.randint(3, 15)` para generar k.

2. **Cifrado del mensaje**:
   - Se utiliza un bucle `for` para recorrer cada carácter del mensaje.
   - Se verifica si el carácter es una letra usando `isalpha()`.
   - Se manejan mayúsculas y minúsculas por separado para evitar errores en el cifrado.
   - Si el carácter no es una letra, se añade al mensaje cifrado sin modificarlo.

3. **Inclusión del desplazamiento k**:
   - Se convierte \( k \) en una letra del alfabeto usando la fórmula `chr(ord('A') + k - 1)`.
   - Esta letra se concatena al final del mensaje cifrado.

4. **Manejo de casos especiales**:
   - Si el desplazamiento hace que una letra salga del rango del alfabeto (por ejemplo, `z` + 3), se ajusta el valor para que "vuelva" al inicio del alfabeto.

# Descifrar.py

Este programa descifra un mensaje cifrado con el cifrado César, utilizando un desplazamiento k que está oculto en el propio mensaje cifrado. El valor de k se codifica como una letra al final del mensaje cifrado, y el programa lo extrae para descifrar el mensaje original.
El programa recibe el mensaje cifrado completo, que incluye el mensaje cifrado y una letra al final que representa el desplazamiento k.
   - La última letra del mensaje cifrado se extrae y se convierte en k usando la fórmula:
     
    k = ord(letra_k) - ord('A') + 1
  
El mensaje cifrado (sin la última letra) se descifra restando k a cada letra.
  - Si el descifrado hace que una letra salga del rango del alfabeto, el alfabeto se "reinicia" sumando 26 para volver al final del alfabeto.
El valor de k se codifica como una letra del alfabeto, donde:
  - A → 1
  - B → 2
  - C → 3
  - ...
  - Z → 26
Por ejemplo:
- Si la última letra es "C", entonces k = 3.

## Implementacion en Phyton

La implementación del algoritmo en Python se realizó de la siguiente manera:

1. **Extracción de k**:
   - Se utiliza la última letra del mensaje cifrado (`mensaje_cifrado_completo[-1]`) para obtener k.
   - Se convierte la letra en k usando la fórmula:  
     ```python
     k = ord(letra_k) - ord('A') + 1
     ```

2. **Descifrado del mensaje**:
   - Se utiliza un bucle `for` para recorrer cada carácter del mensaje cifrado (sin la última letra).
   - Se verifica si el carácter es una letra usando `isalpha()`.
   - Si el carácter es una letra, se resta \( k \) a su valor ASCII.
   - Si el resultado es menor que `a` (para minúsculas) o `A` (para mayúsculas), se suma 26 para reiniciar el alfabeto.
   - Si el carácter no es una letra, se añade al mensaje descifrado sin modificarlo.

3. **Manejo de casos especiales**:
   - Si el descifrado hace que una letra salga del rango del alfabeto (por ejemplo, `a` - 3), se ajusta el valor sumando 26 para que "vuelva" al final del alfabeto.
