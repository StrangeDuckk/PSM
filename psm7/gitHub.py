#rozwiazanie od serafinski, https://github.com/serafinski/PSM---Podstawy-Symulacji-Komputerowych/blob/main/Cwiczenia_7/main.py

import numpy as np
import matplotlib.pyplot as plt


class WyliczMacierz:
    def __init__(self, rozmiar, gora, lewo, dol, prawo):
        # Macierz kwadratowa wypełniona 0
        self.matrix = np.zeros((rozmiar * rozmiar, rozmiar * rozmiar))
        # Wektor wypełniony 0
        self.vector = np.zeros(rozmiar * rozmiar)
        self.rozmiar = rozmiar
        # Górna granica
        self.gora = gora
        # Lewa granica
        self.lewo = lewo
        # Dolna granica
        self.dol = dol
        # Prawa granica
        self.prawo = prawo

    def wylicz(self):
        # Counter
        index = 0
        for i in range(self.rozmiar):
            for j in range(self.rozmiar):
                # Wylicz górną granicę
                self.licz_gore(i, j, index)
                # Wylicz dolną granicę
                self.licz_dol(i, j, index)
                # Wylicz prawą granicę
                self.licz_prawo(i, j, index)
                # Wylicz lewą granicę
                self.licz_lewo(i, j, index)
                # Ustawiamy wartość elementu diagonalnego na -4
                self.matrix[index, index] = -4
                index += 1

    def licz_gore(self, i, j, index):
        # Jeżeli i jest na górnej granicy
        if i == self.rozmiar - 1:
            # Dodaj górną wartość do odpowiedniego elementu wektora
            self.vector[index] += self.gora
        else:
            # Ustaw na 1
            self.matrix[index, (i + 1) * self.rozmiar + j] = 1

    def licz_dol(self, i, j, index):
        # Jeżeli i jest na dolnej granicy
        if i == 0:
            # Dodaj dolna wartość do odpowiedniego elementu wektora
            self.vector[index] += self.dol
        else:
            # Ustaw na 1
            self.matrix[index, (i - 1) * self.rozmiar + j] = 1

    def licz_lewo(self, i, j, index):
        # Jeżeli j jest na lewej granicy
        if j == self.rozmiar - 1:
            # Dodaj lewa wartość do odpowiedniego elementu wektora
            self.vector[index] += self.lewo
        else:
            # Ustaw na 1
            self.matrix[index, i * self.rozmiar + j + 1] = 1

    def licz_prawo(self, i, j, index):
        # Jeżeli j jest na prawej granicy
        if j == 0:
            # Dodaj prawą wartość do odpowiedniego elementu wektora
            self.vector[index] += self.prawo
        else:
            # Ustaw na 1
            self.matrix[index, i * self.rozmiar + j - 1] = 1

    def get_matrix(self):
        return self.matrix

    def get_vector(self):
        return self.vector


class Gauss:
    # Metoda służąca rozwiązaniu układu liniowego między macierzami A i B
    @staticmethod
    def rozwiaz(A, B):
        # Długość macierzy A
        n = len(A)
        for p in range(n):
            # Znajdź indeks z największą wartością w bieżącej kolumnie
            max_index = np.argmax(np.abs(A[p:, p])) + p
            # Zamień wiersze w A i B, aby przenieść największą wartość na przekątną
            A[[p, max_index]] = A[[max_index, p]]
            B[p], B[max_index] = B[max_index], B[p]

            # Sprawdź, czy macierz jest jednostkowa lub prawie jednostkowa
            if abs(A[p, p]) <= 1e-10:
                raise RuntimeError("Macierz jest jednostkowa, albo prawie jednostkowa")

            # Eliminacja Gaussa na pozostałych wierszach
            for i in range(p + 1, n):
                alpha = A[i, p] / A[p, p]
                B[i] -= alpha * B[p]
                A[i, p:] -= alpha * A[p, p:]

        # Zmiana wsteczna Gaussa
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (B[i] - np.sum(A[i, i + 1:] * x[i + 1:])) / A[i, i]

        return x



count_matrix = WyliczMacierz(40, 200, 100, 150, 50)
count_matrix.wylicz()

answer = Gauss.rozwiaz(count_matrix.get_matrix(), count_matrix.get_vector())

answer_matrix = answer.reshape(count_matrix.rozmiar, count_matrix.rozmiar)

# Wypisanie wyników na konsoli
for i in range(39, -1, -1):
    for j in range(39, -1, -1):
        print(f"{answer[40 * i + j]:.2f}", end=" ")
    print()

# Heatmapa
plt.imshow(answer_matrix, cmap='inferno', origin='lower')
plt.colorbar(label='Wartości')
plt.title('Heatmapa')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.show()