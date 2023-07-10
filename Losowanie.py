from random import randint
import os

#############################
#       Tymczasowe          #
#############################
import time  # tylko do pomiaru
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
pd = None  # Doświadczenie zyskiwane w trakcie tworzenia
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
profesja = None

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


#################################
#      Mechanika postaci        #
#################################
def los_rasy(rzut):
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


print("--- linia " + gdzie() + ' ---')
# RASA
# 1. Rzut k100
rasa = los_rasy(kosc())

# 2. wybór rasy po rzucie
if akceptacja() == 't':
    # przejście dalej i dodanie pd
    pd += 20
    # dodanie rasy do klasy Postac()
    # XXXX = rasa_postaci
else:
    # ponowne wykonanie rzutu lub ręczny wybór
    if akceptacja('Nowy rzut [N], czy ręczny wybór [R]?', 'n', 'r') == 'n':
        # nowy rzut na rasę
        rasa = los_rasy(kosc())
    else:
        # Samodzielny wybór rasy
        tekst = ' Wybierz rasę: \n 1.' + rasy[0] + '    2.' + rasy[1] + '\n 3.' + rasy[2] + '   4.' + rasy[3] +\
                '\n 5.' + rasy[4]
        reczny_wybor = akceptacja(tekst, '1', '2', '3', '4', '5')
        if reczny_wybor != '1':
            if reczny_wybor == '2':
                rasa = rasy[1]
            elif reczny_wybor == '3':
                rasa = rasy[2]
            elif reczny_wybor == '4':
                rasa = rasy[3]
            elif reczny_wybor == '5':
                rasa = rasy[4]
        else:
            rasa = rasy[0]
print("--- linia " + gdzie() + ' ---')


# PROFESJA

# 1. Rzut k 100
k100 = randint(1, 100)
# 2. Wybór listy na podstawie rasy

start = time.perf_counter()
if (k100 == 1 and rasa == rasy[0]) or (k100 == 1 and rasa == rasy[1]) or (k100 == 1 and rasa == rasy[2]):
    profesja = klasa[0][0]
elif k100 == 2 and rasa == rasy[0]:
    profesja = klasa[0][1]
elif (k100 == 3 and rasa == rasy[0]) or (k100 <= 4 and rasa == rasy[1]) or (k100 == 2 and rasa == rasy[2]):
    profesja = klasa[0][2]
elif k100 <= 8 and rasa == rasy[0]:
    profesja = klasa[0][3]
elif (k100 == 9 and rasa == rasy[0]) or (k100 == 5 and rasa == rasy[1]) or (k100 <= 4 and rasa == rasy[2]):
    profesja = klasa[0][4]
elif k100 <= 11 and rasa == rasy[0]:
    profesja = klasa[0][5]
elif (k100 == 12 and rasa == rasy[0]) or (k100 <= 7 and rasa == rasy[1]) or (k100 <= 6 and rasa == rasy[2]):
    profesja = klasa[0][6]
elif (k100 <= 14 and rasa == rasy[0]) or (k100 <= 9 and rasa == rasy[1]) or (k100 <= 8 and rasa == rasy[2]):
    profesja = klasa[0][7]
# MIESZCZANIE
elif (k100 == 15 and rasa == rasy[0]) or (k100 <= 11 and rasa == rasy[1]) or (k100 <= 10 and rasa == rasy[2]):
    profesja = klasa[1][0]
elif (k100 == 16 and rasa == rasy[0]) or (k100 <= 15 and rasa == rasy[1]) or (k100 <= 14 and rasa == rasy[2]):
    profesja = klasa[1][1]
elif(k100 <= 19 and rasa == rasy[0]) or (k100 <= 21 and rasa == rasy[1]) or (k100 <= 17 and rasa == rasy[2]):
    profesja = klasa[1][2]
elif (k100 <= 21 and rasa == rasy[0]) or (k100 <= 27 and rasa == rasy[1]) or (k100 <= 22 and rasa == rasy[2]):
    profesja = klasa[1][3]
elif (k100 == 22 and rasa == rasy[0]) or (k100 <= 30 and rasa == rasy[1]) or (k100 <= 24 and rasa == rasy[2]):
    profesja = klasa[1][4]
elif (k100 <= 24 and rasa == rasy[0]) or (k100 == 31 and rasa == rasy[1]) or (k100 <= 27 and rasa == rasy[2]):
    profesja = klasa[1][5]
elif (k100 == 25 and rasa == rasy[0]) or (k100 <= 33 and rasa == rasy[1]) or (k100 <= 29 and rasa == rasy[2]):
    profesja = klasa[1][6]
elif (k100 <= 27 and rasa == rasy[0]) or (k100 == 34 and rasa == rasy[1]) or (k100 <= 33 and rasa == rasy[2]):
    profesja = klasa[1][7]
# DWORZANIE
elif (k100 == 28 and rasa == rasy[0]) or (k100 == 35 and rasa == rasy[1]) or (k100 <= 35 and rasa == rasy[2]):
    profesja = klasa[2][0]
elif (k100 == 29 and rasa == rasy[0]) or (k100 <= 37 and rasa == rasy[1]) or (k100 == 36 and rasa == rasy[2]):
    profesja = klasa[2][1]
elif (k100 == 30 and rasa == rasy[0]) or (k100 <= 39 and rasa == rasy[1]) or (k100 <= 38 and rasa == rasy[2]):
    profesja = klasa[2][2]
elif (k100 == 31 and rasa == rasy[0]) or (k100 <= 41 and rasa == rasy[1]) or (k100 == 39 and rasa == rasy[2]):
    profesja = klasa[2][3]
elif (k100 <= 34 and rasa == rasy[0]) or (k100 == 42 and rasa == rasy[1]) or (k100 <= 45 and rasa == rasy[2]):
    profesja = klasa[2][4]
elif (k100 == 35 and rasa == rasy[0]) or (k100 == 43 and rasa == rasy[1]):
    profesja = klasa[2][5]
elif (k100 == 36 and rasa == rasy[0]) or (k100 == 44 and rasa == rasy[1]) or (k100 == 46 and rasa == rasy[2]):
    profesja = klasa[2][6]
elif (k100 == 37 and rasa == rasy[0]) or (k100 == 45 and rasa == rasy[1]):
    profesja = klasa[2][7]
# POSPÓLSTWO 
elif (k100 <= 42 and rasa == rasy[0]) or (k100 == 46 and rasa == rasy[1]) or (k100 <= 49 and rasa == rasy[2]):
    profesja = klasa[3][0]
elif (k100 == 43 and rasa == rasy[0]) or (k100 <= 51 and rasa == rasy[1]) or (k100 <= 50 and rasa == rasy[2]):
    profesja = klasa[3][1]
elif k100 == 44 and rasa == rasy[0]:
    profesja = klasa[3][2]
elif (k100 <= 46 and rasa == rasy[0]) or (k100 <= 53 and rasa == rasy[1]) or (k100 <= 52 and rasa == rasy[2]):
    profesja = klasa[3][3]
elif k100 == 47 and rasa == rasy[0]:
    profesja = klasa[3][4]
elif (k100 == 48 and rasa == rasy[0]) or (k100 <= 55 and rasa == rasy[1]) or (k100 == 53 and rasa == rasy[2]):
    profesja = klasa[3][5]
elif k100 == 49 and rasa == rasy[0] or (k100 <= 56 and rasa == rasy[2]):
    profesja = klasa[3][6]
elif (k100 == 50 and rasa == rasy[0]) or (k100 == 56 and rasa == rasy[1]) or (k100 == 57 and rasa == rasy[2]):
    profesja = klasa[3][7]
# WĘDROWCY
elif k100 <= 52 and rasa == rasy[0]:
    profesja = klasa[4][0]
elif (k100 == 53 and rasa == rasy[0]) or (k100 <= 58 and rasa == rasy[1]) or (k100 <= 59 and rasa == rasy[2]):
    profesja = klasa[4][1]
elif (k100 <= 55 and rasa == rasy[0]) or (k100 <= 60 and rasa == rasy[1]) or (k100 <= 62 and rasa == rasy[2]):
    profesja = klasa[4][2]
elif k100 == 56 and rasa == rasy[0]:
    profesja = klasa[4][3]
elif (k100 == 57 and rasa == rasy[0]) or (k100 <= 64 and rasa == rasy[1]) or (k100 == 63 and rasa == rasy[2]):
    profesja = klasa[4][4]
elif (k100 == 58 and rasa == rasy[0]) or (k100 <= 66 and rasa == rasy[1]) or (k100 == 65 and rasa == rasy[2]):
    profesja = klasa[4][5]
elif (k100 == 59 and rasa == rasy[0]) or (k100 == 66 and rasa == rasy[2]):
    profesja = klasa[4][6]
elif (k100 == 60 and rasa == rasy[0]) or (k100 == 67 and rasa == rasy[1]) or (k100 <= 68 and rasa == rasy[2]):
    profesja = klasa[4][7]
# WODNIACY
elif (k100 <= 62 and rasa == rasy[0]) or (k100 <= 69 and rasa == rasy[1]) or (k100 <= 71 and rasa == rasy[2]):
    profesja = klasa[5][0]
elif (k100 <= 65 and rasa == rasy[0]) or (k100 <= 71 and rasa == rasy[1]) or (k100 <= 74 and rasa == rasy[2]):
    profesja = klasa[5][1]
elif (k100 == 66 and rasa == rasy[0]) or (k100 == 72 and rasa == rasy[1]) or (k100 == 75 and rasa == rasy[2]):
    profesja = klasa[5][2]
elif (k100 == 67 and rasa == rasy[0]) or (k100 == 73 and rasa == rasy[1]):
    profesja = klasa[5][3]
elif (k100 == 68 and rasa == rasy[0]) or (k100 <= 75 and rasa == rasy[1]) or (k100 <= 79 and rasa == rasy[2]):
    profesja = klasa[5][4]
elif (k100 <= 70 and rasa == rasy[0]) or (k100 == 77 and rasa == rasy[1]) or (k100 == 80 and rasa == rasy[2]):
    profesja = klasa[5][5]
elif (k100 <= 72 and rasa == rasy[0]) or (k100 == 81 and rasa == rasy[2]):
    profesja = klasa[5][6]
elif (k100 <= 74 and rasa == rasy[0]) or (k100 == 78 and rasa == rasy[1]) or (k100 == 82 and rasa == rasy[2]):
    profesja = klasa[5][7]
# ŁOTRY
elif (k100 <= 78 and rasa == rasy[0]) or (k100 == 81 and rasa == rasy[1]) or (k100 == 83 and rasa == rasy[2]):
    profesja = klasa[6][0]
elif k100 == 79 and rasa == rasy[0]:
    profesja = klasa[6][1]
elif (k100 == 80 and rasa == rasy[0]) or (k100 == 82 and rasa == rasy[1]) or (k100 == 84 and rasa == rasy[2]):
    profesja = klasa[6][2]
elif (k100 == 81 and rasa == rasy[0]) or (k100 == 85 and rasa == rasy[2]):
    profesja = klasa[6][3]
elif (k100 <= 83 and rasa == rasy[0]) or (k100 <= 88 and rasa == rasy[2]):
    profesja = klasa[6][4]
elif (k100 == 84 and rasa == rasy[0]) or (k100 == 89 and rasa == rasy[1]):
    profesja = klasa[6][5]
elif (k100 == 85 and rasa == rasy[0]) or (k100 <= 90 and rasa == rasy[2]):
    profesja = klasa[6][6]
elif (k100 <= 88 and rasa == rasy[0]) or (k100 == 84 and rasa == rasy[1]) or (k100 <= 94 and rasa == rasy[2]):
    profesja = klasa[6][7]
# WOJOWNICY
elif (k100 == 89 and rasa == rasy[0]) or (k100 <= 87 and rasa == rasy[1]) or (k100 == 95 and rasa == rasy[2]):
    profesja = klasa[7][0]
elif k100 == 90 and rasa == rasy[0]:
    profesja = klasa[7][1]
elif k100 <= 92 and rasa == rasy[0]:
    profesja = klasa[7][2]
elif (k100 <= 94 and rasa == rasy[0]) or (k100 <= 90 and rasa == rasy[1]) or (k100 <= 97 and rasa == rasy[2]):
    profesja = klasa[7][3]
elif (k100 == 95 and rasa == rasy[0]) or (k100 <= 93 and rasa == rasy[1]):
    profesja = klasa[7][4]
elif k100 == 96 and rasa == rasy[0]:
    profesja = klasa[7][5]
elif k100 <= 97 and rasa == rasy[1]:
    profesja = klasa[7][6]
elif (k100 <= 100 and rasa == rasy[0]) or (k100 <= 100 and rasa == rasy[1]) or (k100 <= 100 and rasa == rasy[2]):
    profesja = klasa[7][7]
else:
    profesja = 'Elfiok'

end = time.perf_counter() - start
print('Rzut:' + str(k100) + ' - ' + profesja)
print(end)

# 3. / późniejszy etap: +50 przy pierwszum wyborze
# 4./ Akceptacja lub rzut
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
