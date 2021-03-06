import model


def izpis_igre(igra):
    tekst = (
        '===========================================\n\n'
        'Število preostalih poskusov: {stevilo_preostalih_poskusov} \n\n'
        '       {pravilni_del_gesla}\n\n'
        'Neuspeli poskusi: {neuspeli_poskusi}\n\n'
        '==========================================='
    ).format(
        stevilo_preostalih_poskusov=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla=igra.pravilni_del_gesla(),
        neuspeli_poskusi=igra.neuspeli_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        '===========================================\n\n'
        'Wipiiii, zmaga! Geslo je bilo: {geslo} \n\n'
        '===========================================\n\n'
    ).format(
        geslo = igra.geslo
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        'Booooo, nimaš pojma! Geslo je bilo: {geslo} \n\n'
    ).format(
        geslo=igra.geslo
    )
    return tekst



def izpis_napake():
    return '\n####### ugiba se ena črka naenkrat! ########\n\n'

def izpis_napake_znak():
    return '\n\######### brez posebnih znakov! ########\n\n'




def pozeni_vmesnik():
    

    igra = model.nova_igra()

    while True:
        #najprej izpisemo stanje, da vidimo, koliko črk je
        print(izpis_igre(igra))
        #čakamo na črko od uporabnika
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake())
        elif rezultat_ugiba == model.POSEBEN_ZNAK:
            print(izpis_napake_znak())
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            ponovni_zagon = input('Za ponovni zagon vpišite 1.').strip()
            if ponovni_zagon == "1":
                igra = model.nova_igra()
            else:
                break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            ponovni_zagon = input("Za ponovni zagon vpiši 1.\n").strip()
            if ponovni_zagon == "1":
                igra = model.nova_igra()
            else:
                break


#zaženi igro
pozeni_vmesnik()