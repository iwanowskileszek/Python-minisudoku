from os import system


def wyswietl():
    for i in range(9):
        if i == 0:
            print("      ----------------------------------")
            print("      |--1--2--3-|--4--5--6-|--7--8--9-|")
            print("      ----------------------------------")
            print("      ----------------------------------")
        if i == 3 or i == 6:
            print("      ----------------------------------")
        for j in range(9):
            if j == 0:
                print(" |",  i+1, "||", end='')
            if j == 3 or j == 6:
                print(" |", end='')
            print(" ", Plansza[i][j], end='')
        print(" |")
    print("      ----------------------------------")
    print("      ----------------------------------")
    print("      |--1--2--3-|--4--5--6-|--7--8--9-|")
    print("      ----------------------------------")


def test():
    Error = 0
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if Plansza[i][j] == Plansza[i][k] and Plansza[i][j] != 0 and k != j:
                    #print("Error = ", 1)
                    Error = 1
    for j in range(9):
        for i in range(9):
            for k in range(9):
                if Plansza[i][j] == Plansza[k][j] and Plansza[i][j] != 0 and k != i:
                    Error = 1
    return Error


Plansza = [
        [4, 9, 8, 2, 0, 3, 1, 0, 7],
        [0, 0, 0, 5, 0, 8, 2, 0, 4],
        [0, 7, 0, 4, 9, 0, 6, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 6, 5],
        [6, 0, 3, 0, 0, 0, 0, 0, 0],
        [2, 0, 7, 0, 5, 9, 0, 3, 1],
        [0, 6, 0, 0, 3, 0, 0, 2, 0],
        [9, 8, 0, 1, 0, 0, 3, 0, 0],
        [0, 2, 4, 7, 8, 0, 5, 1, 9]
    ]

koniec = 0
system('cls')
wyswietl()
for i in range(9):
    for j in range(9):
        if Plansza [i][j] == 0:
            z = 1
            while z < 2:
                system('cls')
                wyswietl()
                print("Podaj cyfrę od 1 do 9 dla wspolzednych (", i+1 ,", ", j+1, ")")
                Plansza [i][j] = int(input("Wartość = "))
                system('cls')
                wyswietl()
                kontrola = test()
                if kontrola == 1 or Plansza [i][j]==0:
                    input("Podana wartość jest nieprawidłowa")
                else:
                    break
