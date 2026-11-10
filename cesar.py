alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def descifrar(mensaje, desplazamiento):
    resultado = ""

    for letra in mensaje:
        minuscula = letra.lower()

        if minuscula in alfabeto:
            posicion = alfabeto.index(minuscula)
            nueva_posicion = (posicion - desplazamiento) % 27

            nueva_letra = alfabeto[nueva_posicion]

            if letra.isupper():
                nueva_letra = nueva_letra.upper()

            resultado += nueva_letra
        else:
            resultado += letra

    return resultado

mensaje = input("\nEscribe el mensaje:\n")

for desplazamiento in range(27):
    print("Desplazamiento:", desplazamiento)
    print(descifrar(mensaje, desplazamiento))
