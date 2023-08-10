import pandas as pd

def dodaj_dnevni_donos(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        tabela["Dnevni_donos"] = ((tabela["Zapiralni"]/tabela["Zapiralni"].shift(1)) - 1)*100
        slovar_tabel[ime] = tabela
    return slovar_tabel

def dodaj_dnevni_razpon(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        nov_stolpec = tabela["Najnižji"].astype(str) + " " + "-" + " " + tabela["Najvišji"].astype(str)
        tabela["Dnevni_razpon"] = nov_stolpec
        slovar_tabel[ime] = tabela
    return slovar_tabel

def povprecje(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        nov_stolpec = ((tabela["Najnižji"] + tabela["Najvišji"])/2).round(3)
        tabela["Povprečni"] = nov_stolpec
        slovar_tabel[ime] = tabela
    return slovar_tabel

def vrednost_izmenjanega(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        nov_stolpec = (tabela["Povprečni"]*tabela["Volumen"]).round(3)
        tabela["Vrednost_izmenjanega"] = nov_stolpec
        slovar_tabel[ime] = tabela
    return slovar_tabel


def drsece_povprecje(slovar_tabel, dni):
    for ime, tabela in slovar_tabel.items():
        tabela[f"Drseče_povprečje_{dni}"] = tabela["Prilagojen_zaključni"].rolling(dni).mean()
        slovar_tabel[ime] = tabela
    return slovar_tabel

def prevedi(slovar_tabel):
    for ime, tabela in slovar_tabel.items():
        tabela.rename(columns={
            "Date": "Datum",
            "Open": "Odpiralni",
            "High": "Najvišji",
            "Low": "Najnižji",
            "Close": "Zapiralni",
            "Adj Close": "Prilagojen_zaključni",
            "Volume": "Volumen"
        }, inplace=True)
    
    
    return slovar_tabel

def dopolni(slovar_s_podatki):
    for ime_delnice, tabela in slovar_s_podatki.items():
        slovar_s_podatki[ime_delnice] = tabela.ffill()
        stolpci_zaokr = [col for col in tabela.columns if col != "Date"]
        tabela[stolpci_zaokr] = tabela[stolpci_zaokr].round(3)
        slovar_s_podatki[ime_delnice] = tabela
    
    return slovar_s_podatki

import os



def shrani_podatke(slovar_tabel):
    os.makedirs("data", exist_ok=True)
    for ime, tabela in slovar_tabel.items():
        file_name = f"{ime}.csv"
        tabela.to_csv("data/" + file_name)
