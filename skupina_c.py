"""
Preverjanje znanja je sestavljeno iz 4. nepovezanih nalog
Po vsaki nalogi imate podano funkcijo (npr. vaja_01_c_test()), ki testira delovanje vaše rešitve.
Če želite že sami preveriti pravilno delovanje odkomentirajte klic funkcije. Kdor testerjev ne želi uporabljati jih ne rabi.
***Pravilno opravljeni testi ne pomenijo da so vaše rešitve popolnoma pravilne, so pa dober indikator***
"""

"""
(2 točki)
Zapišite funkcijo vaja_01_c, ki prejme niz vrne besedo v nizu z največ števkami v besedi.
Besede so med sabo ločene s presledki sdf12345678.9,j_dfj2312 je torej ena sama 'beseda'
V primeru, da števk ne vsebuje vrnete prazni niz, če niz vsebuje več besed z istim številom
števk vrnete tisto, ki se je prva pojavila v besedilu

Primer: ('Danes je 11.november oziroma 11.11. lahko bi rekli tudi 11.11.2024 ali 11.november2024'') vrne 11.11.2024

"""

def vaja_01_c(niz):
    najvecje_stevilo_stevk = 0
    stevke = 0
    beseda = niz.split()
    for i in beseda:
        for j in i:
            if j.isdigit() :
                stevke += 1
        if stevke > najvecje_stevilo_stevk:
            najvecje_stevilo_stevk = stevke
            stevke = 0

    print(najvecje_stevilo_stevk)


    for i in beseda:
        for j in i:
            if j >= "0" and j <= "9":
                stevke +=1
            if najvecje_stevilo_stevk == stevke:
                return(i)
            stevke = 0

vaja_01_c("2500-500=2000")


def vaja_01_c_test():
    print(f"preverjanje naloge 01, skupina c")
    test_data = [
        'Danes je 11.november oziroma 11.11. lahko bi rekli tudi 11.11.2024 ali 11.november2024',
        'yxcvbnbvc aslfjbasf,fajbff cdascnka',
        '2500-500=2000',
        '2500 - 500 = 2000',
        '2500> 2000=True'
    ]
    results = [
        '11.11.2024',
        '',
        '2500-500=2000',
        '2500',
        '2500>'
    ]
    for i in range(len(test_data)):
        if vaja_01_c(test_data[i]) == results[i]:
            print(f"{i + 1}. primer je OK")

        else:
            print(f"{i + 1}. primer ni OK, vhodni podatki: {test_data[i]}, pričakovan rezultat: [{results[i]}]")

    print()


#vaja_01_c_test()


"""
(3,5 točk) Napišite funkcijo vaja_02_c ki prejme dva seznama. Prvi je seznam dijakov, drugi je 
gnezdeni seznam njihovih ocen (primer spodaj). Funkcija vrne seznam dijakov, urejen glede na njihove povprečne ocene, 
vendar brez dijakov, ki ne dosegajo minimalnega standarda (povprečna ocena 2), v primeru da imata dva 
dijaka enako povprečje ju uredite po abecedi.

Vrnjen seznam naj bo urejen najprej po povprečni oceni, nato pa po imenu, če je povprečna ocena enaka.

Primer: 
vaja_02_c(['Ana', 'Blaž', 'Cilka', 'David', 'Eva'], [[3, 4, 5, 1, 2, 2], [2, 1, 3, 3, 3], [4, 5, 5], [1, 1, 2], [1, 1, 3, 2]])
vrne ['Blaž', 'Ana', 'Cilka']
"""

def vaja_02_c_test():
    print(f"preverjanje naloge 02, skupina c")
    test_names = [
        ['Ana', 'Blaž', 'Cilka', 'David', 'Eva'],
        ['David', 'Cilka', 'Blaž', 'Ana', 'Eva'],
        ['David', 'Cilka', 'Blaž', 'Ana', 'Eva'],
        ['David', 'Cilka', 'Blaž', 'Ana', 'Eva'],
        ['Ana', 'Blaž', 'Cilka', 'David', 'Eva']
    ]
    test_grades = [
        [[3, 4, 5], [2, 1, 3], [4, 5, 5], [1, 1, 2], [1, 3, 2]],
        [[1],[1],[1],[1],[1]],
        [[2], [2], [2], [2], [2]],
        [[1], [2], [3], [4], [5]],
        [[3, 4, 5, 1, 2, 2], [2, 1, 3, 3, 3], [4, 5, 5], [1, 1, 2], [1, 1, 3, 2]],
    ]
    results = [
        ['Blaž', 'Eva', 'Ana', 'Cilka'],
        [],
        ['Ana', 'Blaž', 'Cilka', 'David', 'Eva'],
        ['Cilka', 'Blaž', 'Ana', 'Eva'],
        ['Blaž', 'Ana', 'Cilka']
    ]
    for i in range(len(test_names)):
        if vaja_02_c(test_names[i], test_grades[i]) == results[i]:
            print(f"{i + 1}. primer je OK")

        else:
            print(f"{i + 1}. primer ni OK, vhodni podatki: {test_names[i]}\n{test_grades[i]}\npričakovan rezultat: [{results[i]}]")

    print()

#vaja_02_c_test()


"""
(3 točke) Napišite funkcijo vaja_03_c, ki prejme seznam terk in vrne eno terko, ki vsebuje vse 
elemente iz seznama, vendar brez podvojenih elementov.
Primer: unikatna_terka([(1, 2, 3, 4), (3, 4, 5, 6), (5, 6, 7, 8)]) vrne (1, 2, 3, 4, 5, 6, 7, 8)
"""

def vaja_03_c_test():
    print(f"preverjanje naloge 03, skupina c")
    test_data = [
        [(1, 2, 3, 4), (3, 4, 5, 6), (5, 6, 7, 8)],
        [(1, 1, 1), (1, 1, 1)],
        [(1,), (1,), (1,)],
        [(1,)],
        [(-1, -2, -3), (1, ), (3, 1, 2)]
    ]
    results = [
        (1, 2, 3, 4, 5, 6, 7, 8),
        (1,),
        (1,),
        (1,),
        (-1, -2, -3, 1, 3, 2)
    ]

    for i in range(len(test_data)):
        if vaja_03_c(test_data[i]) == results[i]:
            print(f"{i + 1}. primer je OK")

        else:
            print(f"{i + 1}. primer ni OK, vhodni podatki: {test_data[i]}, pričakovan rezultat: [{results[i]}]")

    print()

#vaja_03_c_test()


"""
(3t) Napišite funkcijo, ki z enovrstično for zanko (list comprehension) ustvari n*n 
gnezden seznam (n elementov v n seznamih) napolnjen z številom 0. Dopišite kodo, ki 
zamenja del tega gnezdenega seznama zamenja z naključnimi števili med [1, 9] (obe števili vključeni).
Končni rezultat izpišite.

n=9
[[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 2, 7, 7, 9, 9]
[0, 0, 0, 0, 0, 8, 6, 3, 8]
[0, 0, 0, 0, 0, 0, 2, 8, 8]
[0, 0, 0, 0, 0, 0, 0, 7, 7]
[0, 0, 0, 0, 0, 0, 0, 0, 7]]

n=5
[[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 5, 4, 8]
[0, 0, 0, 3, 9]
[0, 0, 0, 0, 6]]

n=6
[[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 7, 9, 3]
[0, 0, 0, 0, 7, 6]
[0, 0, 0, 0, 0, 2]]
"""

#Ta vaja nima testa, svoje rešitve lahko primerjate z podanimi primeri
