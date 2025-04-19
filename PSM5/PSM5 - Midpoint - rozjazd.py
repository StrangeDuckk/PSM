import numpy as np
import matplotlib.pyplot as plt

def Midpoint(Rzs, Ms, Mz, Mk, Time_symulacji, deltaT, Rzk):
    N = len(Time_symulacji)

    # Inicjalizacja pozycji i prędkości
    x_Z = np.zeros(N)
    y_Z = np.zeros(N)
    vx_Z = np.zeros(N)
    vy_Z = np.zeros(N)

    x_K = np.zeros(N)
    y_K = np.zeros(N)
    vx_K = np.zeros(N)
    vy_K = np.zeros(N)

    # Początkowe pozycje i prędkości (Ziemia na orbicie kołowej)
    x_Z[0] = Rzs
    y_Z[0] = 0
    vy_Z[0] = np.sqrt(G * Ms / Rzs)  # prędkość orbitalna

    x_K[0] = x_Z[0] + Rzk
    y_K[0] = 0
    vy_K[0] = vy_Z[0] + np.sqrt(G * Mz / Rzk)  # prędkość Księżyca wokół Ziemi + ruch Ziemi

    for i in range(N-1):
        # Siła grawitacyjna Słońce-Ziemia
        dx_z = -x_Z[i]
        dy_z = -y_Z[i]
        r_z = np.sqrt(dx_z**2 + dy_z**2)
        Fz = G * Ms * Mz / r_z**2
        ax_z = Fz * dx_z / (r_z * Mz)
        ay_z = Fz * dy_z / (r_z * Mz)

        # Siła grawitacyjna Słońce-Księżyc
        dx_k = -x_K[i]
        dy_k = -y_K[i]
        r_k = np.sqrt(dx_k**2 + dy_k**2)
        Fk = G * Ms * Mk / r_k**2
        ax_k = Fk * dx_k / (r_k * Mk)
        ay_k = Fk * dy_k / (r_k * Mk)

        # oddzialywanie Ziemia-Księżyc
        dx_ziemia_ks = x_K[i] - x_Z[i]
        dy_ziemia_ks = y_K[i] - y_Z[i]
        r_ziemia_ks = np.sqrt(dx_ziemia_ks**2 + dy_ziemia_ks**2)
        Fz_ks = G * Mz * Mk / r_ziemia_ks**2
        ax_ks = Fz_ks * dx_ziemia_ks / (r_ziemia_ks * Mk)
        ay_ks = Fz_ks * dy_ziemia_ks / (r_ziemia_ks * Mk)

        # -------------------(midpoint) ------------------
        vx_Z_half = vx_Z[i] + (ax_z + ax_ks) * deltaT / 2
        vy_Z_half = vy_Z[i] + (ay_z + ay_ks) * deltaT / 2
        vx_K_half = vx_K[i] + (ax_k - ax_ks) * deltaT / 2
        vy_K_half = vy_K[i] + (ay_k - ay_ks) * deltaT / 2

        # Obliczamy nowe pozycje na podstawie prędkości w połowie kroku
        x_Z[i+1] = x_Z[i] + vx_Z_half * deltaT
        y_Z[i+1] = y_Z[i] + vy_Z_half * deltaT
        x_K[i+1] = x_K[i] + vx_K_half * deltaT
        y_K[i+1] = y_K[i] + vy_K_half * deltaT

        # Obliczamy nowe siły na podstawie nowych pozycji
        dx_z = -x_Z[i+1]
        dy_z = -y_Z[i+1]
        r_z = np.sqrt(dx_z**2 + dy_z**2)
        Fz = G * Ms * Mz / r_z**2
        ax_z = Fz * dx_z / (r_z * Mz)
        ay_z = Fz * dy_z / (r_z * Mz)

        dx_k = -x_K[i+1]
        dy_k = -y_K[i+1]
        r_k = np.sqrt(dx_k**2 + dy_k**2)
        Fk = G * Ms * Mk / r_k**2
        ax_k = Fk * dx_k / (r_k * Mk)
        ay_k = Fk * dy_k / (r_k * Mk)

        dx_ziemia_ks = x_K[i+1] - x_Z[i+1]
        dy_ziemia_ks = y_K[i+1] - y_Z[i+1]
        r_ziemia_ks = np.sqrt(dx_ziemia_ks**2 + dy_ziemia_ks**2)
        Fz_ks = G * Mz * Mk / r_ziemia_ks**2
        ax_ks = Fz_ks * dx_ziemia_ks / (r_ziemia_ks * Mk)
        ay_ks = Fz_ks * dy_ziemia_ks / (r_ziemia_ks * Mk)

        # ------------ full point ------------------
        vx_Z[i+1] = vx_Z[i] + ax_z * deltaT
        vy_Z[i+1] = vy_Z[i] + ay_z * deltaT
        vx_K[i+1] = vx_K[i] + ax_k * deltaT
        vy_K[i+1] = vy_K[i] + ay_k * deltaT

    wykres(x_Z, y_Z, x_K, y_K)

def wykres(x_Ziemii, y_Ziemii, x_Ksiezyca, y_Ksiezyca):
    plt.figure(figsize=(8,8))
    plt.scatter(0, 0, label='Słońce', color='orange')
    plt.plot(x_Ziemii, y_Ziemii, label='Ziemia', color='green')
    plt.plot(x_Ksiezyca, y_Ksiezyca, label='Księżyc', color='gray')
    plt.title("(Midpoint)")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.show()

# Stałe
skalaOrbityKsiezyca = 10000
deltaT = 1000  # krok czasowy
iloscKrokow = 100000
G = 6.6743e-11
Ms = 1.989e30
Mz = 5.972e24
Mk = 7.347e22
Rzs = 1.5e11
Rzk = 384400 * skalaOrbityKsiezyca

Time_symulacji = np.linspace(0, deltaT * iloscKrokow, iloscKrokow)

Midpoint(Rzs, Ms, Mz, Mk, Time_symulacji, deltaT, Rzk)
