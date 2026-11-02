def area(a, b, c):
    return abs(
        a[0] * (b[1] - c[1]) +
        b[0] * (c[1] - a[1]) +
        c[0] * (a[1] - b[1])
    ) / 2
puntos = []
archivo = open("campo.in")
for linea in archivo:
    x, y = map(int, linea.split())
    if x == -1 and y == -1:
        break
    puntos.append((x, y))

n = len(puntos)
mejor_area = 0
mejor_triangulo = None

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area_actual = area(
                puntos[i],
                puntos[j],
                puntos[k]
            )
            if area_actual > mejor_area:
                mejor_area = area_actual
                mejor_triangulo = (
                    puntos[i],
                    puntos[j],
                    puntos[k]
                )
salida = open("campo.out", "w")
for punto in mejor_triangulo:
    salida.write(f"{punto[0]} {punto[1]}\n")