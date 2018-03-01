import random

# todo:
# get_number_of_mines():
# pobieranie od uzytkownika liczby calkowitej
# sprawdzanie, czy liczba z zakresu
# sprawdzanie, czy podana zostala liczba
# return liczba
field_size = 50


def get_number_of_mines(mines):
    if mines >= field_size and mines < 1:
        print("BLAD")
        return 0
    else:
        #print(mines)
        return mines


# deploy_mines():
# pobieranie jako argument liczby min i rozmiaru tablicy
# zwracanie wygenerowanej tablicy

def deploy_mines(mines, width, height):
    #tymczasowa tablica, która będzie zwracana. wartość 9 = mina w tym polu.
    tmparr=[[0 for x in range(width)] for y in range(height)]
    tmpMines=mines
    while(True):
        if tmpMines==0:
            return tmparr
        # zmienne do losowania pozycji min
        tmpx = random.randint(0, height - 1)
        tmpy = random.randint(0, width - 1)
        print("Wkladam do x: ", tmpx, " y:", tmpy)
        if 0 == tmparr[tmpx][tmpy]:
            tmparr[tmpx][tmpy]=9
            tmpMines-=1

# number_of_neighboring_mines():
# jako argument dwie wspolrzedne + tablica z minami. Sprawdzanie rekurencyjnie
# sprawdzanie od tej wspolrzednej pol (od x i y)
# [x-1, y-1], [x-1, y], [x,y-1]
# sprawdzanie, czy nie wychodzimy poza tablice (prawdopodobnie wyjątek)
# return liczba_min
def number_of_neighboring_mines(zMinami, x, y):
    nom=0### number of mines
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i==0 and j==0) or x+i<0 or y+j<0:
                pass
            else:
                try:
                    zMinami[x+i][y+j]==9
                except IndexError:
                    pass
                else:
                    if int(zMinami[x+i][y+j])==9:
                        nom+=1
    return nom

# create_board():
#   przekazać tablicę z minami, uzupełnić ilością min na sąsiednich polach
# generowanie pierwotnej tablicy, na które będzie odbywać się gra
# liczby min na sąsiednich i miny
# return tablica_pierwotna

def create_board(zMinami):
    height= len(zMinami)
    width= len(zMinami[0])
    for i in range(height):
        for j in range(width):
            if zMinami[i][j]==0:
                zMinami[i][j]=number_of_neighboring_mines(zMinami, i, j)
    return zMinami

# reveal_squears():
# odkrywanie sąsiednich pól
# rekurencja
# sprawdzanie, czy nie wychodzimy poza zasieg
# jako argument współrzędne podane przez użytkownika
# jeśli wybrane 0, to sprawdzamy rekurencyjnie sąsiednie pola wywołując
# tą samą funkcję z nowymi argumentami
# tworzymy kopię pierwotnej tablicy i jeśli pole=1 oznacza, że już odkrywana
# to u gory zle
# tworzymy nowa, pustą dwuwymiarową tablicę o rozmiarach takich samych, jak nasza plansza

def reveal_squears(tabGlowna, tabCzyOdkryte, x, y):
    if tabGlowna[x][y]!=0:
            tabCzyOdkryte[x][y]=1
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or x + i < 0 or y + j < 0 or x+i>len(tabGlowna)-1 or y+1>len(tabGlowna[0])-1:
                    pass
                else:
                    if tabCzyOdkryte[x+i][y+1]==0:
                        tabCzyOdkryte[x + i][y + j] = 1
                        reveal_squears(tabGlowna, tabCzyOdkryte, x+i, y+j)
        #reveal_squears(tabGlowna, tabCzyOdkryte, i, j)


test = input("Podaj liczbę min na planszy: ")
while (True):
    try:
        get_number_of_mines(int(test))
    except ValueError:
        print("Podano zlą liczbę")
        test = input("Podaj liczbę min na planszy: ")
    else:
        break
print("Eloszka")
width = int(input("Podaj szerokość: "))
height = int(input("Podaj wysokosc: "))
# tworzenie macierzy
tablica = [[0 for x in range(width)] for y in range(height)]
### Tworzenie tablicy, ktora zawiera informacje, czy pola powinny byc wyswietlane
tabCzyOdkryte=[[0 for x in range(width)] for y in range(height)]
#print(len(tablica))
#print(len(tablica[1]))
#print(tablica)
#print(deploy_mines(int(test), width, height))
tabZMinami=deploy_mines(int(test), width, height)
for i in range(height):
    rzad=""
    for j in range(width):
        rzad+=str(tabZMinami[i][j])
        rzad+=" "
    print(rzad)
#print("Sasiedzi z pola [0,0]: ", number_of_neighboring_mines(tabZMinami,9, 9))
tabGlowna=create_board(tabZMinami)
print("\n\n")
print((" "+chr(9473))*width)
for i in range(height):
    rzad=chr(9475)
    for j in range(width):
        rzad+=str(tabGlowna[i][j])
        rzad+=chr(9475)
    print(rzad)
    print((" " + chr(9473)) * width)

reveal_squears(tabGlowna, tabCzyOdkryte, 0, 0)
print("\n\n")
print((" "+chr(9473))*width)
for i in range(height):
    rzad=chr(9475)
    for j in range(width):
        rzad+=str(tabCzyOdkryte[i][j])
        rzad+=chr(9475)
    print(rzad)
    print((" " + chr(9473)) * width)
#print("Test poza zasiegiem", str(tabZMinami[-1][-1]))




# print_board():
# drukowanie
# jesli pole w tymczasowej kopii=1 wyswietla z pierwotnej, jeśli 0, to wypisuje
# spację

# sapper():
# korzystanie z poprzednich funkcji
# odpowiednie komunikaty na ekran
# zczytywanie danych
# zrobić warunek sprawdzający, czy odkryte wszystkie puste pola
# sprawdzić, czy trafiono na minę, zerwanie pętli
