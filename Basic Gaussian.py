def opr(obj):
    return int(obj) if int(obj) == obj else obj


lst = []
sp = int(input('Enter the number of equations: '))
for i in range(sp):
    eqt = list(map(float, input(f'Enter coefficients of {i + 1} equation: ').split()))
    lst.append(eqt)

for z in range(sp):
    for i in range(z + 1, sp):
        k = lst[i][z] / lst[z][z]
        for j in range(z, sp + 1):
            lst[i][j] -= lst[z][j] * k

ans = [0] * sp
for i in range(sp - 1, -1, -1):
    ans[i] = lst[i][sp]
    for j in range(i + 1, sp):
        ans[i] -= lst[i][j] * ans[j]
    ans[i] /= lst[i][i]

print("The solution is:")
print([opr(i) for i in ans])
