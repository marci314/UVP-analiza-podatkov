# ANALIZA IN VIZUALIZACIJA FINANČNIH PODATKOV O DELNICAH 

Avtor: Marcel Blagotinšek

Pri predmetu Uvod v programiranje sem pripravil projektno nalogo iz analize podatkov. V nalogi izberem delnice velikih ameriških podjetji, uvozim ter izluščim podatke, ki me zanimajo za nadaljno analizo, tabele shranim (datoteke ime_delnice.csv v mapi "data"), in na koncu predstavim rezultate z Jupyter Notebook. 

Podatki o delnicah, ki jih potrebujem so dostopni na spletni strani [Yahoo Finance](https://finance.yahoo.com/). Programe za pridobitev, ureditev ter analizo podatkov napišem v ločene datoteke .py, v Jupyter Notebook-u pa kličem in poganjam funkcije iz teh datotek, da je vse skupaj bolj pregledno.
 
## UPORABNOST IN NAVODILA ZA UPORABO
V datoteki pridobitev_podatkov.py se nahaja program, ki je namenjen pridobitvi podatkov izključno s spletne strani [Yahoo Finance](https://finance.yahoo.com/). Čeprav se v Jupyter Notebook-u nahajajo ugotovitve in rezultati za mojo izbiro delnic in opazovanega obdobja, si lahko uporabnik na začetku Jupyter Notebook-a izbere svoj interval in svoj nabor delnic, le paziti mora, da zapiše datum v pravilnem formatu ter, da se na spletni strani [Yahoo Finance](https://finance.yahoo.com/) prepriča o pravilnih oznakah delnic podjetij. Seveda rezultati analize za druga podjetja ne bojo relevantni, a vendar dobi kar nekaj izračunov in vizualizacij gibanja cen, vrednosti podjetja itd. s katerimi lahko potem sam naredi analizo ter predstavi rezultate.  
Torej, ko uporabnik prenese vse potrebne datoteke .py in glavno datoteko projekta .ipynb, mora v primeru, da še ni namestil vseh potrebnih paketov, storiti še to.  
Uporabil, sem naslednje pakete: `yfinance`, `pandas`, `matplotlib.pyplot`, `math`, `plotly.express`, `os` in `numpy`. Ko uporabnik naloži potrebno, lahko požene program, ki se nahaja v datoteki rezultati.ipynb. 