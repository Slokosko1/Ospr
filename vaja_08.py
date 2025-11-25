# """
# OSPR2 – vaje/praksa
# Vaja 08 - vaja iz množic (set)
#
# VSE NALOGE REŠUJTE S FUNKCIJAMI, KO ODDAJATE KODO NAJ BODO ZAKOMENTIRANA NAVODILA IN KLICI VAŠIH FUNKCIJ (FUNKCIJE SAME NAJ NE BODO ZAKOMENTIRANE)
#
#
# 1. naloga
# Napišite funkcijo ustvari, ki ustvari in vrne množico z »n« naključnimi števili v razponu [a,b]. Spremenljivke »n, a in b« so parametri funkcije.
# Primer: ustvari(3, 1, 15) -> {12, 7, 4}
import random
def ustvari(n, a, b):
    mn = set()
    for i in range(n):
        mn.add(random.randint(a,b))
    print(mn)

#ustvari(3, 1, 15)


# 2.naloga
# Napišite funkcijo dodaj_element s parametri »mnozica« in »vrednost«, vrne naj množico, ki ji je bil dodan argument »vrednost«.
#  Primer: dodaj_element({1, 2, 3}, 4) -> {1, 2, 3, 4}

def dodaj_element(mnozica, vrednost):
    mnozica.add(vrednost)
    print(mnozica)

#dodaj_element({1, 2, 3}, 4)


# 3. naloga
# Napišite funkcijo zdruzi_mnozice, ki prejme poljubno mnogo mnozic in jih zdruzi.
# Primer: zdruzi_mnozice({1,2,3}, {2}, {123}) -> {1, 2, 3, 123}

def zdruzi_mnozice(*mnozice):
    nov_mn = set()
    for i in mnozice:
        for j in i:
            nov_mn.add(j)
    print(nov_mn)

#zdruzi_mnozice({1,2,3}, {2}, {123})


# 4. naloga
# Napišite funkcijo odstrani, ki ima kot parametra definirani spremenljivki mnozica in *elementi. Iz prejete mnozice odstranite vse elemente in vrnite mnozico. Uporabite discard.
# Primer: odstrani({1,2,3,4,5,6,7}, 1, 3, 4) -> {2, 4, 6, 7}

def odstrani(mnozica, *elementi):
    for i in elementi:
        mnozica.discard(i)
    print(mnozica)

#odstrani({1,2,3,4,5,6,7}, 1, 3, 4)


# 5.naloga
# Napiši funkcijo kolikokrat_ponovi, ki prejme eno vrednost in poljubno mnogo množic. Funkcija prešteje v koliko množicah se pojavi iskan element in to število vrne.
# Kolikokrat_ponovi(2, {1,23,3}, {2, 3, 4, 5}, {1, 2}) -> 2

def kolikokrat_ponovi(vrednost, *mnozice):
    st=0
    for i in mnozice:
        for j in i:
            if j == vrednost:
                st+=1
    print(st)

#kolikokrat_ponovi(2, {1,23,3}, {2, 3, 4, 5}, {1, 2})


# 6. naloga
# Napišite funkcijo razlika_dolzine, ki prejme poljubno mnogo množic. Funkcija vrne razliko med skupno dolžino vseh seznamov in dolžino unikatnih elementov vseh seznamov.

# 7. naloga
# Napišite funkcijo, ki prejme poljubno število množic in vrne njihov presek.

def presek(*mnozice):
    presek =
    print(set.intersection(*mnozice))

#presek({1,23,3}, {1, 2, 3, 4, 5}, {1, 2})


# 8. naloga
# Napišite funkcijo, ki prejme poljubno število množic in vrne njihovo razliko.

def razlika(*mnozice):
    rezultat = mnozice[0].copy()
    for m in mnozice[1:]:
        rezultat = rezultat - m
    return rezultat

print(razlika({1, 2, 3, 4}, {2, 3}, {1}))



# 9. naloga
# Napišite funkcijo podmnozica, ki prejme poljubno število množic in prešteje kolikokrat je množica podmnožica neke druge množice (vse kombinacije)
#
#
# 10. naloga
# Napišite funkcijo podvojeni, ki prejme poljubno mnogo seznamov in/ali terk. Vrnite dve množici, prva naj vsebuje elemente, ki so se v terkah/seznamih pojavili natančno enkrat, drugi naj vsebuje vse elemente, ki so se pojavili več kot enkrat.
#
# 11. naloga
# Ustvarite zamrznjeno množico (frozenset), preverite katere operacije lahko izvajate nad njo.
#
# 12. naloga
# Napišite funkcijo, ki prejme množico in njeno vsebino izpiše v naraščajočem vrstnem redu.
# """
#
