# """
# OSPR2 – vaje/praksa
# Vaja 08 - vaja iz terk (tuples)
#
# VSE NALOGE REŠUJTE S FUNKCIJAMI, KO ODDAJATE KODO NAJ BODO ZAKOMENTIRANA NAVODILA IN KLICI VAŠIH FUNKCIJ (FUNKCIJE SAME NAJ NE BODO ZAKOMENTIRANE)
#
# 1. naloga
# Napišite funkcijo sestej(slovar1, slovar2), ki združi dva slovarja, tako da pri enakih ključih vrednosti sešteje.
# Primer:
# Sestej({"a": 10, "b": 20, "c": 30}, {"a": 5, "b": 15, "d": 25}) vrne {"a": 15, "b": 35, "c": 30, "d": 25}

# 2. naloga
# Napišite funkcijo filtriranje(slovar), ki iz slovarja odstrani vse ključe, katerih vrednosti so manjše od 10.
# Primer:
# filtriranje({"a": 5, "b": 15, "c": 8, "d": 20}) vrne {"b": 15, "d": 20}


# 3. naloga
# Napišite funkcijo manjkajoci(slovar, seznam_kljucev), vrne seznam tistih ključev iz seznam_kljucev, ki manjkajo v slovarju.
# Primer:
# manjkajoci({"a": 1, "c": 3, "e": 5}, ["a", "b", "c", "d", "e"]) vrne ['b', 'd']


# 4. naloga
# Napišite funkcijo najdi_iste(seznam_slovarjev), ki vrne seznam vrednosti, ki so skupne vsem slovarjem iz seznam_slovarjev.
# Primer:
# najdi_iste([ {"a": 10, "b": 20, "c": 30}, {"b": 20, "c": 30, "d": 40}, {"a": 10, "c": 30, "e": 50}]) vrne [30]
#
# 5. naloga
# Napišite program za beleženje strank in kupljenih izdelkov. Podatki naj bodo shranjeni v slovarjih (en slovar za vsako osebo). Primer takšnega slovarja:
# oseba1 = {'ime': 'Miro', 'telefon': '041555666', 'kupljeni izdelki': ['žoga', 'barvice', 'balon']}
# Sestavite funkcijo podatek(oseba, lastnost), ki vrne podatek o lastnosti, ki ga ima v slovarju oseba. Funkcija naj vrne None, če se ta podatek v slovarju ne nahaja.
# Primer:
# podatek({'ime': 'Miro', 'telefon': '041555666', 'kupljeni izdelki': ['žoga', 'barvice', 'balon']}, 'telefon') vrne '041555666'
# podatek({'ime': 'Miro', 'telefon': '041555666', 'kupljeni izdelki': ['žoga', 'barvice', 'balon']}, 'naslov') vrne None
#
# 6. naloga
# Če za dve osebi poznamo podatek o neki lastnosti in sta ta podatka enaka, se ti osebi ujemata v tej lastnosti. Če za dve osebi poznamo podatka in sta podatka različna, pa pravimo, da se osebi razlikujeta v tej lastnosti.
# oseba1 = {'ime': 'Miro', 'priimek': 'Gorenjc'}
# oseba2 = {'ime': 'Mojca', 'priimek': 'Gorenjc', 'starost': 16}
# V zgornjem primeru se osebi ujemata v lastnosti 'priimek' in razlikujeta v lastnosti 'ime', v lastnosti 'starost' pa se niti ne ujemata niti ne razlikujeta.
# Napišite funkcijo ujemanje(oseba1, oseba2), ki vrne število lastnosti, v katerih se osebi oseba1 in oseba2 ujemata in število lastnosti, v katerih se razlikujeta. Rezultat naj bo seznam z dvema elementoma.
# Primer:
# ujemanje({'ime': 'Miro', 'priimek': 'Gorenjc'}, {'ime': 'Mojca', 'priimek': 'Gorenjc', 'starost': 16}) vrne [1, 1]



# 7. naloga
# Napišite funkcijo ista_oseba(oseba1, oseba2), ki vrne True, če sta oseba1 in oseba2 ista oseba, torej, če se razlikujeta v največ 1 lastnosti in ujemata v vsaj 4 lastnostih.
#
# 8.naloga
# Napišite funkcijo nakupovanje(seznam_zivil, kolicina), ki sestavi in vrne posodobljeni nakupovalni seznam, ki naj vsebuje vsa živila iz seznam_zivil, le da vse količine v njem pomnožene s faktorjem.
# Primer:
# nakupovanje({'mleko': 3, 'kruh': 4}, 2) vrne {'mleko': 6, 'kruh': 8}
#
# 9. naloga
# Napišite funkcijo kljuc_z_najvecjo_vrednostjo(slovar), ki vrne tisti ključ, ki ima največjo pripadajočo vrednost.
# Primer:
# kljuc_z_najvecjo_vrednostjo({'Anica': 83, 'Bojana': 95, 'Cveto': 84, 'Darja': 92}) vrne 'Bojana'

def kljuc_z_najvecjo_vrednostjo(slovar):
    najvecje = 0
    for kljuc, vrednost in slovar:
        if vrednost > najvecje:
            najvecje = vrednost

    for kljuc, vrednost in slovar:
        if vrednost == najvecje:
            print(kljuc)

kljuc_z_najvecjo_vrednostjo({'Anica': 83, 'Bojana': 95, 'Cveto': 84, 'Darja': 92})

# 10. naloga
# Napišite funkcijo urejen_kljuc_z_najvecjo_vrednostjo(slovar), ki vrne po abecedi urejen seznam vseh ključev z največjo vrednostjo. Če je slovar prazen, naj funkcija vrne prazen seznam.
#
# 11. naloga
# Napišite funkcijo ista_imena(slovar), ki prejme slovar, kjer se ime starša preslika v seznam vseh imen njegovih otrok. Funkcija naj vrne seznam tistih staršev, ki imajo otroka z istim imenom.
# Primer:
# ista_imena({'Miro' : ['Urban', 'Maja'],
# 'Jernej' : [],
# 'Ana' : ['Ana', 'Katja'],
# 'Kaja' : ['Tine'],
# 'Karlo' : ['Bine']})
# vrne ['Ana']
#
# 12. naloga
# Napišite funkcijo povprecna_ocena(slovar), ki vrne povprečno oceno vsakega dijaka.
# Primer:
# povprecna_ocena({
# "Anica": {"MAT": 91, "OSPR": 86},
# "Bojana": {"MAT": 73, "OSPR": 77},
# "Cveto": {"MAT": 89, "OSPR": 91}})
# vrne {"Anica": 88.5, "Bojana": 75.0, "Cveto": 90.0}
# """
