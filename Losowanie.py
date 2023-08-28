from random import randint
import os  # na potrzebę czysc()

#############################
#       Tymczasowe          #
#############################
import inspect
import profesje as pr


class Empty:  # tem
    nazwa = nazwa_poz = ['', '']


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
tab_gl = True  # dla tabeli umiejętności
rasy = ('Człowiek', 'Krasnolud', 'Niziołek', 'Wysoki elf', 'Leśny elf')
# klasy
# uczeni = ('Aptekarka', "Czarodziej", 'Inżynier', 'Kapłan', 'Medyczka', 'Mniszka', 'Prawniczka', 'Uczony')
uczeni = (pr.Aptekarka, pr.Czarodziej, pr.Inzynier, pr.Kaplan, pr.Medyczka, pr.Mniszka, pr.Prawniczka, pr.Uczony)
mieszczanie = (pr.Agitator, pr.Kupiec, pr.Mieszczka, pr.Rzemieslniczka, pr.Straznik, pr.Szczurolap, pr.Sledczy,
               pr.Zebrak)
dworzanie = (pr.Artystka, pr.Doradca, pr.Posel, pr.Namiestnik, pr.Sluzaca, pr.Szlachcic, pr.Szpieg, pr.Zwadzca)
pospolstwo = (pr.Chlopka, pr.Gornik, pr.Guslarz, pr.Lowczyni, pr.Mistyczka, pr.Zarzadca, pr.Zielarka, pr.Zwiadowca)
wedrowcy = (pr.Biczownik, pr.Domokrazca, pr.Kuglarka, pr.LowcaCzarownic, pr.LowczyniNagrod, pr.Poslaniec,
            pr.StrazniczkaDrog, pr.Woznica)
wodniacy = (pr.Doker, pr.Flisak, pr.PilotkaRzeczna, pr.PiratRzeczny, pr.Przemytniczka, pr.Przewoznik,
            pr.StraznikRzeczny, pr.Zeglarz)
lotry = (pr.Banita, pr.Czarownica, pr.HienaCmentarna, pr.Paser, pr.Rajfur, pr.Rekietierka, pr.Szarlatan, pr.Zlodziej)
wojownicy = (pr.Gladiator, pr.KaplanBitewny, pr.Kawalerzysta, pr.Ochroniarz, pr.Oprych, pr.Rycerz, pr.Zabojca,
             pr.Zolnierz)
klasa = (uczeni, mieszczanie, dworzanie, pospolstwo, wedrowcy, wodniacy, lotry, wojownicy)
# prof_post = ''
lista = []  # używane do ręcznego wyboru profesji

# Rasowe modyfikatory cech
mod_rasowy = []
mod_r_ludz = (20, 20, 20, 20, 20, 20, 20, 20, 20, 20)  # WW, US, S, Wt, In, Zw, Zr, Int, SW, Ogd
mod_r_kras = (30, 20, 20, 30, 20, 10, 30, 20, 40, 10)
mod_r_niz = (10, 30, 10, 20, 20, 20, 30, 20, 30, 30)
mod_r_elf = (30, 30, 20, 20, 40, 30, 30, 30, 30, 20)


class Postac:
    plec = 2
    rasa = ''
    prof = None
    klasa_post = ''  # Dodanie wartości

    cechy_pocz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # WW, US, S, Wt, In, Zw, Zr, Int, SW, Ogd
    cechy_rozw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # dodanie wartości

    pp = 0
    pb = 0
    szyb = 0

    pd = 0
    pd_wyd = 0

    # Lista um podstawowych w tabeli z którą porównuje w trakcie generowania?
    # w tabeli sprawdza czy wykupiona lub podstawowa i dopisuje?
    # zmienna = [nazwa, cecha, rozwinięcia]
    atle = ['Atletyka', 'Zw', 0]  # Podstawowa
    bada = ['Badania Naukowe', 'Int', 0]

    bbia = ['Broń Biała (Podstawowa)', 'WW', 0]  # Podstawowa / # Specjalizacje:
    bbij = ['Broń Biała (Bijatyka)', 'WW', 0]  # Bijatyka
    bdrz = ['Broń Biała (Drzewcowa)', 'WW', 0]  # Drzewcowa
    bdwr = ['Broń Biała (Dwuręczna)', 'WW', 0]  # Dwuręczna
    bkaw = ['Broń Biała (Kawaleryjska)', 'WW', 0]  # Kawaleryjska
    bcep = ['Broń Biała (Korbacze)', 'WW', 0]  # Korbacze
    bpar = ['Broń Biała (Parująca)', 'WW', 0]  # Parująca
    bszr = ['Broń Biała (Szermiercza)', 'WW', 0]  # Szermiercza

    bzpr = ['Broń Zasięgowa (Proce)', 'US', 0]  # Specjalizacje: Proce
    bzlu = ['Broń Zasięgowa (Łuki)', 'US', 0]  # Łuki
    bzku = ['Broń Zasięgowa (Kusze)', 'US', 0]  # Kusze
    bzmi = ['Broń Zasięgowa (Miotana)', 'US', 0]  # Broń Miotana
    bzop = ['Broń Zasięgowa (Oplątująca)', 'US', 0]  # Broń Oplątująca
    bzmw = ['Broń Zas. (Mat. Wybuchowe)', 'US', 0]  # Materiały Wybuchowe
    bzps = ['Broń Zasięgowa (Prochowa)', 'US', 0]  # Broń Prochowa
    bzex = ['Broń Zas. (Eksperymentalna)', 'US', 0]  # Broń Eksperymentalna

    char = ['Charyzma', 'Ogd', 0]  # Podstawowa
    dowo = ['Dowodzenie', 'Ogd', 0]  # Podstawowa
    haza = ['Hazard', 'Int', 0]  # Podstawowa
    intu = ['Intuicja', 'I', 0]  # Podstawowa

    jezk = ['Jeździectwo (Konie)', 'Zw', 0]  # Podstawowa / Konie
    jezg = ['Jeździectwo (Gryfy)', 'Zw', 0]  # Gryfy
    jezp = ['Jeździectwo (Pegazy)', 'Zw', 0]  # Pegazy
    jezs = ['Jeździectwo (Półgryfy)', 'Zw', 0]  # Półgryfy
    jezw = ['Jeździectwo (Wielkie Wilki)', 'Zw', 0]  # Wielkie Wilki

    jezy = ['Język (Reikspiel)', 'Int', 0]  # Specjalizacje: Reikspiel
    jalb = ['Język (Albioński)', 'Int', 0]  # Albioński
    jbit = ['Język (Bitewny)', 'Int', 0]  # Bitewny
    jbrt = ['Język (Bretoński)', 'Int', 0]  # Bretoński
    jelf = ['Język (Elthárin)', 'Int', 0]  # Elthárin (elficki)
    jest = ['Język (Estalijski)', 'Int', 0]  # Estalijski
    jork = ['Język (Grumbarth)', 'Int', 0]  # Grumbarth (orczy)
    jkis = ['Język (Hospodarnyj)', 'Int', 0]  # Hospodarnyj (kislevski)
    jjkr = ['Język (Jałowej Krainy)', 'Int', 0]  # Jałowej Krainy
    jkrs = ['Język (Khazalid)', 'Int', 0]  # Khazalid
    jkls = ['Język (Klasyczny)', 'Int', 0]  # Klasyczny
    jniz = ['Język (Krainy Zgromadzenia)', 'Int', 0]  # Krainy Zgromadzenia
    jmag = ['Język (Magiczny)', 'Int', 0]  # Magiczny
    jnrs = ['Język (Norsmeński)', 'Int', 0]  # Norsmeński
    jskv = ['Język (Queekish)', 'Int', 0]  # Queekish(skav)
    jtil = ['Język (Tileański)', 'Int', 0]  # Tileański
    jgil = ['Język (Gildii)', 'Int', 0]  # Gildii
    jzlo = ['Język (Złodziejski)', 'Int', 0]  # Złodziejska grypsera

    kugl = ['Kuglarstwo', 'Zw', 0]

    lecz = ['Leczenie', 'Int', 0]
    mglo = ['Mocna Głowa', 'Wt', 0]  # Podstawowa
    modl = ['Modlitwa', 'Ogd', 0]

    mdud = ['Muzyka (Dudy)', 'Zr', 0]  # Dudy
    muhr = ['Muzyka (Harfa)', 'Zr', 0]  # Harfa
    mulu = ['Muzyka (Lutnia)', 'Zr', 0]  # Lutnia
    muob = ['Muzyka (Obój)', 'Zr', 0]  # Obój
    musk = ['Muzyka (Skrzypce)', 'Zr', 0]  # Skrzypce
    mufl = ['Muzyka (Flet)', 'Zr', 0]  # Flet

    nawi = ['Nawigacja', 'I', 0]  # Podstawowa
    odpo = ['Odporność', 'Wt', 0]  # Podstawowa
    opan = ['Opanowanie', 'SW', 0]  # Podstawowa
    opzw = ['Opieka nad Zwierzętami', 'Int', 0]
    oswa = ['Oswajanie', 'SW', 0]  # Podstawowa
    otza = ['Otwieranie Zamków', 'Zr', 0]
    perc = ['Percepcja', 'I', 0]  # Podstawowa
    plot = ['Plotkowanie', 'Ogd', 0]  # Podstawowa
    powo = ['Powożenie', 'Zw', 0]  # Podstawowa
    prze = ['Przekupstwo', 'Ogd', 0]  # Podstawowa
    plyw = ['Pływanie', 'S', 0]

    rapt = ['Rzemiosło (Aptekarstwo)', 'Zr', 0]  # Aptekarstwo
    rbal = ['Rzemiosło (Balsamowanie)', 'Zr', 0]  # Balsamowanie
    rgrb = ['Rzemiosło (Garbarstwo)', 'Zr', 0]  # Garbarstwo
    rgot = ['Rzemiosło (Gotowanie)', 'Zr', 0]  # Gotowanie
    rkal = ['Rzemiosło (Kaligrafa)', 'Zr', 0]  # Kaligrafa
    rkow = ['Rzemiosło (Kowalstwo)', 'Zr', 0]  # Kowalstwo
    rswi = ['Rzemiosło (Świecarstwo)', 'Zr', 0]  # Świecarstwo
    rgar = ['Rzemiosło (Garncarstwo)', 'Zr', 0]  # Garncarstwo
    rkam = ['Rzemiosło (Kamieniarstwo)', 'Zr', 0]  # Kamieniarstwo
    rtru = ['Rzemiosło (Truciciel)', 'Zr', 0]  # Truciciel

    scch = ['Sekretne Znaki (Cechu)', 'Int', 0]  # Cechu
    skoc = ['Sekretne Znaki (Kol. Cienia)', 'Int', 0]  # Kolegium Cienia
    slow = ['Sekretne Znaki (Łowców)', 'Int', 0]  # Łowców
    swed = ['Sekretne Znaki (Włóczęgów)', 'Int', 0]  # Włóczęgów
    szlo = ['Sekretne Znaki (Złodziei)', 'Int', 0]  # Złodziei
    szwd = ['Sekretne Znaki (Zwiadowców)', 'Int', 0]  # Zwiadowców

    skrp = ['Skradanie (Podziemia)', 'Zw', 0]  # Podstawowa Podziemia
    skrm = ['Skradanie (Miasto)', 'Zw', 0]  # Podstawowa Miasto
    skrw = ['Skradanie (Wieś)', 'Zw', 0]  # Podstawowa Wieś

    splm = ['Splatanie Magii (Aqshy)', 'SW', 0]  # Ogólne
    smaq = ['Splatanie Magii (Aqshy)', 'SW', 0]  # (Aqshy)
    smaz = ['Splatanie Magii (Azyr)', 'SW', 0]  # (Azyr)
    smch = ['Splatanie Magii (Chamon)', 'SW', 0]  # (Chamon)
    smdr = ['Splatanie Magii (Dhar)', 'SW', 0]  # (Dhar)
    smgr = ['Splatanie Magii (Ghur)', 'SW', 0]  # (Ghur)
    smgn = ['Splatanie Magii (Ghyran)', 'SW', 0]  # (Ghyran)
    smhy = ['Splatanie Magii (Hysh)', 'SW', 0]  # (Hysh)
    smsh = ['Splatanie Magii (Shyish)', 'SW', 0]  # (Shyish)
    smul = ['Splatanie Magii (Ulgu)', 'SW', 0]  # (Ulgu)

    sztu = ['Sztuka', 'Zr', 0]  # Podstawowa

    sprz = ['Sztuka Przetrwania', 'Int', 0]  # Podstawowa
    targ = ['Targowanie', 'Ogd', 0]  # Podstawowa
    tres = ['Tresura', 'Int', 0]
    trop = ['Tropienie', 'I', 0]
    unik = ['Unik', 'Zw', 0]  # Podstawowa

    wchm = ['Wiedza (Chemia)', 'Int', 0]  # Specjalizacje: Chemia
    wgeo = ['Wiedza (Geologia)', 'Int', 0]  # Geologia
    wher = ['Wiedza (Heraldyka)', 'Int', 0]  # Heraldyka
    whis = ['Wiedza (Historia)', 'Int', 0]  # Historia
    winz = ['Wiedza (Inżynieria)', 'Int', 0]  # Inżynieria
    wmag = ['Wiedza (Magia)', 'Int', 0]  # Magia
    wmed = ['Wiedza (Medycyna)', 'Int', 0]  # Medycyna
    wmet = ['Wiedza (Metalurgia)', 'Int', 0]  # Metalurgia
    wnau = ['Wiedza (Nauka)', 'Int', 0]  # Nauka
    wpra = ['Wiedza (Prawo)', 'Int', 0]  # Prawo
    wros = ['Wiedza (Rośliny)', 'Int', 0]  # Rośliny
    wteo = ['Wiedza (Teologia)', 'Int', 0]  # Teologia
    wwoj = ['Wiedza (Wojna)', 'Int', 0]  # Wojna
    wimp = ['Wiedza (Reikland)', 'Int', 0]  # Reikland
    wkrs = ['Wiedza (Krasnoludy)', 'Int', 0]  # Wiedza (Krasnoludy)

    wios = ['Wioślarstwo', 'S', 0]  # Podstawowa
    wspi = ['Wspinaczka', 'S', 0]  # Podstawowa
    wycn = ['Wycena', 'Int', 0]

    wsak = ['Występy (Aktorstwo)', 'Ogd', 0]  # Podstawowa / Aktorstwo
    wsga = ['Wyst. (Gawędziarstwo)', 'Ogd', 0]  # Podstawowa / Gawędziarstwo
    wsko = ['Wyst. (Komedianctwo)', 'Ogd', 0]  # Podstawowa / Komedianctwo
    wssp = ['Występy (Śpiewanie)', 'Ogd', 0]  # Podstawowa / Śpiewanie

    zpul = ['Zastawianie Pułapek', 'Zr', 0]
    zast = ['Zastraszanie', 'S', 0]  # Podstawowa
    zwpa = ['Zwinne Palce', 'Zr', 0]
    zegl = ['Żeglarstwo', 'Zw', 0]

    @property
    def ple(self):
        if self.plec == 0:
            rodzaj = "Mężczyzna"
        elif self.plec == 1:
            rodzaj = "Kobieta"
        else:
            rodzaj = ''
        return rodzaj

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
    def c_akt(self):  # WW, US, S, Wt, In, Zw, Zr, Int, SW, Ogd
        ww = self.cechy_pocz[0] + self.cechy_rozw[0]
        us = self.cechy_pocz[1] + self.cechy_rozw[1]
        s = self.cechy_pocz[2] + self.cechy_rozw[2]
        wt = self.cechy_pocz[3] + self.cechy_rozw[3]
        ini = self.cechy_pocz[4] + self.cechy_rozw[4]
        zw = self.cechy_pocz[5] + self.cechy_rozw[5]
        zr = self.cechy_pocz[6] + self.cechy_rozw[6]
        inte = self.cechy_pocz[7] + self.cechy_rozw[7]
        sw = self.cechy_pocz[8] + self.cechy_rozw[8]
        ogd = self.cechy_pocz[9] + self.cechy_rozw[9]
        return ww, us, s, wt, ini, zw, zr, inte, sw, ogd

    def umiej(self, um):  # Końcowe wartości umiejętności
        cecha = -100  # wskarze błedny zapis cechy
        if um[1] == 'WW':
            cecha = self.c_akt[0]
        elif um[1] == 'US':
            cecha = self.c_akt[1]
        elif um[1] == 'S':
            cecha = self.c_akt[2]
        elif um[1] == 'Wt':
            cecha = self.c_akt[3]
        elif um[1] == 'I':
            cecha = self.c_akt[4]
        elif um[1] == 'Zw':
            cecha = self.c_akt[5]
        elif um[1] == 'Zr':
            cecha = self.c_akt[6]
        elif um[1] == 'Int':
            cecha = self.c_akt[7]
        elif um[1] == 'SW':
            cecha = self.c_akt[8]
        elif um[1] == 'Ogd':
            cecha = self.c_akt[9]

        cale = cecha + um[2]
        return cecha, cale  # wart. cechy, całkowita wartość umiejętności

    @property
    def nazwy(self):
        """ Nazwy wywodzące się z klasy postaci. -> nazwy[nazwa_profesji, nazwa_poziomu_postaci]"""
        if self.plec is True:  # True to facet
            f = 0  # zmienna do pozycji listy nazwy
        else:
            f = 1  # zmienna do pozycji listy nazwy
        if self.prof is None:
            return '', ''
        else:
            return self.prof.nazwa[f], self.prof.Poz1.nazwa_poz[f]


#################################
#           Narzędzia           #
#################################

def czysc():  # oczyść ekran
    os.system('cls' if os.name == 'nt' else 'clear')
    print('')


def kosc(k=100):  # rzut kością
    rzut = randint(1, k)
    return rzut


def ktora_tab():
    if tab_gl:
        return tabela()
    else:
        return tab_um()


def akceptacja(pytanie=' Akceptujesz wynik rzutu? (T/N)', *args):
    if len(args) == 1:
        args = str(args[0])
    if len(args) == 0:
        args = list(args)
        args.append('t')
        args.append('n')
    while True:
        try:
            ktora_tab()
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
            tresc += f' {licz:02d}. {lista[licz - 1]:18}'
            if (licz % 4) == 0:  # stała określająca liczbę profesji w rzędzie pakietu
                tresc += '\n '
            licz += 1
        if (licz % 8) == 0 and licz <= len(lista):  # ostani element w wyświetlanym pakiecie.
            tresc += f' {licz:02d}. {lista[licz - 1]:18}'
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
    pl = p.plec
    # uwzględnić w tabelce

    czysc()

    print(f' ┌{line*92}┐')
    print(f' │ Imię: {plc:36} Rasa: {p.rasa:21} Płeć: {p.ple:13} │')
    print(f' ├{line * 92}┤')
    print(f' │ Klasa: {p.klasa_post:14} Profesja: {p.nazwy[0]:24} Poziom: {p.nazwy[1]:25} │')
    print(f' ├{line*12}┬────┬────┬────┬────┬────┬────┬────┬─────┬────┬─────┬{line*27}┤')
    print(f' │   Cechy    │ WW │ US │  S │ Wt │  I │ Zw │ Zr │ Int │ SW │ Ogd │       Doświadczenie       │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┬────────┬───────┤')
    print(f' │ Początkowa │ {cp[0]:02} │ {cp[1]:02d} │ {cp[2]:02d} │ {cp[3]:02d} │ {cp[4]:02d} │ {cp[5]:02d} │'
          f' {cp[6]:02d} │  {cp[7]:02d} │ {cp[8]:02d} │  {cp[9]:02d} │ Aktualne │ Wydane │ Razem │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┼────────┼───────┤')
    print(f' │ Rozwinięcia│ {cr[0]:02d} │ {cr[1]:02d} │ {cr[2]:02d} │ {cr[3]:02d} │ {cr[4]:02d} │ {cr[5]:02d} │'
          f' {cr[6]:02d} │  {cr[7]:02d} │ {cr[8]:02d} │  {cr[9]:02d} │   {p.pd:4d}   │  {p.pd_wyd:4d}  │'
          f'  {p.pd + p.pd_wyd:4d} │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┴┬───────┼───────┤')
    print(f' │  Aktualna  │ {ca[0]:02d} │ {ca[1]:02d} │ {ca[2]:02d} │ {ca[3]:02d} │ {ca[4]:02d} │ {ca[5]:02d} │'
          f' {ca[6]:02d} │  {ca[7]:02d} │ {ca[8]:02d} │  {ca[9]:02d} │ Żywotność │  {p.zyw:2}   │  {plc:4} │')
    print(f' ├────────────┴─┬──┴────┴────┴─┬──┴────┼────┴────┴────┬┴────┴────┬┴───┬──────┬┴───┬───┴──┬────┤')
    print(f' │ Pt. Boh.: {p.pb:2d} │ Pt. Det.: {p.pb:2d} │ PP: {p.pp:1} │ Pt. Szcz.: {p.pp:1} │ Szybkość │ {p.szyb:2}'
          f' │ Chód │ {p.szyb*2:2d} │ Bieg │ {p.szyb*4:2d} │')
    print(f' └──────────────┴──────────────┴───────┴──────────────┴──────────┴────┴──────┴────┴──────┴────┘')
    print(f' {wiad}')


def tab_um():
    line = '─'
    line2 = '═'
    sep = f' ├{line * 29}┼─────┼────┼──────┼──────┼┼{line * 29}┼─────┼────┼──────┼──────┤\n'
    um = p.umiej
    plc = ''

    # lista umiejętności podstawowych (na zewnątrz?)
    um_podst = [p.atle, p.bbia, p.bbij, p.char, p.dowo, p.haza, p.intu, p.jezk, p.mglo, p.nawi, p.odpo, p.opan, p.oswa,
                p.perc, p.plot, p.powo, p.prze, p.skrm, p.skrw, p.sztu, p.sprz, p.targ, p.unik, p.wios, p.wspi, p.wsak,
                p.wsga, p.wsko, p.wssp, p.zast]
    # lista umiejętności zaawansowanych (na zewnątrz?)
    um_zaaw = [p.bada, p.bdrz, p.bdwr, p.bkaw, p.bcep, p.bpar, p.bszr, p.bzpr, p.bzlu, p.bzku, p.bzmi, p.bzop, p.bzmw,
               p.bzps, p.bzex, p.jezg, p.jezp, p.jezs, p.jezw, p.jezy, p.jalb, p.jbit, p.jbrt, p.jelf, p.jest, p.jork,
               p.jkis, p.jjkr, p.jkrs, p.jkls, p.jniz, p.jmag, p.jnrs, p.jskv, p.jtil, p.jzlo, p.kugl, p.lecz, p.modl,
               p.mdud, p.muhr, p.mulu, p.muob, p.musk, p.mufl, p.opzw, p.otza, p.plyw, p.rapt, p.rbal, p.rgrb, p.rgot,
               p.rkal, p.rkow, p.rswi, p.rgar, p.rkam, p.rtru, p.scch, p.skoc, p.slow, p.swed, p.szlo, p.szwd, p.skrp,
               p.splm, p.smaq, p.smaz, p.smch, p.smdr, p.smgr, p.smgn, p.smhy, p.smsh, p.smul, p.tres, p.trop, p.wchm,
               p.wgeo, p.wher, p.whis, p.winz, p.wmag, p.wmed, p.wmet, p.wnau, p.wpra, p.wros, p.wteo, p.wwoj, p.wimp,
               p.wkrs, p.wycn, p.zpul, p.zwpa, p.zegl]
    # lista umiejętności do tabeli - kopia podstawowych
    um_tab = um_podst.copy()
    # pętla sprawdza kolejne um. zaawansowane, czy mają rozwinięcia
    for u in um_zaaw:
        if u[2] > 0:  # jeśli tak, to um. jest dodana do listy z tabeli
            um_tab.append(u)
    # nagłówek tabeli
    tab = f' ┌{line * 29}┬──────────┬──────┬──────┬┬{line * 29}┬──────────┬──────┬──────┐\n'
    tab += ' │         Umiejętność         │   Cecha  │ Roz. │ Suma │' \
           '│         Umiejętność         │   Cecha  │ Roz. │ Suma │\n'
    tab += f' ╞{line2 * 29}╪═════╤════╪══════╪══════╪╪{line2 * 29}╪═════╤════╪══════╪══════┤\n'
    # liczone są elementy listy i połowa stanowi wyznacznik długości tabeli
    dl = len(um_tab) // 2
    if len(um_tab) % 2 != 0:
        pk = dl + 1  # wartości dla prawej kolumny
    else:
        pk = dl
    # Pętla drukuje wewnętrzne wiersze
    for l in range(0, dl):
        tab += f' │ {um_tab[l][0]:27} │ {um_tab[l][1]:^3} │ {um(um_tab[l])[0]:^2} │ {um_tab[l][2]:^4} │' \
               f' {um(um_tab[l])[1]:^4} ││ {um_tab[l+pk][0]:27} │ {um_tab[l+pk][1]:^3} │ {um(um_tab[l+pk])[0]:^2} │' \
               f' {um_tab[l+pk][2]:^4} │ {um(um_tab[l+pk])[1]:^4} │\n'
        if l < dl - 1:
            tab += sep
    # Ostatni wiersz
    if len(um_tab) % 2 != 0:
        # Jeśli jest nieparzysta liczba elementów w ostatnim wierszu będzie pusta 'komórka'.
        tab += sep
        tab += f' │ {um_tab[l+1][0]:27} │ {um_tab[l+1][1]:^3} │ {um(um_tab[l+1])[0]:^2} │ {um_tab[l+1][2]:^4} │' \
               f' {um(um_tab[l+1])[1]:^4} ││ {plc:27} │ {plc:^3} │ {plc:^2} │ {plc:^4} │ {plc:^4} │\n'
    tab += f' └{line * 29}┴─────┴────┴──────┴──────┴┴{line * 29}┴─────┴────┴──────┴──────┘'

    czysc()
    print(tab)


#################################
#      Mechanika postaci        #
#################################
def los_rasy(rzut):  # Przydział razy postaci
    rasa_postaci = None
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


def rozw_um_start():  # przydział rozwinięć Umiejętności na start
    um_wybier = 1  # odliczanie umiejętności do rozwinięcia (2 razy po 3)
    rozw = 5  # wartość rozwinięcia w cyklu
    """ Połączyć z grupa_prof() - funkcją do wyboru profesji. Zewnętrzna część może być dekoratorem.
     Można stworzyć zmienne podmieniające profesje i umiejętności między sobę. 
     If może być użytu do wyboru wariantu z listą odpowiedzi dla akceptacji, czyba że akceptacja() radzi sobie z krotką
     """  # temp
    while True:
        if um_wybier == 4:
            um_wybier = 1
            rozw = 3
        licz = 1
        while licz <= len(um_start):
            tresc = f' Wybierz umiejętność ({um_wybier}/3), którą rozwiniesz o {rozw}:\n'
            while (licz % 6) != 0:  # stała określająca liczbę umiejętności w pakiecie
                if licz > len(um_start):  # jeśli nie ma więcej elementów w liście
                    tresc += '\n '
                    break
                tresc += f'  {licz:<2d}. {um_start[licz - 1][0]:29}'
                if (licz % 3) == 0:  # stała określająca liczbę umiejętności w rzędzie pakietu
                    tresc += '\n'
                licz += 1
            if (licz % 6) == 0 and licz <= len(um_start):  # ostani element w wyświetlanym pakiecie.
                tresc += f'  {licz:<2d}. {um_start[licz - 1][0]:29}\n  '
                licz += 1
            if len(um_start) > 6:
                tresc += '[N] - Następne'
            wybrany = akceptacja(tresc, str(licz - 6), str(licz - 5), str(licz - 4), str(licz - 3), str(licz - 2),
                                 str(licz - 1), 'n')
            if wybrany == 'n':  # nastęna grupa umiejętności
                if licz >= len(um_start):  # zapętla na końcu listy
                    licz = 1
                continue
            else:
                um_start[int(wybrany) - 1][2] += rozw  # dodaje rozwinięcie do umiejętności
                del um_start[int(wybrany) - 1]  # usuwa wybrany z listy
                um_wybier += 1
                break
        if um_wybier == 4 and rozw == 3:
            break


#####################################
#       Tworzenie postaci           #
#####################################
p = Postac()  # nowa tworzona postać

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

# Wartości cech i umiejętności  zależne od rasy
if p.rasa == rasy[0]:  # modyfikator rasowy, PP, PB, Szybkość
    mod_rasowy = mod_r_ludz
    p.pp = 2
    p.pb = 1
    p.szyb = 4
    p_dodat = 3
    um_start = [p.bbia, p.bzlu, p.char, p.dowo, p.jbrt, p.jjkr, p.opan, p.opzw, p.plot, p.targ, p.wimp, p.wycn]
    # miejsce na talenty
elif p.rasa == rasy[1]:
    mod_rasowy = mod_r_kras
    p.pb = 2
    p.szyb = 3
    p_dodat = 2
    um_start = [p.bbia, p.jkrs, p.odpo, p.opan, p.mglo, p.rapt, p.rbal, p.rgrb, p.rgot, p.rkal, p.rkow, p.rswi, p.rgar,
                p.rkam, p.wgeo, p.wkrs, p.wmet, p.wycn, p.wsga, p.zast]
    # miejsce na talenty
elif p.rasa == rasy[2]:
    mod_rasowy = mod_r_niz
    p.pb = 2
    p.szyb = 3
    p_dodat = 3
    um_start = [p.char, p.haza, p.intu, p.jniz, p.mglo, p.perc, p.rgot, p.skrp, p.skrm, p.skrw, p.targ, p.unik, p.wimp,
                p.zwpa]
    # miejsce na talenty
elif p.rasa == rasy[3]:
    mod_rasowy = mod_r_elf  # Wysoki
    p.szyb = 5
    p_dodat = 2
    um_start = [p.bbia, p.bzlu, p.dowo, p.jelf, p.mufl, p.muhr, p.mulu, p.muob, p.musk, p.nawi, p.opan, p.plyw, p.perc,
                p.wycn, p.wssp, p.zegl]
    # miejsce na talenty
elif p.rasa == rasy[4]:
    mod_rasowy = mod_r_elf  # Leśny
    p.szyb = 5
    p_dodat = 2
    um_start = [p.atle, p.bbia, p.bzlu, p.jelf, p.odpo, p.perc, p.skrw, p.sprz, p.trop, p.wspi, p.wssp, p.zast]
    # miejsce na talenty

#PŁEĆ
k2 = randint(0,1)

p.plec = k2

wiad = f'Wylosowano płeć: {p.ple}.'
wybor = akceptacja()
print(f'wybór: {wybor}, płeć: {p.plec}')
if wybor == "n":
    if p.plec == 0:
        p.plec = 1
    else:
        p.plec = 0

# PROFESJA
# 1. Rzut k 100
k100 = kosc()
# 2. Wybór listy na podstawie rasy
prof1 = profesje(k100, p.rasa)
wiad = f' PROFESJA Wynik: {k100:02d} - {prof1.nazwa[0]}                {gdzie()}'  # Wiad - zmienna tekstu wyświetlana w tabeli
if akceptacja() == 't':
    p.prof = prof1
    p.pd += 50  # pd za wybór pierwszego rzutu
else:  # wykonanie dodatkowych rzutów lub ręczny wybór
    k100b = kosc()
    k100c = kosc()
    prof2 = profesje(k100b, p.rasa)
    prof3 = profesje(k100c, p.rasa)
    wiad = ' PROFESJA'
    tekst = (f' Czy któryś z tych rzutów jest satysfakcjonujący?\n  {k100:02d}. {prof1.nazwa[0]:18}'
             f' {k100b:02d}. {prof2.nazwa[0]:18} {k100c:02d}. {prof3.nazwa[0]:18}\n  [R] - Ręczny wybór')
    reczny_wybor = akceptacja(tekst, str(k100), str(k100b), str(k100c), 'r')
    if reczny_wybor != 'r':  # wybrano jeden z rzutów
        prof_post = profesje(int(reczny_wybor), p.rasa)
        p.pd += 25
    else:  # funkcje ręcznego wyboru
        prof_rasowe()
        p.prof_post = grupa_prof()


# 5. /    Kolejne rzutu z innymi pd

# ATRYBUTY
# 1. Rzut 2k10 * 10 cech
wiad = f'                                      {gdzie()}'
cechy = ('WW', 'US', 'S', 'Wt', 'I', 'Zw', 'Zr', 'Int', 'SW', 'Ogd')
rzuty = []    # WW, US, S, Wt, In, Zw, Zr, Int, SW, Ogd

tekst = ''
tekst2 = ''
for i in range(0, 10):
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
            for i in range(0, 10):  # pyta o kolejne cechy i kaze przypisać jeden z wyników
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
            for i in range(0, 10):
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

for i in range(0, 10):  # Dodanie ostatecznych wartości cech do klasy Postac
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

# Rozwój cech na podstawie profesji - 5 pt. do podziału

# Rozwój umiejętności na podstawie rasy
"""Uwaga: jeśli przy Talencie lub Umiejętności widnieje oznaczenie „(Dowolne)”,oznacza to, że możesz wybrać
 jedną z opcji danego Talentu lub danej Umiejętności na tym poziomie Profesji. Zatem Wiedza (Dowolna) to może być
Wiedza (Geografa), Wiedza (Wiedza Ludowa), Wiedza (Magia) albo dowolny inny, podobnyprzykład. """
rozw_um_start()

# Talenty (też z rasy)

# Podsumowanie wyników.
wiad = ''  # temp

wybor = akceptacja(' Wyświetlić umiejętoności? [U] / [Q] - Koniec ', 'u', 'q')
while True:
    if wybor == 'u':
        tab_gl = False
        wybor = akceptacja(' Przełączanie widoku:\n  [U] - umiejętoności, [C] - Cechy, [Q] - Koniec ', 'u', 'q', 'c')
        continue
    elif wybor == 'c':
        tab_gl = True
        wybor = akceptacja(' Przełączanie widoku:\n  [U] - umiejętoności, [C] - Cechy, [Q] - Koniec ', 'u', 'q', 'c')
        continue
    else:
        break
