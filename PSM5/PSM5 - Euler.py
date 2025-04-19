import numpy as np
import matplotlib.pyplot as plt  # Biblioteka do rysowania wykresów

def Euler(Rzs,Ms,Mz,Time_symulacji,Time_rok,Time_ksiezycowyRok,Rzk):
    #pozycjonowanie slonca i ziemi
    R_ziemia_slonce = Rzs * Ms / (Ms+Mz)

    theta_z = 2*np.pi * Time_symulacji/Time_rok
    x_Ziemii = Rzs * np.cos(theta_z)
    y_Ziemii = Rzs * np.sin(theta_z)

    #pozycjonowanie ksiezyca wzgledem Ziemii
    theta_k = 2*np.pi * Time_symulacji/Time_ksiezycowyRok
    x_Ksiezyca = x_Ziemii + Rzk * np.cos(theta_k)
    y_Ksiezyca = y_Ziemii + Rzk * np.sin(theta_k)

    wykres(x_Ziemii, y_Ziemii, x_Ksiezyca, y_Ksiezyca)


def wykres(x_Ziemii, y_Ziemii, x_Ksiezyca, y_Ksiezyca):
    # ------------------ rysowanie -----------------
    plt.figure(figsize=(8,8))
    plt.scatter(0, 0, label='Słońce', color='orange')
    plt.plot(x_Ziemii, y_Ziemii, label='Ziemia', color='green')
    plt.plot(x_Ksiezyca, y_Ksiezyca, label='Księżyc', color='gray')
    plt.title("Trajektorie Słońca, Ziemi i Księżyca względem środka masy")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.show()


skalaOrbityKsiezyca = 33
deltaT = 1
iloscKrokow = 300000
G = 6.6743e-11  # stała grawitacyjna
Ms = 1.989e30  # masa Słońca
Mz = 5.972e24  # masa Ziemi
Mk = 7.347e22  # masa Księżyca
Rzs = 1.5e8  # m - odległość Ziemia-Słońce
Rzk = 384400 * skalaOrbityKsiezyca  # m - odległość Ziemia-Księżyc

# czas
Time_rok = 365 * 24 * 60 * 60  # czas w sekundach
Time_ksiezycowyRok = 28 * 24 * 3600  # czas w sekundach, ksiezyc do pelnego obrotu potrzebuje 28 dni

Time_symulacji = np.linspace(0, Time_rok, iloscKrokow)

Euler(Rzs, Ms, Mz, Time_symulacji, Time_rok, Time_ksiezycowyRok, Rzk)
