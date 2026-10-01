def zn(obj):
    return '+' if obj >= 0 else '-'


def opr(obj):
    return int(obj) if int(obj) == obj else obj


lst = []
for i in range(3):
    eql = list(map(float, input('Input coordinates: ').split()))
    lst.append([eql[0]**2, eql[0], 1, eql[1]])

for z in range(3):
    p = max(range(z, 3), key=lambda r: abs(lst[r][z]))
    if lst[p][z] == 0:
        raise ValueError('Points must have different x values')
    lst[z], lst[p] = lst[p], lst[z]
    for i in range(z + 1, 3):
        k = lst[i][z] / lst[z][z]
        for j in range(z, 4):
            lst[i][j] -= lst[z][j] * k

c = lst[-1][-1] / lst[-1][-2]
b = (lst[-2][-1] - c * lst[-2][-2]) / lst[-2][-3]
a = (lst[0][3] - b * lst[0][1] - c * lst[0][2]) / lst[0][0]

print(f'Equation of Parabola: y = {opr(a)}x**2 {zn(b)} {abs(opr(b))}x {zn(c)} {abs(opr(c))}')

l, r = sorted((float(input('Left bound: ')), float(input('Right bound: '))))
Area1 = (a * l**3/3 + b * l**2 / 2 + l*c) - (a * r**3/3 + b * r**2 / 2 + r * c)
osn1 = a * r**2 + b * r + c
osn2 = a * l**2 + b * l + c
h = r - l
Area2 = 0.5 * (osn1 + osn2) * h
print('The area through the integral:', abs(Area2 - Area1))

l, r = int(l * 10000), int(r * 10000)
area1 = 0
for i in range(l, r):
    i = i / 10000
    j = i + 0.0001
    osn1 = a * j ** 2 + b * j + c
    osn2 = a * i ** 2 + b * i + c
    area1 += 0.5 * (osn1 + osn2) * (j - i)

print('The area through cycle', abs(Area2 - area1))
