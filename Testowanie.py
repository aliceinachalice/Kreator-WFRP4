####################### Niezbędne elementy ##############################
from random import randint
rasy = ('Człowiek', 'Krasnolud', 'Niziołek', 'Wysoki elf', 'Leśny elf')


def kosc(k=100):  # rzut kością
    rzut = randint(1, k)
    return rzut


def akceptacja(pytanie='Akceptujesz wynik rzutu? (T/N)', *args):
    # długość ciągu
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


####################### Zmienne  do testów ##############################
rasa = rasy[0]
pd = 0
######################### Testowany kod #################################


class Postac:
    def __init__(self, rasa):
        self.rasa = rasa


'''
┌─┬┴┼┤│└┘├┐
 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 
 ┌───────────────────────────────────────────────────────────────────────────────────────┐
 │ Imię:                                    Rasa:                        Płeć: Mężczyzna │  
 ├───────────────────────────────────────────────────────────────────────────────────────┤
 │ Klasa:               Profesja:                       Poziom:                          │
 ├────────────┬────┬────┬────┬────┬────┬────┬─────┬────┬─────┬───────────────────────────┤
 │   Cechy    │ WW │ US │  S │ Wt │  I │ Zw │ Int │ SW │ Ogd │       Doświadczenie       │
 ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┬────────┬───────┤
 │ Początkowa │ 99 │ 99 │ 99 │ 99 │ 99 │ 99 │  99 │ 99 │  99 │ Aktualne │ Wydane │ Razem │
 ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┼────────┼───────┤
 │ Aktualna   │ 99 │ 99 │ 99 │ 99 │ 99 │ 99 │  99 │ 99 │  99 │          │        │       │ 
 ├────────────┴─┬──┴────┴────┴─┬──┴────┴────┴────┬┴────┴────┬┴───┬──────┼────┬───┴──┬────┤
 │ Pt. Boh.: 99 │ Pt. Det.: 99 │ PP: 99  PS: 99  │ Szybkość │ 99 │ Chód │ 99 │ Bieg │ 99 │
 └──────────────┴──────────────┴─────────────────┴──────────┴────┴──────┴────┴──────┴────┘
'''


def tabela():
    # Tabela ma szerokość 99 znaków plus spacja na początku jako odstęp od krawędzi okna.
    line = '─'
    plc = ''  # paceholder
    plc2 = 0  # paceholder
    plc3 = [15,16,'']
    fd = '02d'

    #try:

    print(' 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789')  # temp
    print(f' ┌{line*87}┐')
    print(f' │ Imię: {plc:35} Rasa: {rasa:21} Płeć: {plc:9} │')
    print(f' ├{line * 87}┤')
    print(f' │ Klasa: {plc:12} Profesja: {plc:22} Poziom: {plc:24} │')
    print(f' ├{line*12}┬────┬────┬────┬────┬────┬────┬─────┬────┬─────┬{line*27}┤')
    print(f' │   Cechy    │ WW │ US │  S │ Wt │  I │ Zw │ Int │ SW │ Ogd │       Doświadczenie       │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┬────────┬───────┤')
    print(f' │ Początkowa │ {plc2:02} │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │  {plc2:02d} │'
          f' {plc2:02d} │  {plc2:02d} │ Aktualne │ Wydane │ Razem │')
    print(f' ├────────────┼────┼────┼────┼────┼────┼────┼─────┼────┼─────┼──────────┼────────┼───────┤')
    print(f' │  Aktualna  │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │ {plc2:02d} │  {plc2:02d} │'
          f' {plc2:02d} │  {plc2:02d} │   {plc2:04d}   │  {plc2:04d}  │  {plc2:04d} │')
    print(f' ├────────────┴─┬──┴────┴────┴─┬──┴────┴────┴────┬┴────┴────┬┴───┬──────┼────┬───┴──┬────┤')
    print(f' │ Pt. Boh.: {plc2:02d} │ Pt. Det.: {plc2:02d} │ PP: {plc2:02d}  PS: {plc2:02d}  │ Szybkość │ {plc3[2]:02}'
          f' │ Chód │ {plc3[1]:02d} │ Bieg │ {plc3[0]:{fd}} │')
    print(f' └──────────────┴──────────────┴─────────────────┴──────────┴────┴──────┴────┴──────┴────┘')
    #except ValueError:
       # fd = 2

    #except IndexError:
       # pass



test = "        "
print(len(test))
tabela()
"""
import Losowanie as Los
ile = maks = 0
nazwy = []
for i in range(0, len(Los.klasa)):
    for j in range(0, len(Los.klasa[i])):
        dlug = len(Los.klasa[i][j])
        if dlug == maks:
            ile += 1
            nazwy.append(Los.klasa[i][j])
        if dlug > maks:
            ile = 1
            nazwy = []
            maks = dlug
            nazwa = Los.klasa[i][j]
            nazwy.append(Los.klasa[i][j])


print('------------------------------------------------------------------------------')
print(f' Najdłuższa nazwa profesji to {nazwa} i ma {maks} znaków. Jest łączne {ile} profesji tej długości.\n'
      f' Są to: {nazwy}')
"""