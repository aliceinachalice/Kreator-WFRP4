from random import randint
import os  # na potrzebę czysc()

#############################
#       Tymczasowe          #
#############################
import inspect


def gdzie():
    # https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number
    callerframerecord = inspect.stack()[1]    # 0 represents this line, # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    return str(info.lineno)
    # print(info.lineno)                        # __LINE__     -> 13
    # print("--- linia " + gdzie() + ' ---')  # wkleić w miejscu testu


#################################
#             Spisy             #
#################################
pd = 0  # Doświadczenie zyskiwane w trakcie tworzenia
# rasa = None
rasy = ('Człowiek', 'Krasnolud', 'Niziołek', 'Wysoki elf', 'Leśny elf')

# klasy
uczeni = ('Aptekarka', "Czarodziej", 'Inżynier', 'Kapłan', 'Medyczka', 'Mniszka', 'Prawniczka', 'Uczony')
mieszczanie = ('Agitator', "Kupiec", 'Mieszczka', 'Rzemieślniczka', 'Strażnik', 'Szczurołap', 'Śledczy', 'Żebrak')
dworzanie = ('Artystka', 'Doradca', 'Poseł', 'Namiestnik', 'Służąca', 'Szlachcic', 'Szpieg', 'Zwadźca')
pospolstwo = ('Chłopka', 'Górnik', 'Guślarz', 'Łowczyni', 'Mistyczka', 'Zarządca', 'Zielarka', 'Zwiadowca')
wedrowcy = ('Biczownik', 'Domokrążca', 'Kuglarka', 'Łowca Czarownic', 'Łowczyni Nagród', 'Posłaniec',
            'Strażniczka Dróg', 'Woźnica')
wodniacy = ('Doker', 'Flisak', 'Pilotka Rzeczna', 'Pirat Rzeczny', 'Przemytniczka', 'Przewoźnik', 'Strażnik Rzeczny',
            'Żeglarz')
lotry = ('Banita', 'Czarownica', 'Hiena Cmentarna', 'Paser', 'Rajfur', 'Rekietierka', 'Szarlatan', 'Złodziej')
wojownicy = ('Gladiator', 'Kapłan Bitewny', 'Kawalerzysta', 'Ochroniarz', 'Oprych', 'Rycerz', 'Zabójca', 'Żołnierz')
klasa = (uczeni, mieszczanie, dworzanie, pospolstwo, wedrowcy, wodniacy, lotry, wojownicy)
prof_post = None
lista = []  # używane do ręcznego wyboru profesji

#################################
#           Narzędzia           #
#################################


def czysc():  # oczyść ekran
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')


def kosc(k=100):  # rzut kością
    rzut = randint(1, k)
    return rzut


def akceptacja(pytanie='Akceptujesz wynik rzutu? (T/N)', *args):
    if len(args) == 0:
        args = list(args)
        args.append('t')
        args.append('n')
    while True:
        try:
            tresc = input('\n ' + pytanie + '\n ')
            if tresc.lower() in args:
                return tresc
            else:
                raise ValueError
        except ValueError:
            continue


def prof_rasowe():
    for i in range(1, 101):
        prof = profesje(i, rasa)
        lista.append(prof)
        # print(i, prof, lista.count(prof))
        if lista.count(prof) > 1:
            lista.remove(prof)


def grupa_prof():
    licz = 1
    while licz <= len(lista):
        # tu jest miejsce na czyszczenie ekranu czysc()
        tresc = ' Wybierz profesję: \n '
        while (licz % 6) != 0:  # stała określająca liczbę profesji w pakiecie
            if licz > len(lista):  # jeśli nie ma więcej elementów w liście
                tresc += '\n '
                break
            tresc += str(licz) + '. ' + lista[licz - 1] + '\t'
            if (licz % 3) == 0:  # stała określająca liczbę profesji w rzędzie pakietu
                tresc += '\n '
            licz += 1
        if (licz % 6) == 0 and licz <= len(lista):  # ostani element w wyświetlanym pakiecie.
            tresc += str(licz) + '. ' + lista[licz - 1] + '\t'
            licz += 1
        tresc += '\n [N] - Następne'
        wybor = akceptacja(tresc, str(licz - 6), str(licz - 5), str(licz - 4),
                           str(licz - 3), str(licz - 2), str(licz - 1), 'n')
        if wybor == 'n':  # nastęna grupa profesji
            if licz >= len(lista):  # zapętla na końcu listy
                licz = 1
            continue
        else:
            return lista[int(wybor) - 1]


#################################
#      Mechanika postaci        #
#################################
def los_rasy(rzut):  # Przydział razy postaci
    if rzut > 90:
        if 91 <= rzut <= 94:
            rasa_postaci = rasy[2]
        elif 95 <= rzut <= 98:
            rasa_postaci = rasy[1]
        elif rzut == 99:
            rasa_postaci = rasy[3]
        elif rzut == 100:
            rasa_postaci = rasy[4]
    else:
        rasa_postaci = rasy[0]
    print(" Wynik:" + str(rzut) + " – " + rasa_postaci)
    return rasa_postaci


def profesje(rzut, r_post):  # zakres profesji zależnie od rasy postaci
    if (rzut == 1 and r_post == rasy[0]) or (rzut == 1 and r_post == rasy[1]) or (rzut == 1 and r_post == rasy[2]):
        profesja = klasa[0][0]
    elif rzut == 2 and r_post == rasy[0]:
        profesja = klasa[0][1]
    elif (rzut == 3 and r_post == rasy[0]) or (rzut <= 4 and r_post == rasy[1]) or (rzut == 2 and r_post == rasy[2]):
        profesja = klasa[0][2]
    elif rzut <= 8 and r_post == rasy[0]:
        profesja = klasa[0][3]
    elif (rzut == 9 and r_post == rasy[0]) or (rzut == 5 and r_post == rasy[1]) or (rzut <= 4 and r_post == rasy[2]):
        profesja = klasa[0][4]
    elif rzut <= 11 and r_post == rasy[0]:
        profesja = klasa[0][5]
    elif (rzut == 12 and r_post == rasy[0]) or (rzut <= 7 and r_post == rasy[1]) or (rzut <= 6 and r_post == rasy[2]):
        profesja = klasa[0][6]
    elif (rzut <= 14 and r_post == rasy[0]) or (rzut <= 9 and r_post == rasy[1]) or (rzut <= 8 and r_post == rasy[2]):
        profesja = klasa[0][7]
    # MIESZCZANIE
    elif (rzut == 15 and r_post == rasy[0]) or (rzut <= 11 and r_post == rasy[1]) or (rzut <= 10 and r_post == rasy[2]):
        profesja = klasa[1][0]
    elif (rzut == 16 and r_post == rasy[0]) or (rzut <= 15 and r_post == rasy[1]) or (rzut <= 14 and r_post == rasy[2]):
        profesja = klasa[1][1]
    elif(rzut <= 19 and r_post == rasy[0]) or (rzut <= 21 and r_post == rasy[1]) or (rzut <= 17 and r_post == rasy[2]):
        profesja = klasa[1][2]
    elif (rzut <= 21 and r_post == rasy[0]) or (rzut <= 27 and r_post == rasy[1]) or (rzut <= 22 and r_post == rasy[2]):
        profesja = klasa[1][3]
    elif (rzut == 22 and r_post == rasy[0]) or (rzut <= 30 and r_post == rasy[1]) or (rzut <= 24 and r_post == rasy[2]):
        profesja = klasa[1][4]
    elif (rzut <= 24 and r_post == rasy[0]) or (rzut == 31 and r_post == rasy[1]) or (rzut <= 27 and r_post == rasy[2]):
        profesja = klasa[1][5]
    elif (rzut == 25 and r_post == rasy[0]) or (rzut <= 33 and r_post == rasy[1]) or (rzut <= 29 and r_post == rasy[2]):
        profesja = klasa[1][6]
    elif (rzut <= 27 and r_post == rasy[0]) or (rzut == 34 and r_post == rasy[1]) or (rzut <= 33 and r_post == rasy[2]):
        profesja = klasa[1][7]
    # DWORZANIE
    elif (rzut == 28 and r_post == rasy[0]) or (rzut == 35 and r_post == rasy[1]) or (rzut <= 35 and r_post == rasy[2]):
        profesja = klasa[2][0]
    elif (rzut == 29 and r_post == rasy[0]) or (rzut <= 37 and r_post == rasy[1]) or (rzut == 36 and r_post == rasy[2]):
        profesja = klasa[2][1]
    elif (rzut == 30 and r_post == rasy[0]) or (rzut <= 39 and r_post == rasy[1]) or (rzut <= 38 and r_post == rasy[2]):
        profesja = klasa[2][2]
    elif (rzut == 31 and r_post == rasy[0]) or (rzut <= 41 and r_post == rasy[1]) or (rzut == 39 and r_post == rasy[2]):
        profesja = klasa[2][3]
    elif (rzut <= 34 and r_post == rasy[0]) or (rzut == 42 and r_post == rasy[1]) or (rzut <= 45 and r_post == rasy[2]):
        profesja = klasa[2][4]
    elif (rzut == 35 and r_post == rasy[0]) or (rzut == 43 and r_post == rasy[1]):
        profesja = klasa[2][5]
    elif (rzut == 36 and r_post == rasy[0]) or (rzut == 44 and r_post == rasy[1]) or (rzut == 46 and r_post == rasy[2]):
        profesja = klasa[2][6]
    elif (rzut == 37 and r_post == rasy[0]) or (rzut == 45 and r_post == rasy[1]):
        profesja = klasa[2][7]
    # POSPÓLSTWO
    elif (rzut <= 42 and r_post == rasy[0]) or (rzut == 46 and r_post == rasy[1]) or (rzut <= 49 and r_post == rasy[2]):
        profesja = klasa[3][0]
    elif (rzut == 43 and r_post == rasy[0]) or (rzut <= 51 and r_post == rasy[1]) or (rzut <= 50 and r_post == rasy[2]):
        profesja = klasa[3][1]
    elif rzut == 44 and r_post == rasy[0]:
        profesja = klasa[3][2]
    elif (rzut <= 46 and r_post == rasy[0]) or (rzut <= 53 and r_post == rasy[1]) or (rzut <= 52 and r_post == rasy[2]):
        profesja = klasa[3][3]
    elif rzut == 47 and r_post == rasy[0]:
        profesja = klasa[3][4]
    elif (rzut == 48 and r_post == rasy[0]) or (rzut <= 55 and r_post == rasy[1]) or (rzut == 53 and r_post == rasy[2]):
        profesja = klasa[3][5]
    elif rzut == 49 and r_post == rasy[0] or (rzut <= 56 and r_post == rasy[2]):
        profesja = klasa[3][6]
    elif (rzut == 50 and r_post == rasy[0]) or (rzut == 56 and r_post == rasy[1]) or (rzut == 57 and r_post == rasy[2]):
        profesja = klasa[3][7]
    # WĘDROWCY
    elif rzut <= 52 and r_post == rasy[0]:
        profesja = klasa[4][0]
    elif (rzut == 53 and r_post == rasy[0]) or (rzut <= 58 and r_post == rasy[1]) or (rzut <= 59 and r_post == rasy[2]):
        profesja = klasa[4][1]
    elif (rzut <= 55 and r_post == rasy[0]) or (rzut <= 60 and r_post == rasy[1]) or (rzut <= 62 and r_post == rasy[2]):
        profesja = klasa[4][2]
    elif rzut == 56 and r_post == rasy[0]:
        profesja = klasa[4][3]
    elif (rzut == 57 and r_post == rasy[0]) or (rzut <= 64 and r_post == rasy[1]) or (rzut == 63 and r_post == rasy[2]):
        profesja = klasa[4][4]
    elif (rzut == 58 and r_post == rasy[0]) or (rzut <= 66 and r_post == rasy[1]) or (rzut == 65 and r_post == rasy[2]):
        profesja = klasa[4][5]
    elif (rzut == 59 and r_post == rasy[0]) or (rzut == 66 and r_post == rasy[2]):
        profesja = klasa[4][6]
    elif (rzut == 60 and r_post == rasy[0]) or (rzut == 67 and r_post == rasy[1]) or (rzut <= 68 and r_post == rasy[2]):
        profesja = klasa[4][7]
    # WODNIACY
    elif (rzut <= 62 and r_post == rasy[0]) or (rzut <= 69 and r_post == rasy[1]) or (rzut <= 71 and r_post == rasy[2]):
        profesja = klasa[5][0]
    elif (rzut <= 65 and r_post == rasy[0]) or (rzut <= 71 and r_post == rasy[1]) or (rzut <= 74 and r_post == rasy[2]):
        profesja = klasa[5][1]
    elif (rzut == 66 and r_post == rasy[0]) or (rzut == 72 and r_post == rasy[1]) or (rzut == 75 and r_post == rasy[2]):
        profesja = klasa[5][2]
    elif (rzut == 67 and r_post == rasy[0]) or (rzut == 73 and r_post == rasy[1]):
        profesja = klasa[5][3]
    elif (rzut == 68 and r_post == rasy[0]) or (rzut <= 75 and r_post == rasy[1]) or (rzut <= 79 and r_post == rasy[2]):
        profesja = klasa[5][4]
    elif (rzut <= 70 and r_post == rasy[0]) or (rzut == 77 and r_post == rasy[1]) or (rzut == 80 and r_post == rasy[2]):
        profesja = klasa[5][5]
    elif (rzut <= 72 and r_post == rasy[0]) or (rzut == 81 and r_post == rasy[2]):
        profesja = klasa[5][6]
    elif (rzut <= 74 and r_post == rasy[0]) or (rzut == 78 and r_post == rasy[1]) or (rzut == 82 and r_post == rasy[2]):
        profesja = klasa[5][7]
    # ŁOTRY
    elif (rzut <= 78 and r_post == rasy[0]) or (rzut == 81 and r_post == rasy[1]) or (rzut == 83 and r_post == rasy[2]):
        profesja = klasa[6][0]
    elif rzut == 79 and r_post == rasy[0]:
        profesja = klasa[6][1]
    elif (rzut == 80 and r_post == rasy[0]) or (rzut == 82 and r_post == rasy[1]) or (rzut == 84 and r_post == rasy[2]):
        profesja = klasa[6][2]
    elif (rzut == 81 and r_post == rasy[0]) or (rzut == 85 and r_post == rasy[2]):
        profesja = klasa[6][3]
    elif (rzut <= 83 and r_post == rasy[0]) or (rzut <= 88 and r_post == rasy[2]):
        profesja = klasa[6][4]
    elif (rzut == 84 and r_post == rasy[0]) or (rzut == 89 and r_post == rasy[1]):
        profesja = klasa[6][5]
    elif (rzut == 85 and r_post == rasy[0]) or (rzut <= 90 and r_post == rasy[2]):
        profesja = klasa[6][6]
    elif (rzut <= 88 and r_post == rasy[0]) or (rzut == 84 and r_post == rasy[1]) or (rzut <= 94 and r_post == rasy[2]):
        profesja = klasa[6][7]
    # WOJOWNICY
    elif (rzut == 89 and r_post == rasy[0]) or (rzut <= 87 and r_post == rasy[1]) or (rzut == 95 and r_post == rasy[2]):
        profesja = klasa[7][0]
    elif rzut == 90 and r_post == rasy[0]:
        profesja = klasa[7][1]
    elif rzut <= 92 and r_post == rasy[0]:
        profesja = klasa[7][2]
    elif (rzut <= 94 and r_post == rasy[0]) or (rzut <= 90 and r_post == rasy[1]) or (rzut <= 97 and r_post == rasy[2]):
        profesja = klasa[7][3]
    elif (rzut == 95 and r_post == rasy[0]) or (rzut <= 93 and r_post == rasy[1]):
        profesja = klasa[7][4]
    elif rzut == 96 and r_post == rasy[0]:
        profesja = klasa[7][5]
    elif rzut <= 97 and r_post == rasy[1]:
        profesja = klasa[7][6]
    elif (rzut <= 100 and r_post == rasy[0]) or (rzut <= 100 and r_post == rasy[1])\
            or (rzut <= 100 and r_post == rasy[2]):
        profesja = klasa[7][7]
    else:
        profesja = 'Elfiok'  # póki wena na przepisywanie kolumn nie wróci
    return profesja


#####################################
#       Tworzenie postaci           #
#####################################
print("--- linia " + gdzie() + ' ---')
# RASA
# 1. Rzut k100
rasa = los_rasy(kosc())
# 2. wybór rasy po rzucie
if akceptacja() == 't':
    # przejście dalej i dodanie pd
    pd += 20
else:  # ponowne wykonanie rzutu lub ręczny wybór
    # dodać tu pętlę while do kolejnych rzutów?
    if akceptacja('Nowy rzut [N], czy ręczny wybór [R]?', 'n', 'r') == 'n':  # nowy rzut na rasę
        rasa = los_rasy(kosc())
    else:  # Samodzielny wybór rasy
        tekst = 'Wybierz rasę: \n 1.' + rasy[0] + '    2.' + rasy[1] + '\n 3.' + rasy[2] + '    4.' + rasy[3] +\
                '\n 5.' + rasy[4]
        reczny_wybor = akceptacja(tekst, '1', '2', '3', '4', '5')
        rasa = rasy[int(reczny_wybor)-1]
        print(rasa)  # temp
# dodanie rasy do klasy Postac()
# XXXX = rasa_postaci
print("--- linia " + gdzie() + ' ---')

# PROFESJA
# 1. Rzut k 100
k100 = kosc()
# 2. Wybór listy na podstawie rasy
prof1 = profesje(k100, rasa)
print(' Rzut:' + str(k100) + ' - ' + prof1)
if akceptacja() == 't':
    prof_post = prof1
    pd += 50  # pd za wybór pierwszego rzutu
else:  # wykonanie dodatkowych rzutów lub ręczny wybór
    k100b = kosc()
    k100c = kosc()
    prof2 = profesje(k100b, rasa)
    prof3 = profesje(k100c, rasa)
    tekst = 'Czy któryś z tych rzutów jest satysfakcjonujący?\n ' + str(k100) + '. ' + prof1 + '\n ' + str(k100b)\
            + '. ' + prof2 + '\n ' + str(k100c) + '. ' + prof3 + '\n [R] - Ręczny wybór'
    reczny_wybor = akceptacja(tekst, str(k100), str(k100b), str(k100c), 'r')
    if reczny_wybor != 'r':  # wybrano jeden z rzutów
        prof_post = profesje(int(reczny_wybor), rasa)
        pd += 25
    else:  # funkcje ręcznego wyboru
        prof_rasowe()
        prof_post = grupa_prof()


print(rasa, prof_post, 'PD : ', pd)
print("--- linia " + gdzie() + ' ---')
# 5. /    Kolejne rzutu z innymi pd

# ATRYBUTY
# 1. Rzut 2k10 * 10 cech

WW = kosc(10) + kosc(10)
US = kosc(10) + kosc(10)
S = kosc(10) + kosc(10)
Wt = kosc(10) + kosc(10)
In = kosc(10) + kosc(10)
Zw = kosc(10) + kosc(10)
Zr = kosc(10) + kosc(10)
Int = kosc(10) + kosc(10)
SW = kosc(10) + kosc(10)
Ogd = kosc(10) + kosc(10)

print(WW, US, S, Wt, In, Zw, Int, SW, Ogd)
# 2. uwzględnienie rasy
if rasa == rasy[0]:
    WW += 20
    US += 20
    S += 20
    Wt += 20
    In += 20
    Zw += 20
    Zr += 20
    Int += 20
    SW += 20
    Ogd += 20
elif rasa == rasy[1]:
    WW += 30
    US += 20
    S += 20
    Wt += 30
    In += 20
    Zw += 10
    Zr += 30
    Int += 20
    SW += 40
    Ogd += 10
elif rasa == rasy[2]:
    WW += 10
    US += 30
    S += 10
    Wt += 20
    In += 20
    Zw += 20
    Zr += 30
    Int += 20
    SW += 30
    Ogd += 30
elif rasa == rasy[3] or rasy[4]:
    WW += 30
    US += 30
    S += 20
    Wt += 20
    In += 40
    Zw += 30
    Zr += 30
    Int += 30
    SW += 30
    Ogd += 20

print(WW, US, S, Wt, In, Zw, Int, SW, Ogd)
# 3. / +50 pd
# 4. / Zamiana miejscami wyników
# 5./ +25 pd
# 6 / ponowne rzuty lub ręczny rozkład 100 pt.

# TABELA POSTACI
# Podsumowanie wyników.

# Przydasie

# liczba z wiodącym zerem
'''
print(f"{US:02d}")
zz = f"{US:02d}"
print(zz)'''
