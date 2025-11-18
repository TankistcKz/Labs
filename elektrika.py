import numpy as np

def I(U, E, R):
    return (U + E) / R


Rn = [1.2, 1, 1.5, 4.2]
n = len(Rn)
En = [48, 45, 45, 0]
Ke = [1, 1, 1, 1]
Jn = [0, 0, 0, 0]
Kj = [1, 1, 1, 1]

i = 0
Gn = [0] * n
EGn = [0] * n
JnKj = [0] * n

for x in Rn:
    Gn[i] = 1/x
    EGn[i] = Ke[i] * En[i] * Gn[i]
    JnKj[i] = Kj[i] * Jn[i]
    i = i + 1


U12 = (sum(EGn) - sum(JnKj)) / sum(Gn)
Ku = [-1, -1, -1, 1]

i = 0
Un = [0] * n
In = [0] * n

for y in Ku:
    Un[i] = y * U12
    In[i] = I(Un[i], En[i], Rn[i])
    i = i + 1


print(f"\nRn = {Rn} Ом")
print(f"\nEn = {En} В")
print(f"\nJn = {Jn} А")
print(f"\nGn = {[round(g, 15) for g in Gn]} См")
print(f"\nU12 = {round(U12, 1)} В")
print(f"\nUn = {[round(u, 1) for u in Un]} В")
print(f"\nIn = {[round(i_val, 1) for i_val in In]} А")


print("Проверка по 1-му закону Кирхгофа:")

sum_currents = sum(In)
print(f"Сумма токов в узле: {round(sum_currents, 10)} А")
if abs(sum_currents) < 1e-6:
    print("✓ Баланс токов сходится")
else:
    print("✗ Ошибка в расчетах")


print("Мощности:")

P_resistors = []
for i in range(n):
    P = In[i]**2 * Rn[i]
    P_resistors.append(P)
    print(f"P_R{i+1} = {round(P, 2)} Вт")

print(f"\nСумма мощностей на резисторах: {round(sum(P_resistors), 2)} Вт")

P_sources = []
for i in range(n):
    if En[i] != 0:
        P = En[i] * In[i]
        P_sources.append(P)
        print(f"P_E{i+1} = {round(P, 2)} Вт")

print(f"Сумма мощностей источников: {round(sum(P_sources), 2)} Вт")