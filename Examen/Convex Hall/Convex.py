def area(a, b, c):
    return abs(
        a[0] * (b[1] - c[1]) +
        b[0] * (c[1] - a[1]) +
        c[0] * (a[1] - b[1])
    ) / 2
def producto(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - \
        (a[1] - o[1]) * (b[0] - o[0])

puntos = []
with open("campo.in") as archivo:
    for linea in archivo:
        x, y = map(int, linea.split())
        if x == -1 and y == -1:
            break
        puntos.append((x, y))
puntos.sort()

inferior = []
for p in puntos:
    while len(inferior) >= 2 and \
            producto(
                inferior[-2],
                inferior[-1],
                p
            ) <= 0:
        inferior.pop()
    inferior.append(p)

superior = []
for p in reversed(puntos):
    while len(superior) >= 2 and \
            producto(
                superior[-2],
                superior[-1],
                p
            ) <= 0:
        superior.pop()
    superior.append(p)

hull = inferior[:-1] + superior[:-1]
h = len(hull)
mejor_area = 0
mejor_triangulo = None
for i in range(h):
    for j in range(i + 1, h):
        for k in range(j + 1, h):
            area_actual = area(
                hull[i],
                hull[j],
                hull[k]
            )
            if area_actual > mejor_area:
                mejor_area = area_actual
                mejor_triangulo = (
                    hull[i],
                    hull[j],
                    hull[k]
                )

with open("campo.out", "w") as salida:
    for punto in mejor_triangulo:
        salida.write(
            f"{punto[0]} {punto[1]}\n"
        )