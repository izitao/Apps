from PIL import Image, ImageFilter

import requests

exit_tags = ['quit', 'q', 'STOP', 'stop', 'exit', 'no', 'No']

def cernobila(obrazek_url):
    """Cernobily filtr"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size
    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu

            if prumer > 127:
                obrazek.putpixel((x,y), (255, 255, 255)) #nastavi dany pixel na danou barvu
            else:
                obrazek.putpixel((x,y), (0, 0, 0))
            y += 1
        x += 1
    obrazek.show()

def svetle_pixely(obrazek_url):
    """Zvyrazni svetle pixely snimku"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size
    hranicni_hodnota = -1
    while hranicni_hodnota not in range(0,255+1):
        hranicni_hodnota = input('Nastav prahovou hodnotu barvy (0 az 255): ')
        if hranicni_hodnota.isdecimal():
            hranicni_hodnota = int(hranicni_hodnota)
    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu

            if prumer > hranicni_hodnota:
                obrazek.putpixel((x,y), (255, 255, 255)) #nastavi dany pixel na danou barvu

            y += 1
        x += 1
    obrazek.show()

def tmave_pixely(obrazek_url):
    """Zvyrazni tmave pixely snimku"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size
    hranicni_hodnota = -1
    while hranicni_hodnota not in range(0,255+1):
        hranicni_hodnota = input('Nastav prahovou hodnotu barvy (0 az 255): ')
        if hranicni_hodnota.isdecimal():
            hranicni_hodnota = int(hranicni_hodnota)
    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu

            if prumer < hranicni_hodnota:
                obrazek.putpixel((x,y), (0, 0, 0)) #nastavi dany pixel na danou barvu

            y += 1
        x += 1
    obrazek.show()

def obarvy_pixely(obrazek_url):
    """Obarvy vybrane pixely vybranou barvou"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size
    hranicni_hodnota = -1
    cervena_uzivatel = -1
    zelena_uzivatel = -1
    modra_uzivatel = -1

    while hranicni_hodnota not in range(0,255+1):
        hranicni_hodnota = input('Nastav prahovou hodnotu barvy (0 az 255): ')
        if hranicni_hodnota.isdecimal():
            hranicni_hodnota = int(hranicni_hodnota)

    while cervena_uzivatel not in range(0,255+1):
        cervena_uzivatel = input('Nastav intenzitu cervene barvy (0 az 255), na kterou chces menit: ')
        if cervena_uzivatel.isdecimal():
            cervena_uzivatel = int(cervena_uzivatel)

    while zelena_uzivatel not in range(0,255+1):
        zelena_uzivatel = input('Nastav intenzitu zelene barvy (0 az 255), na kterou chces menit: ')
        if zelena_uzivatel.isdecimal():
            zelena_uzivatel = int(zelena_uzivatel)

    while modra_uzivatel not in range(0,255+1):
        modra_uzivatel = input('Nastav intenzitu modre barvy (0 az 255), na kterou chces menit: ')
        if modra_uzivatel.isdecimal():
            modra_uzivatel = int(modra_uzivatel)

    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu

            if prumer > hranicni_hodnota:
                obrazek.putpixel((x,y), (cervena_uzivatel, zelena_uzivatel, modra_uzivatel)) #nastavi dany pixel na danou barvu

            y += 1
        x += 1
    obrazek.show()

def zmena_kontrastu(obrazek_url):
    """Zmena kontrastu obrazku"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size
    intenzita = -1
    while intenzita not in range(0,255+1):
        intenzita = input('Nastav intenzitu zmeny kontrastu: ')
        if intenzita.isdecimal():
            intenzita = int(intenzita)
    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu

            if prumer > 127:
                obrazek.putpixel((x,y), (r+intenzita, g+intenzita, b+intenzita)) #nastavi dany pixel na danou barvu
            else:
                obrazek.putpixel((x,y), (r-intenzita, g-intenzita, b-intenzita))

            y += 1
        x += 1
    obrazek.show()

def diapozitiv(obrazek_url):
    """Diapozitiv obrazku"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size

    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu
            obrazek.putpixel((x,y), (255-prumer, 255-prumer, 255-prumer))

            y += 1
        x += 1
    obrazek.show()

def prohozeni_barev(obrazek_url):
    """Vzajemne prohozeni barev jednotlivych pixelu"""
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    sirka, vyska = obrazek.size

    x = 0

    while x < sirka:
        y = 0
        while y < vyska:
            #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y)) #ziska hodnotu barev daneho pixelu
            prumer = int((r+g+b)/3) #prumerna svitivost bodu
            obrazek.putpixel((x,y), (g, b, r))

            y += 1
        x += 1
    obrazek.show()

def rozmazani(obrazek_url):
    """Rozamzani obrazku"""
    from PIL.ImageFilter import (BLUR)
    obrazek = Image.open(requests.get(obrazek_url, stream=True).raw)
    obrazek = obrazek.filter(BLUR)
    obrazek.show()

while True:
    obrazek = input('Zadej adresu obrazku: ')
    if obrazek in exit_tags:
        break

    filtr = int(input('Zvol filtr: \n'
                      '\t1.cernobila \n'
                      '\t2.Zvyrazni svetle pixely \n'
                      '\t3.Zvyrazni tmave pixely \n'
                      '\t4.Obarvy pixely \n'
                      '\t5.Zmena kontrastu \n'
                      '\t6.Diapozitiv \n'
                      '\t7.Prohozeni barev \n'
                      '\t8.Rozmazani obrazku \n'))
    if filtr in exit_tags:
        break
    elif filtr == 1:
        cernobila(obrazek)
    elif filtr == 2:
        svetle_pixely(obrazek)
    elif filtr == 3:
        tmave_pixely(obrazek)
    elif filtr == 4:
        obarvy_pixely(obrazek)
    elif filtr == 5:
        zmena_kontrastu(obrazek)
    elif filtr == 6:
        diapozitiv(obrazek)
    elif filtr == 7:
        prohozeni_barev(obrazek)
    elif filtr == 8:
        rozmazani(obrazek)

    pokracovat = input('Pokracovat? ')
    if pokracovat in exit_tags:
        break