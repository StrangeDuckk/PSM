"""
Zadanie 3

Zrealizować symulację ruchu wahadła matematycznego rozwiązując równania ruchu wahadła
metodą Eulera, ulepszoną metodą Eulera (midpoint) oraz metodą RK4 (Runge Kutta)


Sporządzić wykres energii potencjalnej, kinetycznej oraz całkowitej.

Porównać otrzymane wyniki obliczone metodą Eulera z wynikami otrzymanymi po
zastosowaniu ulepszonej metody Eulera oraz metody RK4

wzory:
alfa'=w,
w'=E

E=g/l * sin(alfa0)

Euler:
alfa(t0+dt)=alfa(t0)+ omega(t0)*deltaT
omega(t0)=w(t0)+ E(t0)+deltaT
E=g/l * sin(alfa0)

Midpoint:
k1:
alfa(t0+deltaT)=alfa_t0 + omega(t0+deltaT/2)*deltaT
omega(t0+deltaT/2)=w(t0)+ E(t0)+deltaT/2
E(t0)=g/l * sin(alfa0(t0))
k2:
alfa(t0+deltaT/2)=alfa(t0)+ omega(t0)*deltaT/2
omega(t0+deltaT)= omega(t0)+ E(t0+deltaT/2)*deltaT
E(t0+deltaT/2)=g/l * sin(alfa0(t0+deltaT/2))

RK4
k1_a,k1_w = D(a,w)
a/2, w/2 = E(a,w,k1_a,k1_w,dt/2)
k2_a,k2_w = D(a/2,w/2)
a/2, w/2 = E(a,w,k2_a,k2_w,dt/2)
k3_a,k3_w = D(a/2,w/2)
ae,we = E(a,w,k3_a,k3_w,dt/2)
k4_a,k4_w = D(ae,we)

Alfa = dt * (k1_a + k2_a*2 + k3_a*2 + k4_a*2)/6
omega = dt * (k1_w + k2_w*2 + k3_w*2 + k4_w*2)/6
"""
import math
import matplotlib.pyplot as plt

#---------------- stałe i zmienna deltaT ----------------
l = 1 #int(input("podaj l (najelpszy wykres dla 1):"))
g = -10
alfa0 = math.radians(45) #int(input("podaj kat (alfa0) (najlepszy wykres dla 45)):")
iloscT = 10000 #int(input("podaj ilosc chwil czasowych T (najlepszy wykres dla: 10000):"))
deltaT = 0.0006 #float(input("podaj delta T (najlepszy wykres dla 0,006:").replace(",","."))
m=1 #int(input("podaj m (najlepszy wykres dla 1):"))

def rysowanieWykresu(lista_EP, lista_EK, lista_EC,tytul):
    # ---------------- rysowanie wykresu dla Eulera----------------
    plt.figure(figsize=(10, 6))  # rozmiar wykresu, proporcje
    plt.plot(lista_chwilT, lista_EP, label="EP")  # pierwsza funkcja - energia potecjalna
    plt.plot(lista_chwilT, lista_EK, label="EK")  # druga funkcja - energia kinetyczna
    plt.plot(lista_chwilT, lista_EC, label="EC", linewidth=2, linestyle="--")  # trzecia funkcja - energia calkowita
    plt.xlabel("Czas [s]")  # os x nazwa
    plt.ylabel("Energia [J]")  # os y nazwa
    plt.title(tytul)  # tytul
    plt.legend(loc="lower right")  # legenda
    plt.grid()  # podzialka na wykresie
    plt.show()  # pokazanie wykresu

def energiaPotencjalna(alfa):
    return m * abs(g) * l * (1 - math.cos(alfa))

def energiaKinetyczna(omega):
    return 0.5 * m * (omega * l) ** 2

def Euler(alfa, omega, deltaT, iloscT):
    # ------------------------- przypisanie pierwszych wartosci do tablicy ----------------------
    lista_alfa = [alfa]
    lista_omega = [omega]
    lista_EnergiaPotencjalna = [energiaPotencjalna(alfa)]
    lista_EnergiaKinetyczna = [energiaKinetyczna(omega)]
    lista_EnergiaCalkowita = [lista_EnergiaPotencjalna[0] + lista_EnergiaKinetyczna[0]]
    lista_chwilT = [0]

    for i in range(iloscT):
        # E=  g/l * sin(alfa0)
        E = (g / l) * math.sin(alfa)  # przyspieszenie katowe z sin poprzedniego alfa, omega' = E
        # omega(t0) = w(t0)+ E(t0)+deltaT
        omega = omega + E * deltaT  # aktualizacja predkosci katowej
        # alfa(t0+dt) = alfa(t0)+ omega(t0)*deltaT
        alfa = alfa + omega * deltaT  # aktualizacja kata

        lista_alfa.append(alfa)
        lista_omega.append(omega)
        lista_EnergiaPotencjalna.append(energiaPotencjalna(alfa))#dodanie wyliczenia dla nowej alfy
        lista_EnergiaKinetyczna.append(energiaKinetyczna(omega))#dodanie wyliczenia dla nowej omegi
        lista_EnergiaCalkowita.append(lista_EnergiaPotencjalna[-1] + lista_EnergiaKinetyczna[-1])#energia calkowita to suma potecjalnej i kinetycznej
        lista_chwilT.append((i + 1) * deltaT)#dodanie kolejnej chwili czasowej

    return lista_chwilT, lista_EnergiaPotencjalna, lista_EnergiaKinetyczna, lista_EnergiaCalkowita

def Midpoint(alfa, omega, deltaT, iloscT):
    # ------------------- przypisanie pierwszych wartosci -------------------
    lista_alfa = [alfa]
    lista_omega = [omega]
    lista_EnergiaPotencjalna = [energiaPotencjalna(alfa)]
    lista_EnergiaKinetyczna = [energiaKinetyczna(omega)]
    lista_EnergiaCalkowita = [lista_EnergiaPotencjalna[0] + lista_EnergiaKinetyczna[0]]
    lista_chwilT = [0]

    E = (g / l) * math.sin(alfa)

    for i in range(iloscT):

        #------------------- polowa przedzialu (kroku)-------------------
        h_omega = omega + E * (deltaT/2)
        h_alfa = alfa + h_omega * (deltaT/2)
        h_e = (g/l) * math.sin(h_alfa)

        # ------------------- pelny przedzial (krok) -------------------
        omega = omega + h_e * deltaT
        alfa = alfa + h_omega * deltaT

        # ------------------- dodawanie do list -------------------
        lista_alfa.append(alfa)
        lista_omega.append(omega)
        lista_EnergiaKinetyczna.append(energiaKinetyczna(omega))
        lista_EnergiaPotencjalna.append(energiaPotencjalna(alfa))
        lista_EnergiaCalkowita.append(lista_EnergiaKinetyczna[-1] + lista_EnergiaPotencjalna[-1])
        lista_chwilT.append((i + 1) * deltaT)


    return lista_chwilT,lista_EnergiaPotencjalna,lista_EnergiaKinetyczna,lista_EnergiaCalkowita

def RK4(alfa, omega, deltaT, iloscT):
    # ------------------- przypisanie pierwszych wartosci -------------------
    lista_alfa = [alfa]
    lista_omega = [omega]
    lista_EnergiaPotencjalna = [energiaPotencjalna(alfa)]
    lista_EnergiaKinetyczna = [energiaKinetyczna(omega)]
    lista_EnergiaCalkowita = [lista_EnergiaPotencjalna[0] + lista_EnergiaKinetyczna[0]]
    lista_chwilT = [0]
    E = (g / l) * math.sin(alfa)

    for i in range(iloscT):
        # ------------------- k1 -------------------
        k1_omega = (g/l)*math.sin(alfa)
        k1_alfa = omega

        #------------------- k2 -------------------
        k2_omega = (g/l)*math.sin(alfa + k1_alfa*deltaT/2)
        k2_alfa = omega + k1_omega * deltaT/2

        #------------------- k3 -------------------
        k3_omega = (g/l)*math.sin(alfa + k2_alfa*deltaT/2)
        k3_alfa = omega + k2_omega * deltaT/2

        #------------------- k4 -------------------
        k4_omega = (g/l)*math.sin(alfa + k3_alfa*deltaT)
        k4_alfa = omega + k3_omega * deltaT

        # ------------------- obliczenie nowej alfy i omegi -------------------
        alfa = alfa + deltaT * (k1_alfa + k2_alfa*2 + k3_alfa*2 + k4_alfa)/6
        omega = omega + deltaT * (k1_omega+ k2_omega*2 + k3_omega*2 + k4_omega)/6

        lista_alfa.append(alfa)
        lista_omega.append(omega)
        lista_EnergiaPotencjalna.append(energiaPotencjalna(alfa))
        lista_EnergiaKinetyczna.append(energiaKinetyczna(omega))
        lista_EnergiaCalkowita.append(lista_EnergiaPotencjalna[-1] + lista_EnergiaKinetyczna[-1])
        lista_chwilT.append((i + 1) * deltaT)

    return lista_chwilT, lista_EnergiaPotencjalna, lista_EnergiaKinetyczna, lista_EnergiaCalkowita


# ------------------- obliczenia i rysowanie dla eulera -------------------
lista_chwilT, lista_EP, lista_EK, lista_EC = Euler(alfa0,0,deltaT,iloscT)
rysowanieWykresu(lista_EP, lista_EK, lista_EC, "energia wahadla dla Eulera")

# ------------------- obliczenia i rysowanie dla Midpoint (ulepszony euler) -------------------
lista_chwilT,lista_EP,lista_EK,lista_EC = Midpoint(alfa0,0,deltaT,iloscT)
rysowanieWykresu(lista_EP, lista_EK, lista_EC, "energia wahadla dla Midpoint")

# ------------------- obliczenia i rysowanie dla RK4 -------------------
lista_chwilT,lista_EP,lista_EK,lista_EC = RK4(alfa0,0,deltaT,iloscT)
rysowanieWykresu(lista_EP, lista_EK, lista_EC, "energia wahadla dla RK4")