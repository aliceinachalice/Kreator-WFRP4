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
    # print(f'--- linia {gdzie()}  ---')  # wkleić w miejscu testu


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

mod_rasowy = []
mod_r_ludz = (20, 20, 20, 20, 20, 20, 20, 20, 20, 20)  # WW, US, S, Wt, In, Zw, Int, SW, Ogd
mod_r_kras = (30, 20, 20, 30, 20, 10, 30, 20, 40, 10)
mod_r_niz = (10, 30, 10, 20, 20, 20, 30, 20, 30, 30)
mod_r_elf = (30, 30, 20, 20, 40, 30, 30, 30, 30, 20)


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
    if len(args) == 1:
        args = str(args[0])
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


def prof_rasowe():  # tworzy listę profesji dostęną dla rasy
    for i in range(1, 101):
        prof = profesje(i, rasa)
        lista.append(prof)
        # print(i, prof, lista.count(prof))
        if lista.count(prof) > 1:
            lista.remove(prof)


def grupa_prof():  # pozwala na ręczy wybór profesji
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
    print(f' Wynik: {str(rzut)} - {rasa_postaci}')  # Wynieść poza funkcję
    return rasa_postaci


def profesje(rzut, r_post):  # zakres profesji zależnie od rasy postaci
    # UCZENI
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
# RASA
# 1. Rzut k100
rasa = los_rasy(kosc())
# 2. wybór rasy po rzucie
if akceptacja() == 't':  # przejście dalej i dodanie pd
    pd += 20
else:  # ponowne wykonanie rzutu lub ręczny wybór
    # dodać tu pętlę while do kolejnych rzutów?
    if akceptacja('Nowy rzut [N], czy ręczny wybór [R]?', 'n', 'r') == 'n':  # nowy rzut na rasę
        rasa = los_rasy(kosc())
    else:  # Samodzielny wybór rasy
        tekst = f' Wybierz rasę:\n 1. {rasy[0]:12} 2. {rasy[1]:12}\n 3. {rasy[2]:12} 4. {rasy[3]:12}\n 5. {rasy[4]:12}'
        reczny_wybor = akceptacja(tekst, '1', '2', '3', '4', '5')
        rasa = rasy[int(reczny_wybor) - 1]

if rasa == rasy[0]:  # modyfikator rasowy
    mod_rasowy = mod_r_ludz
elif rasa == rasy[1]:
    mod_rasowy = mod_r_kras
elif rasa == rasy[2]:
    mod_rasowy = mod_r_niz
elif rasa == rasy[3] or rasy[4]:
    mod_rasowy = mod_r_elf
# dodanie rasy do klasy Postac()
# XXX.X = rasa_postaci

# PROFESJA
# 1. Rzut k 100
k100 = kosc()
# 2. Wybór listy na podstawie rasy
prof1 = profesje(k100, rasa)
print(f' Rzut: {k100} - {prof1}')
if akceptacja() == 't':
    prof_post = prof1
    pd += 50  # pd za wybór pierwszego rzutu
else:  # wykonanie dodatkowych rzutów lub ręczny wybór
    k100b = kosc()
    k100c = kosc()
    prof2 = profesje(k100b, rasa)
    prof3 = profesje(k100c, rasa)
    tekst = (f'Czy któryś z tych rzutów jest satysfakcjonujący?\n {k100}. {prof1}\n {k100b}. {prof2}\n'
             f' {k100c}. {prof3}\n [R] - Ręczny wybór')
    reczny_wybor = akceptacja(tekst, str(k100), str(k100b), str(k100c), 'r')
    if reczny_wybor != 'r':  # wybrano jeden z rzutów
        prof_post = profesje(int(reczny_wybor), rasa)
        pd += 25
    else:  # funkcje ręcznego wyboru
        prof_rasowe()
        prof_post = grupa_prof()


print(rasa, prof_post, 'PD : ', pd)
# 5. /    Kolejne rzutu z innymi pd

# ATRYBUTY
# 1. Rzut 2k10 * 10 cech
cechy = ('WW', 'US', 'S', 'Wt', 'I', 'Zw', 'Int', 'SW', 'Ogd')
rzuty = []    # WW, US, S, Wt, In, Zw, Int, SW, Ogd
for i in range(0, 9):
    rzuty.append(kosc(10) + kosc(10))  # dodać do pętli niżej

tekst = ''
tekst2 = ''
for i in range(0, 9):
    tekst += f' {cechy[i]}: {rzuty[i]:02d}'
    tekst2 += f' {cechy[i]}: {rzuty[i] + mod_rasowy[i]}'

print(f' Twoje rzuty na cechy:\n {tekst}\n\n Po uwzględnieniu rasy ({rasa}):\n {tekst2}')
# 3. / +50 pd
if akceptacja() == 't':
    # przejście dalej i dodanie pd
    # pętla dodająca wartości rasowe do rzutów/ dać to na koniec?
    pd += 50
else:
    # 4. / Zamiana miejscami wyników

    # pyta o zmianę kolejności, lub ręczne przypisanie z puli
    if akceptacja('Zamienić rzuty miejscami [Z], czy rozdzielić jako 100 pt? [R]', 'z', 'r') == 'z':
        # W pętli:
        while True:
            pula_start = rzuty  # wartośći tymczasowe
            pula_koniec = []
            tekst = tekst2 = ''
            for i in range(0, 9):  # pyta o kolejne cechy i kaze przypisać jeden z wyników
                #  wyświetla pólę rzutów
                print(f' Twoje rzuty na cechy:\n {tekst}\n\n Po uwzględnieniu rasy ({rasa}):\n {tekst2}')
                wybor = akceptacja(f'{pula_start}\n Wybierz wartość dla {cechy[i]}.', pula_start)
                pula_koniec.append(int(wybor))  # zamienić kolejność
                pula_start.remove(int(wybor))  # obsługa błedu wartości
                tekst += f' {cechy[i]}: {pula_koniec[i]:02d}'  # pokazuje wartości już przypisane
                tekst2 += f' {cechy[i]}: {pula_koniec[i] + mod_rasowy[i]}'
            # pyta o akceptację układu i kończy lub zaczyna od początku
            if akceptacja(f'Akceptujesz ten układ? (T/N)\n {tekst}\n {tekst2}') == 't':
                pd += 25
                break
            else:
                continue

    else:  # ręczny układ
        # W pętli:
        while True:
            punkty = 100  # wyświetla pólę punktów = 100
            pula_koniec = []
            tekst = ''
            tekst2 = ''
            zakresy = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
            for i in range(0, 9):
                # pyta o kolejne cechy i kaze przypisać punkty w zakresie 4-18
                zapas = (len(cechy) - (len(pula_koniec) + 1)) * 4  # Zapas punktów dla minimum
                # punkty powyżej zapasu
                zasob = punkty - zapas
                if zasob > 18:
                    maks = 18
                else:
                    maks = zasob
                    #  tworzy listę dla zakresu
                    zakresy = []
                    for z in range(4, maks + 1):
                        zakresy.append(str(z))
                # pyta o kolejne cechy i kaze przypisać punkty w zakresie 4-18
                print(f' Punkty: {punkty}\n Twoje punkty na cechy:\n {tekst}\n\n Po uwzględnieniu rasy ({rasa}):\n'
                      f' {tekst2}')
                wybor = akceptacja(f' Przypisz do cechy {cechy[i]} punkty w zakresie 4-{maks}',
                                   zakresy)
                pula_koniec.append(int(wybor))
                punkty -= int(wybor)
                tekst += f' {cechy[i]}: {pula_koniec[i]:02d}'
                tekst2 += f' {cechy[i]}: {pula_koniec[i] + mod_rasowy[i]}'
            if punkty > 0:
                akceptacja(f' Nie wydano wszystkich punktów. Pozostało: {punkty}. Naciśnij wpisz [t], aby kontynuować')
                continue
            if akceptacja('Czy taki rozkład punktów jest dobry?') == 't':
                break
            else:
                continue

# TABELA POSTACI
# Podsumowanie wyników.
