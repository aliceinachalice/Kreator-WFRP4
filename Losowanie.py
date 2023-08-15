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
# pd = pd_wyd = 0  # Doświadczenie zyskiwane w trakcie tworzenia
# rasa = ''
p_dodat = 0  # punkty na PP i PB
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
# prof_post = ''
lista = []  # używane do ręcznego wyboru profesji

mod_rasowy = []
mod_r_ludz = (20, 20, 20, 20, 20, 20, 20, 20, 20, 20)  # WW, US, S, Wt, In, Zw, Int, SW, Ogd
mod_r_kras = (30, 20, 20, 30, 20, 10, 30, 20, 40, 10)
mod_r_niz = (10, 30, 10, 20, 20, 20, 30, 20, 30, 30)
mod_r_elf = (30, 30, 20, 20, 40, 30, 30, 30, 30, 20)


class Postac:
    plec = ''
    rasa = ''
    klasa_post = ''  # Dodanie wartości
    prof_post = ''

    cechy_pocz = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # WW, US, S, Wt, In, Zw, Int, SW, Ogd
    cechy_rozw = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # dodanie wartości

    pp = 0
    pb = 0
    szyb = 0

    pd = 0
    pd_wyd = 0

    @property
    def zyw(self):
        if self.rasa == rasy[2]:
            bs = 0
        else:
            bs = self.c_akt[2] // 10
        bwt = self.c_akt[3] // 10
        bsw = self.c_akt[7] // 10
        return bs + (2 * bwt) + bsw

    @property
    def c_akt(self):  # WW, US, S, Wt, In, Zw, Int, SW, Ogd
        ww = self.cechy_pocz[0] + self.cechy_rozw[0]
        us = self.cechy_pocz[1] + self.cechy_rozw[1]
        s = self.cechy_pocz[2] + self.cechy_rozw[2]
        wt = self.cechy_pocz[3] + self.cechy_rozw[3]
        ini = self.cechy_pocz[4] + self.cechy_rozw[4]
        zw = self.cechy_pocz[5] + self.cechy_rozw[5]
        inte = self.cechy_pocz[6] + self.cechy_rozw[6]
        sw = self.cechy_pocz[7] + self.cechy_rozw[7]
        ogd = self.cechy_pocz[8] + self.cechy_rozw[8]
        return ww, us, s, wt, ini, zw, inte, sw, ogd


#################################
#           Narzędzia           #
#################################

def czysc():  # oczyść ekran
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')


def kosc(k=100):  # rzut kością
    rzut = randint(1, k)
    return rzut


def akceptacja(pytanie=' Akceptujesz wynik rzutu? (T/N)', *args):
    if len(args) == 1:
        args = str(args[0])
    if len(args) == 0:
        args = list(args)
        args.append('t')
        args.append('n')
    while True:
        try:
            tabela()
            tresc = input(f'\n {pytanie}\n  ')
            if tresc.lower() in args:
                return tresc
            else:
                raise ValueError
        except ValueError:
            continue


def prof_rasowe():  # tworzy listę profesji dostęną dla rasy
    for a in range(1, 101):
        prof = profesje(a, p.rasa)
        lista.append(prof)
        if lista.count(prof) > 1:
            lista.remove(prof)


def grupa_prof():  # pozwala na ręczy wybór profesji
    licz = 1
    while licz <= len(lista):
        tresc = ' Wybierz profesję: \n '
        while (licz % 8) != 0:  # stała określająca liczbę profesji w pakiecie
            if licz > len(lista):  # jeśli nie ma więcej elementów w liście
                tresc += '\n '
                break
            tresc += f'{licz:2d}. {lista[licz - 1]:18}'
            if (licz % 4) == 0:  # stała określająca liczbę profesji w rzędzie pakietu
                tresc += '\n '
            licz += 1
        if (licz % 8) == 0 and licz <= len(lista):  # ostani element w wyświetlanym pakiecie.
            tresc += f'{licz:2d}. {lista[licz - 1]:18}'
            licz += 1
        tresc += '\n  [N] - Następne'
        wybrany = akceptacja(tresc, str(licz - 8), str(licz - 7), str(licz - 6), str(licz - 5), str(licz - 4),
                             str(licz - 3), str(licz - 2), str(licz - 1), 'n')
        if wybrany == 'n':  # nastęna grupa profesji
            if licz >= len(lista):  # zapętla na końcu listy
                licz = 1
            continue
        else:
            return lista[int(wybrany) - 1]


def tabela():
    # Tabela ma szerokość 99 znaków plus spacja na początku jako odstęp od krawędzi okna.
    line = '─'
    plc = ''  # paceholder
    cp = p.cechy_pocz
    cr = p.cechy_rozw
    ca = p.c_akt

    czysc()

    print(f' ┌{line*87}┐')
    print(f' │ Imię: {plc:35} Rasa: {p.rasa:21} Płeć: {p.plec:9} │')
    print(f' ├{line * 87}┤')
    print(f' │ Klasa: {p.klasa_post:12} Profesja: {p.prof_post:22} Poziom: {plc:24} │')
    print(f' ├{line*12}┬────┬────┬────┬────┬────┬────┬─────┬────┬─────┬{line*27}┤')
    print(f' │   Cechy    │ WW │ US │  S │ Wt │  I │ Zw │ Int │ SW │ Ogd │       Doświadczenie       │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┬────────┬───────┤')
    print(f' │ Początkowa │ {cp[0]:02} │ {cp[1]:02d} │ {cp[2]:02d} │ {cp[3]:02d} │ {cp[4]:02d} │ {cp[5]:02d} │'
          f'  {cp[6]:02d} │ {cp[7]:02d} │  {cp[8]:02d} │ Aktualne │ Wydane │ Razem │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┼────────┼───────┤')
    print(f' │ Rozwinięcia│ {cr[0]:02d} │ {cr[1]:02d} │ {cr[2]:02d} │ {cr[3]:02d} │ {cr[4]:02d} │ {cr[5]:02d} │'
          f'  {cr[6]:02d} │ {cr[7]:02d} │  {cr[8]:02d} │   {p.pd:4d}   │  {p.pd_wyd:4d}  │  {p.pd + p.pd_wyd:4d} │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┼────────┼───────┤')
    print(f' │  Aktualna  │ {ca[0]:02d} │ {ca[1]:02d} │ {ca[2]:02d} │ {ca[3]:02d} │ {ca[4]:02d} │ {ca[5]:02d} │'
          f'  {ca[6]:02d} │ {ca[7]:02d} │  {ca[8]:02d} │ Żywotność│   {p.zyw:2}   │  {plc:4} │')
    print(f' ├────────────┴─┬──┴────┴────┴─┬──┴────┴────┴────┬┴────┴────┬┴───┬──────┼────┬───┴──┬────┤')
    print(f' │ Pt. Boh.: {p.pb:2d} │ Pt. Det.: {p.pb:02d} │ PP: {p.pp:2d}  PS: {p.pp:02d}  │ Szybkość │ {p.szyb:2}'
          f' │ Chód │ {p.szyb*2:2d} │ Bieg │ {p.szyb*4:2d} │')
    print(f' └──────────────┴──────────────┴─────────────────┴──────────┴────┴──────┴────┴──────┴────┘')
    print(f' {wiad}')


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
p = Postac()

# RASA
# 1. Rzut k100
k100 = kosc()
prop_rasa = los_rasy(k100)
wiad = f' RASA Wynik: {k100:02d} - {prop_rasa}                {gdzie()}'  # Wiad - zmienna tekstu wyświetlana w tabeli
# 2. wybór rasy po rzucie
if akceptacja() == 't':  # przejście dalej i dodanie pd
    p.pd += 20
    p.rasa = prop_rasa  # ostateczny wybór
else:  # ponowne wykonanie rzutu lub ręczny wybór
    # dodać tu pętlę while do kolejnych rzutów?
    k100 = kosc()
    prop_rasa = los_rasy(k100)
    wiad = f' RASA                            {gdzie()}'  # Wiad: tekst wyświetlany w tabeli
    if akceptacja(' Nowy rzut [N], czy ręczny wybór [R]?', 'n', 'r') == 'n':  # nowy rzut na rasę
        p.rasa = prop_rasa  # ostateczny wybór
    else:  # Samodzielny wybór rasy
        wiad = ''
        tekst = f' Wybierz rasę:\n  1. {rasy[0]:12} 2. {rasy[1]:12} 3. {rasy[2]:12} 4. {rasy[3]:12} 5. {rasy[4]:12}'
        reczny_wybor = akceptacja(tekst, '1', '2', '3', '4', '5')
        p.rasa = rasy[int(reczny_wybor) - 1]

if p.rasa == rasy[0]:  # modyfikator rasowy, PP, PB, Szybkość
    mod_rasowy = mod_r_ludz
    p.pp = 2
    p.pb = 1
    p.szyb = 4
    p_dodat = 3
elif p.rasa == rasy[1]:
    mod_rasowy = mod_r_kras
    p.pb = 2
    p.szyb = 3
    p_dodat = 2
elif p.rasa == rasy[2]:
    mod_rasowy = mod_r_niz
    p.pb = 2
    p.szyb = 3
    p_dodat = 3
elif p.rasa == rasy[3] or rasy[4]:
    mod_rasowy = mod_r_elf
    p.szyb = 5
    p_dodat = 2
# dodanie rasy do klasy Postac()

# PROFESJA
# 1. Rzut k 100
k100 = kosc()
# 2. Wybór listy na podstawie rasy
prof1 = profesje(k100, p.rasa)
wiad = f' PROFESJA Wynik: {k100:02d} - {prof1}                {gdzie()}'  # Wiad - zmienna tekstu wyświetlana w tabeli
if akceptacja() == 't':
    p.prof_post = prof1
    p.pd += 50  # pd za wybór pierwszego rzutu
else:  # wykonanie dodatkowych rzutów lub ręczny wybór
    k100b = kosc()
    k100c = kosc()
    prof2 = profesje(k100b, p.rasa)
    prof3 = profesje(k100c, p.rasa)
    wiad = ' PROFESJA'
    tekst = (f' Czy któryś z tych rzutów jest satysfakcjonujący?\n  {k100:02d}. {prof1:18} {k100b:02d}. {prof2:18}'
             f' {k100c:02d}. {prof3:18}\n  [R] - Ręczny wybór')
    reczny_wybor = akceptacja(tekst, str(k100), str(k100b), str(k100c), 'r')
    if reczny_wybor != 'r':  # wybrano jeden z rzutów
        prof_post = profesje(int(reczny_wybor), p.rasa)
        p.pd += 25
    else:  # funkcje ręcznego wyboru
        prof_rasowe()
        p.prof_post = grupa_prof()


print(p.rasa, p.prof_post, 'PD : ', p.pd)  # temp
# 5. /    Kolejne rzutu z innymi pd

# ATRYBUTY
# 1. Rzut 2k10 * 10 cech
wiad = f'                                      {gdzie()}'
cechy = ('WW', 'US', 'S', 'Wt', 'I', 'Zw', 'Int', 'SW', 'Ogd')
rzuty = []    # WW, US, S, Wt, In, Zw, Int, SW, Ogd

tekst = ''
tekst2 = ''
for i in range(0, 9):
    rzuty.append(kosc(10) + kosc(10))  # rzuty dodawane do listy
    tekst += f' {cechy[i]}: {rzuty[i]:02d}'  # przywołane dla tekstu
    tekst2 += f' {cechy[i]}: {rzuty[i] + mod_rasowy[i]}'

wiad += f'\n  Twoje rzuty na cechy:\n {tekst}\n\n  Po uwzględnieniu rasy ({p.rasa}):\n {tekst2}'
# 3. / +50 p.pd
if akceptacja() == 't':
    # przejście dalej i dodanie pd
    # pętla dodająca wartości rasowe do rzutów/ dać to na koniec?
    p.pd += 50
else:
    # 4. / Zamiana miejscami wyników

    # pyta o zmianę kolejności, lub ręczne przypisanie z puli
    if akceptacja('  Zamienić rzuty miejscami [Z], czy rozdzielić jako 100 pt? [R]', 'z', 'r') == 'z':
        # W pętli:
        while True:
            pula_start = rzuty  # wartośći tymczasowe
            pula_koniec = []
            tekst = tekst2 = ''
            for i in range(0, 9):  # pyta o kolejne cechy i kaze przypisać jeden z wyników
                #  wyświetla pólę rzutów
                print(f'  Twoje rzuty na cechy:\n {tekst}\n\n Po uwzględnieniu rasy ({p.rasa}):\n {tekst2}')
                wybor = akceptacja(f' {pula_start}\n Wybierz wartość dla {cechy[i]}.', pula_start)
                pula_koniec.append(int(wybor))  # zamienić kolejność?
                pula_start.remove(int(wybor))  # obsługa błedu wartości
                tekst += f' {cechy[i]}: {pula_koniec[i]:02d}'  # pokazuje wartości już przypisane
                tekst2 += f' {cechy[i]}: {pula_koniec[i] + mod_rasowy[i]}'
            # pyta o akceptację układu i kończy lub zaczyna od początku
            if akceptacja(f'  Akceptujesz ten układ? (T/N)\n {tekst}\n {tekst2}') == 't':
                p.pd += 25
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
                print(f' Punkty: {punkty}\n Twoje punkty na cechy:\n {tekst}\n\n Po uwzględnieniu rasy ({p.rasa}):\n'
                      f' {tekst2}')
                wybor = akceptacja(f' Przypisz do cechy {cechy[i]} punkty w zakresie 4-{maks}',
                                   zakresy)
                pula_koniec.append(int(wybor))
                punkty -= int(wybor)
                tekst += f' {cechy[i]}: {pula_koniec[i]:02d}'
                tekst2 += f' {cechy[i]}: {pula_koniec[i] + mod_rasowy[i]}'
            if punkty > 0:
                akceptacja(f' Nie wydano wszystkich punktów. Pozostało: {punkty}. Wpisz [t], aby kontynuować')
                continue
            if akceptacja(' Czy taki rozkład punktów jest dobry?') == 't':
                break
            else:
                continue
    rzuty = pula_koniec

for i in range(0, 9):  # Dodanie ostatecznych wartości cech do klasy Postac
    p.cechy_pocz[i] = rzuty[i] + mod_rasowy[i]

# Rozdanie punktów dodatkowych na PP i PB
if p_dodat == 3:
    zakresy = (0, 1, 2, 3)
else:
    zakresy = (0, 1, 2)
wiad = f' Masz {p_dodat} punkty do rozdania na Punkty Przeznaczenia i Punkty Bohatera.'
wybor = akceptacja(' Ile wydasz na PP?', zakresy)
p.pp += int(wybor)
p.pb += p_dodat - int(wybor)

# Podsumowanie wyników.
wiad = ''  # temp
tabela()  # temp
