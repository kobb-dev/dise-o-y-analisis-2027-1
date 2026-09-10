def busqBinaria(datos, buscados):
    noEncontrado = True
    inicio = 0
    fin = len(datos) - 1

    while inicio <= fin:
        numMedio = (inicio + fin) // 2

        if buscados == datos[numMedio]:
            print(f"El num {buscados} se encopntro en el {numMedio} :D")
            noEncontrado = False
            break
        elif buscados > numMedio:
            inicio = numMedio +1

        else:
            fin = numMedio +1
    if noEncontrado:
        print("No existe :d")

lim = 10
info = [x*5 for x in range(1,lim+1)]
busqBinaria(info, lim*5)

lim = 100
info = [x*5 for x in range(1,lim+1)]
busqBinaria(info, lim*5)

lim = 1000
info = [x*5 for x in range(1,lim+1)]
busqBinaria(info, lim*5)

lim = 10000
info = [x*5 for x in range(1,lim+1)]
busqBinaria(info, lim*5)

lim = 100000
info = [x*5 for x in range(1,lim+1)]
busqBinaria(info, lim*5)

lim = 1000000
info = [x*5 for x in range(1,lim+1)]
busqBinaria(info, lim*5)