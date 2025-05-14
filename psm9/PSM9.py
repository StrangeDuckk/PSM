#%% md
# zaimplementuj L-sysstem reprezentujacy wzrost drzewa fraktalnego binarnego dla parametrow:
# 
# 
# symbole X F + - [ ]
# 
# poczatkowe zasady: w = X
# 
# P1: X-> F+[[X]-X]-F[-FX]+X
# 
# p2: F -> FF
# 
# + i - rotacja o 25stopni
# 
# [ -> push
# 
# ] -> pop
# 
# F prosto i linia
# X auxiliary symbol
# 
# 
# wartosci poczatkowe:
# x=0, y=0
# Alfa = 25 stopni, w0=X, generuj wn gdzie n to liczba iteracji
#%% md
# importy i parametry stale
#%%
import turtle

kat = 25
znak = "X"
zasady = {
    "X":"F+[[X]-X]-F[-FX]+x",
    "F":"FF"
}
#%% md
# generowanie l-systemu
#%%
def generateLSystem(znak,zasady,iteracje):
    wynik = znak
    for i in range(iteracje):
        kolejne = ""

        for char in wynik:
            kolejne += zasady.get(char,char) #dla kazdego znaku aktualizacja zasady

        wynik = kolejne

    return wynik
#%% md
# rysowanie l-systemu
#%%
def drawLSystem(instrukcje, kat, dlugosc=10):
    stos = []
    for komenda in instrukcje:
        if komenda == "F":
            turtle.forward(dlugosc)
        if komenda == "+":
            turtle.right(kat)
        if komenda == "-":
            turtle.left(kat)
        if komenda == "[":
            stos.append((turtle.pos(), turtle.heading())) #zapamietanie do pozniejszej realizacji
        if komenda == "]":#powrot do przerwanego miescja
            pozycja, kierunek = stos.pop()
            turtle.penup()
            turtle.setpos(pozycja)
            turtle.setheading(kierunek)
            turtle.pendown()
#%% md
# funkcja uruchamiajaca
#%%
def rozpocznijRysowanieDrzewa(iloscIteracji):
    turtle.reset()
    turtle.speed(0)
    turtle.left(90) #patrzy "w gore"
    turtle.penup()
    turtle.setpos(0,-200)
    turtle.pendown()
    instrukcje = generateLSystem(znak,zasady,iloscIteracji)
    drawLSystem(instrukcje,kat,dlugosc=5)
    turtle.done()
#%% md
# wywolanie funkcji uruchamiajacej
#%%
rozpocznijRysowanieDrzewa(4)