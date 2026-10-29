def hash(numeros, objetivo):
    vistos = {}
    for i, num in enumerate(numeros):
        complemento = objetivo - num
        if complemento in vistos:
            return [vistos[complemento], i]
        vistos[num] = i
    return None


arreglo = [2, 14, 6, 11, 8, 15, 7]
total = 9

resultado = hash(arreglo, total)
print(resultado)