import tkinter as tk
import sys
import random
from tkinter import messagebox as messagebox

root_pvc = tk.Tk()

tablica_na_guziki = []
numer_guzika = 0
wybor_bota = 10
tablica_ruchow_gracza = []
tablica_ruchow_AI = []

zwycieskie_pozycje=[{0,1,2}, {3,4,5}, {6,7,8},  
                    {0,3,6}, {1,4,7}, {2,5,8},  
                    {0,4,8}, {2,4,6}]          

zwycieskie_z_brakiem=[{0, 1}, {0, 2}, {1, 2}, 
                    {3, 4}, {3, 5}, {4, 5}, 
                    {6, 7}, {6, 8}, {7, 8}, 
                    {0, 3}, {0, 6}, {3, 6}, 
                    {1, 4}, {1, 7}, {4, 7}, 
                    {2, 5}, {2, 8}, {5, 8}, 
                    {0, 4}, {0, 8}, {4, 8}, 
                    {2, 4}, {2, 6}, {4, 6}]

full_pozycje = {0,1,2,3,4,5,6,7,8}

def znajdz_brak():
    ai_set = set(tablica_ruchow_AI)
    gracz_set = set(tablica_ruchow_gracza)
    for element in zwycieskie_z_brakiem:
        if element.issubset(ai_set):
            for element_zp in zwycieskie_pozycje:
                if element.issubset(element_zp):
                    brakujace = element_zp - element - ai_set - gracz_set
                    if brakujace:
                        return brakujace.pop()
    return 10

def tworzenie_guzikow():
    global numer_guzika,tablica_na_guziki
    for i in range(3):
        for j in range(3):
            guzik = tk.Button(root_pvc, text='', command=lambda num=numer_guzika: nacisniecie_guzika(num), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
            guzik.grid(row=i, column=j, padx=10, pady=10)
            tablica_na_guziki.append(guzik)
            numer_guzika = numer_guzika + 1
    bRESET = tk.Button(root_pvc, text='RESET', command=fun_reset, width=10, height=1, font=("Arial", 20), bg="#FF6961", relief="raised")
    bRESET.grid(row=3, column=1, pady=10)

def weryfikacja_powtorzen(nowa):
    for element in tablica_ruchow_gracza:
        if nowa == element:
            return 1
    for element in tablica_ruchow_AI:
        if nowa == element:
            return 1
    else:
        return 0

def czy_wygrana():
    for element in zwycieskie_pozycje:
        if(element.issubset(set(tablica_ruchow_gracza))):
            return 'gracz_win'
        if(element.issubset(set(tablica_ruchow_AI))):
            return 'bot_win'
        if(set(tablica_ruchow_AI).union(set(tablica_ruchow_gracza)) == full_pozycje):
            return 'remis'
        

def fun_reset():
    global tablica_na_guziki,numer_guzika,tablica_ruchow_AI,tablica_ruchow_gracza
    tablica_na_guziki = []
    numer_guzika = 0
    tablica_ruchow_gracza = []
    tablica_ruchow_AI = []
    tworzenie_guzikow()


def ruch_bota():
    if ( 0<= znajdz_brak() <=8 ):
        wylosowana = znajdz_brak()
    else:
        wylosowana = random.randint(0,8)
    while True:  
            if weryfikacja_powtorzen(wylosowana) == 0:
                tablica_na_guziki[wylosowana].config(text='⭕')
                tablica_ruchow_AI.append(wylosowana)
                if czy_wygrana() == 'bot_win':
                    mess = messagebox.askyesno('KONIEC','BOT Wygrał\nCzy chcesz grać dalej?')
                    if mess == True:
                        fun_reset()
                    else:
                        sys.exit(0)
                break
            else:
                if ( 0<= znajdz_brak() <=8 ):
                    wylosowana = znajdz_brak()
                else:
                    wylosowana = random.randint(0,8)


def nacisniecie_guzika(numer_guz):
    if weryfikacja_powtorzen(numer_guz) == 0:
        tablica_na_guziki[numer_guz].config(text='❌')
        tablica_ruchow_gracza.append(numer_guz)
        if czy_wygrana() == 'gracz_win':
            mess = messagebox.askyesno('KONIEC','GRACZ Wygrał\nCzy chcesz grać dalej?')
            if mess == True:
                fun_reset()
            else:
                sys.exit(0)
        if czy_wygrana() == 'remis':
            return
        ruch_bota()     
    else:
        messagebox.showwarning('UWAGA','Nie możesz wybrać zajętego pola!')
    print('tablica gracza : ',tablica_ruchow_gracza)
    print('tablica bota : ',tablica_ruchow_AI)
    
tworzenie_guzikow()
root_pvc.mainloop()