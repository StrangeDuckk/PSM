import numpy as np
import matplotlib.pyplot as plt

def midpoint_simulacja(dt=1000, steps=50000):
    # Stałe fizyczne
    G = 6.6743e-11
    Ms = 1.989e30
    Mz = 5.972e24
    Mk = 7.347e22
    Rzs = 1.5e11
    Rzk = 384400e3

    # Początkowe pozycje
    r_s = np.array([0.0, 0.0])
    r_z = np.array([Rzs, 0.0])
    r_k = r_z + np.array([Rzk, 0.0])

    # Początkowe prędkości
    v_z = np.array([0.0, np.sqrt(G * Ms / Rzs)])
    # Wektor od Ziemi do Księżyca
    r_rel = r_k - r_z
    r_rel_unit = r_rel / np.linalg.norm(r_rel)

    # Prędkość orbitalna Księżyca wokół Ziemi (prostopadła do r_rel)
    v_orb_magnitude = np.sqrt(G * Mz / np.linalg.norm(r_rel))
    v_perp = np.array([-r_rel_unit[1], r_rel_unit[0]])  # wektor prostopadły

    # Prędkość Księżyca to prędkość Ziemi + orbitalna względem niej
    v_k = v_z + v_perp * v_orb_magnitude
    v_s = -(v_z * Mz + v_k * Mk) / Ms  # Środek masy układu nieruchomy

    # Tablice pozycji do rysowania
    pos_s, pos_z, pos_k = [], [], []

    for i in range(steps):
        def F(m1, m2, r1, r2):
            r = r2 - r1
            d = np.linalg.norm(r)
            return G * m1 * m2 * r / d**3

        # Przyspieszenia
        a_s = (F(Ms, Mz, r_s, r_z) + F(Ms, Mk, r_s, r_k)) / Ms
        a_z = (-F(Ms, Mz, r_s, r_z) + F(Mz, Mk, r_z, r_k)) / Mz
        a_k = (-F(Ms, Mk, r_s, r_k) - F(Mz, Mk, r_z, r_k)) / Mk

        # Midpoint krok - prędkości w połowie kroku
        v_s_half = v_s + a_s * dt / 2
        v_z_half = v_z + a_z * dt / 2
        v_k_half = v_k + a_k * dt / 2

        # Midpoint krok - pozycje w połowie kroku
        r_s_half = r_s + v_s * dt / 2
        r_z_half = r_z + v_z * dt / 2
        r_k_half = r_k + v_k * dt / 2

        # Przyspieszenia w połowie kroku
        a_s_half = (F(Ms, Mz, r_s_half, r_z_half) + F(Ms, Mk, r_s_half, r_k_half)) / Ms
        a_z_half = (-F(Ms, Mz, r_s_half, r_z_half) + F(Mz, Mk, r_z_half, r_k_half)) / Mz
        a_k_half = (-F(Ms, Mk, r_s_half, r_k_half) - F(Mz, Mk, r_z_half, r_k_half)) / Mk

        # Aktualizacja prędkości i pozycji
        v_s += a_s_half * dt
        v_z += a_z_half * dt
        v_k += a_k_half * dt
        r_s += v_s_half * dt
        r_z += v_z_half * dt
        r_k += v_k_half * dt

        pos_s.append(r_s.copy())
        pos_z.append(r_z.copy())
        pos_k.append(r_k.copy())

    return np.array(pos_s), np.array(pos_z), np.array(pos_k)

def rysuj_trajektorie(pos_s, pos_z, pos_k):
    plt.figure(figsize=(10, 10))
    plt.plot(pos_s[:, 0], pos_s[:, 1], label="Słońce", color="orange")
    plt.plot(pos_z[:, 0], pos_z[:, 1], label="Ziemia", color="green")
    plt.plot(pos_k[:, 0], pos_k[:, 1], label="Księżyc", color="gray")
    plt.scatter(pos_s[0, 0], pos_s[0, 1], color='orange', marker='o', s=50)
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("Midpoint – trajektorie Słońca, Ziemi i Księżyca")
    plt.axis("equal")
    plt.grid(True)
    plt.legend()
    plt.show()

pos_s, pos_z, pos_k = midpoint_simulacja(dt=1000, steps=50000)
rysuj_trajektorie(pos_s, pos_z, pos_k)
