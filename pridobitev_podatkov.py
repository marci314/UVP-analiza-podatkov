import yfinance as yf

def pridobi_podatke(imena_podjetji, začetek, konec):
    podatki = {}
    for ime in imena_podjetji:
        podatki_o_delnici = yf.download(ime, začetek, konec)
        podatki[ime] = podatki_o_delnici
    
    
    return podatki
        
        
