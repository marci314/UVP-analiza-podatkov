import matplotlib.pyplot as plt

def graf_cene(slovar_tabel, ime_stolpca):
    
    for ime, tabela in slovar_tabel.items():
        
        tabela[ime_stolpca].plot(label=f"{ime} {ime_stolpca}", figsize=(10, 5))
    
    
    plt.title("Gibanje cen delnic")
    plt.xlabel("Leto")
    plt.ylabel("Cena v $")
    plt.grid(True)
    plt.legend()
    plt.show()

def padec_meta(slovar_tabel, ime_stolpca):
    for ime, tabela in slovar_tabel.items():
        
        tabela[ime_stolpca].plot(label=f"{ime} {ime_stolpca}", figsize=(10, 5))
    zacetek = "2022-01-01"
    konec = "2022-03-01"
    plt.axvspan(zacetek, konec, color='red', alpha=0.2)
    plt.title("Gibanje cen delnic")
    plt.xlabel("Leto")
    plt.ylabel("Cena v $")
    plt.grid(True)
    plt.legend()
    plt.show()


def graf_volumna(slovar_tabel):
    
    
    for ime, tabela in slovar_tabel.items():
        
        tabela["Volumen"].plot(label=f"{ime} Volumen", figsize=(10, 5))
    
    
    plt.title("Gibanje volumna delnic")
    plt.xlabel("Leto")
    plt.ylabel("Volumen delnic")
    plt.grid(True)
    plt.legend()
    plt.ylim(bottom=0)
    plt.show()

def graf_vrednost(slovar_tabel):
    
    for ime, tabela in slovar_tabel.items():
        tabela["Vrednost_izmenjanega"].plot(label=f"{ime} Vrednost_izmenjanega", figsize=(10, 5))
    
    
    plt.title("Gibanje vrednosti podjetij")
    plt.xlabel("Leto")
    plt.ylabel("Vrednost izmenjanega v $")
    plt.grid(True)
    plt.legend()
    plt.ylim(bottom=0)
    plt.show()

import math

def dnevna_volatilnost(slovar_tabel):
    print("Dnevna volatilnost:")
    for ime, tabela in slovar_tabel.items():
        dnevna = tabela["Dnevni_donos"].std()
        print(f"{ime}: ", '{:.2f}'.format(dnevna), "%")

def graf_volatilnost(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        tabela["Dnevni_donos"].hist(bins=50, label=f"{ime}", alpha=0.5, figsize=(10, 5))
    plt.legend()
    plt.title("Porazdelitev dnevnih donosov")
    plt.xlabel("Dnevni donos v %")
    plt.ylabel("")
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.show()

    
import matplotlib.pyplot as plt

def izracunaj_donos(slovar_tabel):
    print("Kumulativni donos: ")
    for ime, tabela in slovar_tabel.items():
        donos = (tabela["Prilagojen_zaključni"][-1] - tabela["Prilagojen_zaključni"][0]) / tabela["Prilagojen_zaključni"][0]
        donos = donos*100
        donos = donos.round(2)
        print(f"{ime}: {donos}%")
    
import plotly.express as px

def interaktivni_kumulativni(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        tabela["Kumulativni_donos (v %)"] = ((1 + tabela["Dnevni_donos"]/100).cumprod())*100 - 100
        tabela["Ime_delnice"] = ime
        slovar_tabel[ime] = tabela
    
    for ime, tabela in slovar_tabel.items():
        graf = px.line(tabela,  
                y="Kumulativni_donos (v %)", 
                title="Dnevni kumulativni donos za " f"{ime}",
                labels={"Kumulativni_donos (v %)":"dnevni komulativni donos (%)", })
        graf.show()

def izracun_roi(slovar_tabel, ferkvenca=20):
    seznam_imen = []
    seznam_podatkov = []
    seznam_koncnih_zneskov = []
    skupna_vrednost_portfolija = 0
    print("Končni izid strategije:")
    for ime, tabela in slovar_tabel.items():
        st_kupljenih = 0
        investiran_denar = 0
        prodajna_cena = tabela["Zapiralni"][-1]
        
        
        for st_vrstice in range(len(tabela)):
            vrstica = tabela.iloc[st_vrstice]
            if st_vrstice % ferkvenca == 0:
                trenutna_cena = vrstica["Zapiralni"]
                st_kupljenih += 1
                investiran_denar += trenutna_cena
        

        print(" ")
        print("Delnice ", f"{ime}", " v lasti: ", st_kupljenih)
        print("Denar investiran v delnico ", f"{ime}: ", round(investiran_denar, 2),"$.")
        
        if investiran_denar >= st_kupljenih*prodajna_cena:
            izguba = st_kupljenih*prodajna_cena - investiran_denar
            print("Izguba: ", f"{round(izguba, 2)}$")
            seznam_podatkov.append(izguba)

        if investiran_denar < st_kupljenih*prodajna_cena:
            zasluzek = st_kupljenih*prodajna_cena - investiran_denar
            print("Zaslužek: ", f"{round(zasluzek, 2)}$")
            seznam_podatkov.append(zasluzek)
        
        print(" ")
        skupna_vrednost_portfolija += st_kupljenih*trenutna_cena
        seznam_imen.append(ime)
        seznam_koncnih_zneskov.append(st_kupljenih*trenutna_cena)

    plt.figure(figsize=(10, 8))
    seznam_barv = ["blue", "green", "red", "purple", "orange"]
    plt.bar(seznam_imen, seznam_podatkov, color=seznam_barv)
    plt.title("Profit/izguba")
    plt.xlabel("Delnice")
    plt.ylabel("Znesek v $")

    


        
def izracun_roi_portfelj(slovar_tabel, ferkvenca=20):
    seznam_imen = []
    seznam_podatkov = []
    seznam_koncnih_zneskov = []
    skupna_vrednost_portfolija = 0
    
    for ime, tabela in slovar_tabel.items():
        st_kupljenih = 0
        investiran_denar = 0
        prodajna_cena = tabela["Zapiralni"][-1]
        
        
        for st_vrstice in range(len(tabela)):
            vrstica = tabela.iloc[st_vrstice]
            if st_vrstice % ferkvenca == 0:
                trenutna_cena = vrstica["Zapiralni"]
                st_kupljenih += 1
                investiran_denar += trenutna_cena
        

        
        
        if investiran_denar >= st_kupljenih*prodajna_cena:
            izguba = st_kupljenih*prodajna_cena - investiran_denar
            
            seznam_podatkov.append(izguba)

        if investiran_denar < st_kupljenih*prodajna_cena:
            zasluzek = st_kupljenih*prodajna_cena - investiran_denar
            
            seznam_podatkov.append(zasluzek)
        
        
        skupna_vrednost_portfolija += st_kupljenih*trenutna_cena
        seznam_imen.append(ime)
        seznam_koncnih_zneskov.append(st_kupljenih*trenutna_cena)
    print("Vrednost portfelja:", f"{round(skupna_vrednost_portfolija, 2)}$")

    plt.figure(figsize=(10, 8))
    seznam_barv = ["blue", "green", "red", "purple", "orange"]
    
    

    plt.pie(seznam_koncnih_zneskov, labels=seznam_imen, autopct="%1.2f%%", colors=seznam_barv)
    plt.legend()
    plt.title("Portfelj")

