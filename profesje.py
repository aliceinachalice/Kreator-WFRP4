"""Uwaga: jeśli przy Talencie lub Umiejętności widnieje oznaczenie „(Dowolne)”,oznacza to, że możesz wybrać
 jedną z opcji danego Talentu lub danej Umiejętności na tym poziomie Profesji. Zatem Wiedza (Dowolna) to może być
Wiedza (Geografa), Wiedza (Wiedza Ludowa), Wiedza (Magia) albo dowolny inny, podobnyprzykład. """


# UCZENI
class Aptekarka:
    nazwa = ['Aptekarz', 'Aptekarka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Uczeń Aptekarza', 'Uczennica Aptekarki']
        status = 'Brąz 3'
        # umiej = [jkls, lecz, mglo, rapt, rtru, wchm, wmed, wros]
        # Język (Klasyczny), Leczenie, Mocna Głowa, Rzemiosło (Aptekarstwo), Rzemiosło (Truciciel), Wiedza (Chemia),
        # Wiedza (Medycyna), Wiedza (Rośliny)
        cechy = ['Wt', 'Zr', 'Int']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Czytanie/Pisanie, Etykieta (Uczeni), Przyrządzanie, Mikstur, Wytwórca (Aptekarz)

    class Poz2:
        nazwa_poz = ['Aptekarz', 'Aptekarka']
        status = 'Srebro 1'
        # umiej = [char, jgil, perc, plot, targ, wnau]
        # Charyzma, Język (Gildii), Percepcja, Plotkowanie, Targowanie, Wiedza (Nauka)
        cechy = ['Ogd']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Aptekarz, Etykieta (Członkowie Cechu), Przestępca, Żyłka Handlowa

    class Poz3:
        nazwa_poz = ['Farmaceuta', 'Farmaceutka']
        status = 'Srebro 3'
        # umiej = [bada, dowo, intu, scch]  # Badania Naukowe, Dowodzenie, Intuicja, Sekretne Znaki (Cechu)

        cechy = ['I']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Błyskotliwość, Mistrz Rzemiosła (Aptekarz), Mól Książkowy, Odporny na (Trucizny)

    class Poz4:
        nazwa_poz = ['Mistrz Aptekarstwa', 'Mistrzyni Aptekarstwa']
        status = 'Złoto 1'
        # umiej = [jezk, zast]  # Jeździectwo (Konie), Zastraszanie
        cechy = ['SW']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Mistrz Rzemiosła (Truciciel), Wyczulony Zmysł (Smak), Zimna Krew, Znawca (Aptekarstwo)


class Czarodziej:
    nazwa = ['Czarodziej', 'Czarodziejka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Uczeń Czarodzieja', 'Uczennica Czarodziejki']
        status = 'Brąz 3'
        # umiej = [bbia, bdrz, intu, jmag, perc, splm, smaq, smaz, smch, smdr, smgr, smgn, smhy, smsh, smul, unik, wmag]
        # Broń Biała (Podstawowa), Broń Biała (Drzewcowa), Intuicja, Język (Magiczny),Percepcja,
        # Splatanie Magii (Dowolny Kolor),Unik, Wiedza (Magia)
        cechy = ['WW', 'Int', 'SW']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Czytanie/Pisanie, Magia Prosta, Percepcja, Magiczna, Zmysł Magii

    class Poz2:
        nazwa_poz = ['Czarodziej', 'Czarodziejka']
        status = 'Srebro 3'
        # umiej = [char, jbit, opan, plot, zast, jezy, jalb, jbit, jbrt, jelf, jest, jork, jkis, jjkr, jkrs, jkls, jniz,
        #        jmag, jnrs, jskv, jtil, jzlo]
        # Charyzma, Język (Bitewny), Język (Dowolny), Opanowanie, Plotkowanie, Zastraszanie
        cechy = ['Zw']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Magia Tajemna (Dowolna Tradycja), Rozpoznanie Artefaktu, Ruchliwe Dłonie, Szósty Zmysł

    class Poz3:
        nazwa_poz = ['Mistrz Magii', 'Mistrzyni Magii']
        status = 'Złoto 1'
        # umiej = [jezd, opzw, wwoj, wycn]  # Jeździectwo (Konie), Opieka nad Zwierzętami, Wiedza (Wojna), Wycena

        cechy = ['I']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Dwie Bronie, Groźny, Precyzyjne Inkantowanie, Wykrywanie Magii

    class Poz4:
        nazwa_poz = ['Arcymag', 'Arcymagini']
        status = 'Złoto 2'
        # umiej = [jezy, jalb, jbit, jbrt, jelf, jest, jork, jkis, jjkr, jkrs, jkls, jniz, jmag, jnrs, jskv, jtil, jgil,
        #          jzlo, wchm, wgeo, wher, whis, winz, wmag, wmed, wmet, wnau, wpra, wros, wteo, wwoj, wimp, wkrs]
        # Język (Dowolny), Wiedza (Dowolna)
        cechy = ['Ogd']  # WW, US, S, Wt, I, Zw, Zr, Int, SW, Ogd

        # talenty  # Mag Bitewny, Straszny, Zmysł Bitewny, Żelazna Wola


class Inzynier:
    nazwa = ['Inżynier', 'Inżynierka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Student Inżynierii', 'Studentka Inżynierii']


class Kaplan:
    nazwa = ['Kapłan', 'Kapłanka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Kleryk', 'Kleryczka']


class Medyczka:
    nazwa = ['Medyk', 'Medyczka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Student Medycyny', 'Studentka Medycyny']


class Mniszka:
    nazwa = ['Mnich', 'Mniszka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Nowicjusz', 'Nowicjuszka']


class Prawniczka:
    nazwa = ['Prawnik', 'Prawniczka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Student Prawa', 'Studentka Prawa']


class Uczony:
    nazwa = ['Uczony', 'Uczona']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Student', 'Studentka']


# MIESZCZANIE
class Agitator:
    nazwa = ['Agitator', 'Agitatorka']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Pamﬂecista', 'Pamﬂecistka']


class Kupiec:
    nazwa = ['Kupiec', 'Kupiec']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Handlarz', 'Handlarka']


class Mieszczka:
    nazwa = ['Mieszczanin', 'Mieszczka']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Przekupień', 'Przekupka']


class Rzemieslniczka:
    nazwa = ['Rzemieślnik', 'Rzemieślniczka']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Czeladnik', 'Czeladniczka']


class Straznik:
    nazwa = ['Strażnik', 'Strażniczka']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Rekrut Straży', 'Rekrutka Straży']


class Szczurolap:
    nazwa = ['Szczurołap', 'Szczurołapka']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Uczeń Szczurołapa', 'Uczennica Szczurołapki']


class Sledczy:
    nazwa = ['Śledczy', 'Śledcza']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Szpicel', 'Szpicel']


class Zebrak:
    nazwa = ['Żebrak', 'Żebraczka']
    klasa = 'Mieszczanie'

    class Poz1:
        nazwa_poz = ['Biedak', 'Biedaczka']


# DWORZANIE
class Artystka:
    nazwa = ['Artysta', 'Artystka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Uczeń Artysty', 'Uczennica Artystki']


class Doradca:
    nazwa = ['Doradca', 'Doradczyni']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Asystent', 'Asystentka']


class Posel:
    nazwa = ['Poseł', 'Posłanka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Herold', 'Herold']


class Namiestnik:
    nazwa = ['Namiestnik', 'Namiestniczka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Nadzorca', ' Nadzorczyni']


class Sluzaca:
    nazwa = ['Służący', 'Służąca']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Posługacz', 'Posługaczka']


class Szlachcic:
    nazwa = ['Szlachcic', 'Szlachcianka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Dziedzic', 'Dziedziczka']


class Szpieg:
    nazwa = ['Szpieg', 'Szpieg']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Informator', 'Informatorka']


class Zwadzca:
    nazwa = ['Zwadźca', 'Zwadźczyni']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Szermierz', 'Szermierka']


# POSPÓLSTWO
class Chlopka:
    nazwa = ['Chłop', 'Chłopka']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Wyrobnik', 'Wyrobnica']


class Gornik:
    nazwa = ['Górnik', 'Górniczka']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Poszukiwacz', ' Poszukiwaczka']


class Guslarz:
    nazwa = ['Guślarz', 'Guślarka']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Uczeń Guślarza', 'Uczennica Guślarrki']


class Lowczyni:
    nazwa = ['Łowca', 'Łowczyni']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Traper', 'Traperka']


class Mistyczka:
    nazwa = ['Mistyk', 'Mistyczka']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Wróżbiarz', 'Wróżbiarka']


class Zarzadca:
    nazwa = ['Zarządca', 'Zarządczyni']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Poborca Podatków', 'Poborczyni Podatków']


class Zielarka:
    nazwa = ['Zielarz', 'Zielarka']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Zbieracz Ziół', 'Zbieraczka Ziół']


class Zwiadowca:
    nazwa = ['Zwiadowca', 'Zwiadowczyni']
    klasa = 'Pospólstwo'

    class Poz1:
        nazwa_poz = ['Przewodnik', 'Przewodniczka']


# WĘDROWCY
class Biczownik:
    nazwa = ['Biczownik', 'Biczowniczka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Gorliwiec', 'Gorliwiec']


class Domokrazca:
    nazwa = ['Domokrążca', 'Domokrążca']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Powsinoga', ' Powsinoga']


class Kuglarka:
    nazwa = ['Kuglarz', 'Kuglarka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Muzykant', 'Muzykantka']


class LowcaCzarownic:
    nazwa = ['Łowca Czarownic', 'Łowczyni Czarownic']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Oprawca', 'Oprawczyni']


class LowczyniNagrod:
    nazwa = ['Łowca Nagród', 'Łowczyni Nagród']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Pogromczyni Złodziei', 'Pogromca Złodziei']


class Poslaniec:
    nazwa = ['Posłaniec', 'Posłanniczka']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Goniec', 'Goniec']


class StrazniczkaDrog:
    nazwa = ['Strażnik Dróg', 'Strażniczka Dróg']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Mytnik', 'Mytniczka']


class Woznica:
    nazwa = ['Woźnica', 'Woźnica']
    klasa = 'Uczeni'

    class Poz1:
        nazwa_poz = ['Foryś', 'Foryś']


# WODNIACY
class Doker:
    nazwa = ['Doker', 'Dokerka']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Pomocnik Dokera', ' Pomocniczka Dokerki']


class Flisak:
    nazwa = ['Flisak', 'Flisaczka']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Rybak', 'Rybaczka']


class PilotkaRzeczna:
    nazwa = ['Pilot Rzeczny', 'Pilotka Rzeczna']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Przewodnik Rzeczny', 'Przewodniczka Rzeczna']


class PiratRzeczny:
    nazwa = ['Pirat Rzeczny', 'Piratka Rzeczna']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Szabrownik', ' Szabrowniczka']


class Przemytniczka:
    nazwa = ['Przemytnik', 'Przemytniczka']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Szmugler Rzeczny', 'Szmuglerka Rzeczna']


class Przewoznik:
    nazwa = ['Przewoźnik', 'Przewoźniczka']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Chłopiec Pokładowy', 'Dziewka Pokładowa']


class StraznikRzeczny:
    nazwa = ['Strażnik Rzeczny', 'Strażniczka Rzeczna']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Rekrut Rzeczny', 'Rekrutka Rzeczna']


class Zeglarz:
    nazwa = ['Żeglarz', 'Żeglarka']
    klasa = 'Wodniacy'

    class Poz1:
        nazwa_poz = ['Szczur Lądowy', 'Szczurzyca Lądowa']


# ŁOTRY
class Banita:
    nazwa = ['Banita', 'Banitka']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Zbój', 'Zbójczyni']


class Czarownica:
    nazwa = ['Czarownik', 'Czarownica']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Szeptun', 'Szeptucha']


class HienaCmentarna:
    nazwa = ['Hiena Cmentarna', 'Hiena Cmentarna']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Porywaczk Zwłok', 'Porywaczka Zwłok']


class Paser:
    nazwa = ['Paser', 'Paserka']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Pośrednik', 'Pośredniczka']


class Rajfur:
    nazwa = ['Rajfur', 'Rajfurka']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Naganiacz', 'Naganiaczka']


class Rekietierka:
    nazwa = ['Rekietier', 'Rekietierka']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Zakapior', 'Zakapiorka']


class Szarlatan:
    nazwa = ['Szarlatan', 'Szarlatanka']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Kanciarz', 'Kanciarka']


class Zlodziej:
    nazwa = ['Złodziej', 'Złodziejka']
    klasa = 'Łotry'

    class Poz1:
        nazwa_poz = ['Bandzior', 'Bandziorka']


# WOJOWNICY
class Gladiator:
    nazwa = ['Gladiator', 'Gladiatorka']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Pięściarz', 'Pięściarka']


class KaplanBitewny:
    nazwa = ['Kapłan Bitewny', 'Kapłanka Bitewna']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Nowicjusz Kap. Bitewnych', 'Nowicjuszka Kap. Bitewnych']


class Kawalerzysta:
    nazwa = ['Kawalerzysta', 'Kawalerzystka']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Jeździec', ' Jeździec']


class Ochroniarz:
    nazwa = ['Ochroniarz', 'Ochroniarka']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Stróż', 'Stróż']


class Oprych:
    nazwa = ['Oprych', 'Opryszka']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Tani Drań', 'Tani Drań']


class Rycerz:
    nazwa = ['Rycerz', 'Rycerka']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Giermek', 'Giermek']


class Zabojca:
    nazwa = ['Zabójca', 'Zabójczyni']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Zabójca Trolli', 'Zabójczyni Trolli']


class Zolnierz:
    nazwa = ['Żołnierz', 'Żołnierka']
    klasa = 'Wojownicy'

    class Poz1:
        nazwa_poz = ['Rekrut', 'Rekrutka']
