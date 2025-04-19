"""
Zadanie 6
Rozwiązać równanie struny:
𝜕^2 * 𝑦(𝑥,𝑡)/𝜕𝑡^2 = 𝑐^2*(𝜕^2 * 𝑦(𝑥,𝑡)/𝜕𝑥^2)
Gdzie 𝑦(𝑥,𝑡) 𝑜𝑘𝑟𝑒ś𝑙𝑎 𝑘𝑠𝑧𝑡𝑎ł𝑡 𝑠𝑡𝑟𝑢𝑛𝑦 𝑤 𝑐ℎ𝑤𝑖𝑙𝑖 𝑡
Na potrzeby rozwiązania przyjmujemy c=1 (c prędkość propagacji fali)
Prawą stronę
𝜕^2 * 𝑦(𝑥,𝑡)/𝜕𝑥^2
Przybliżamy:
𝜕^2𝑦(𝑥,𝑡) / 𝜕𝑥^2 = 𝑦(𝑥𝑖−1,𝑡) − 2 ∗ 𝑦(𝑥𝑖,𝑡) + 𝑦(𝑥𝑖+1,𝑡)/∆𝑥^2 = 𝑎(𝑥𝑖,𝑡)
L – długość struny (π)
N – na ile części dzielimy (np=10)
∆𝑥 =𝐿/𝑁
Dla każdego punktu struny rozwiązujemy równanie ruchu metodą MidPoint:
{
𝑑𝑦/𝑑𝑡 = 𝑣
𝑑𝑣/𝑑𝑡 = 𝑎
}
Struna jest zamocowana na końcach.
Wyznaczyć energię potencjalną, kinetyczną oraz całkowitą struny:
Ek,Ep suma energii poszczególnych punktów
𝐸𝑘 = ∑(𝑑𝑥 ∗ 𝑉^2(𝑥𝑖)/2)
𝐸𝑝 = ∑((𝑦(𝑥𝑖+1) − 𝑦(𝑥𝑖))^2/2∆𝑥)
Przedstawić Ep, Ek, Ec na wykresie
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametry struny
L = np.pi
c = 1
N = 100
dx = L / N
dt = 0.001  # krok czasowy
T = 5       # czas symulacji
steps = int(T / dt)

# Inicjalizacja siatki
x = np.linspace(0, L, N+1)
y = np.sin(x)      # początkowe wychylenie
v = np.zeros(N+1)  # początkowa prędkość


Ek_list = []
Ep_list = []
Etot_list = []
t_list = []

def acceleration(y):
    a = np.zeros_like(y)
    for i in range(1, N):
        a[i] = c**2 * (y[i-1] - 2*y[i] + y[i+1]) / dx**2
    return a

def midpoint_step(y, v, dt):
    a1 = acceleration(y)
    y_mid = y + 0.5 * dt * v
    v_mid = v + 0.5 * dt * a1
    a2 = acceleration(y_mid)
    y_new = y + dt * v_mid
    v_new = v + dt * a2
    # Warunki brzegowe (końce struny są zamocowane)
    y_new[0] = 0
    y_new[-1] = 0
    return y_new, v_new

for step in range(steps):
    y, v = midpoint_step(y, v, dt)

    # Energia kinetyczna
    Ek = 0.5 * np.sum(v**2) * dx

    # Energia potencjalna
    dy = y[1:] - y[:-1]
    Ep = 0.5 * np.sum((dy / dx)**2) * dx

    # Energia całkowita
    Etot = Ek + Ep

    # Zapis do list
    t_list.append(step * dt)
    Ek_list.append(Ek)
    Ep_list.append(Ep)
    Etot_list.append(Etot)

# Wykres energii
plt.figure(figsize=(10,5))
plt.plot(t_list, Ek_list, label='Energia kinetyczna')
plt.plot(t_list, Ep_list, label='Energia potencjalna')
plt.plot(t_list, Etot_list, label='Energia całkowita', linestyle='--')
plt.xlabel('Czas [s]')
plt.ylabel('Energia')
plt.legend()
plt.title('Energie struny w czasie')
plt.grid(True)
plt.tight_layout()
plt.show()
