import tkinter as tk
import tkinter.messagebox as messagebox
import sys


root_pvp = tk.Tk()
root_pvp.title("Tic Tac Toe")

zwycieskie_pozycje = [{1,2,3},{4,5,6},{7,8,9},
                    {1,4,7},{2,5,8},{3,6,9},
                    {1,5,9},{3,5,7}]


tablicaGracza_N = []
tablicaGracza_C = []
parametr_zmiany_c_n = 0

def weryfikacja_powtorzen(nowa):
    for element in tablicaGracza_N:
        if nowa == element:
            return 1
    for element in tablicaGracza_C:
        if nowa == element:
            return 1
    else:
        return 0

def reset_gry():
    global tablicaGracza_C, tablicaGracza_N, tworzenie_guzikow
    tablicaGracza_N = []
    tablicaGracza_C = []
    tworzenie_guzikow()

def czy_wygrana():
    global koniec_y_n, tablicaGracza_C, tablicaGracza_N
    for element in zwycieskie_pozycje:
        if(element.issubset(set(tablicaGracza_N))):
            print("gracz ⭕ wygrał!")
            odp = messagebox.askyesno('Koniec gry', '⭕ WYGRAŁ\nCzy chcesz zagrać jeszcze raz?')
            if odp == True:
                reset_gry()
            else:
                sys.exit(0)

        if(element.issubset(set(tablicaGracza_C))):
            print("gracz ❌ wygrał!")
            odp = messagebox.askyesno('Koniec gry', '❌ WYGRAŁ\nCzy chcesz zagrać jeszcze raz?')
            if odp == True:
                reset_gry()
            else:
                sys.exit(0)
            

def ruch_c_lub_n(poleX,numer_do_dodania):
    global parametr_zmiany_c_n, tablicaGracza_C, tablicaGracza_N
    
    if (weryfikacja_powtorzen(numer_do_dodania)==0):
        if (parametr_zmiany_c_n % 2 == 0):
            poleX.config(text='❌')
            tablicaGracza_C.append(numer_do_dodania)
            print(tablicaGracza_C)
            parametr_zmiany_c_n = parametr_zmiany_c_n + 1
            czy_wygrana()
    
        else:
            poleX.config(text='⭕')
            tablicaGracza_N.append(numer_do_dodania)
            print(tablicaGracza_N)
            parametr_zmiany_c_n = parametr_zmiany_c_n + 1
            czy_wygrana()
    else:
        messagebox.showwarning('UWAGA','Nie możesz wybrać zajętego pola!')

def tworzenie_guzikow():
    pole1 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole1, 1), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole1.grid(row=0, column=0, padx=10, pady=10)

    pole2 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole2, 2), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole2.grid(row=0, column=1, padx=10, pady=10)

    pole3 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole3, 3), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole3.grid(row=0, column=2, padx=10, pady=10)

    pole4 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole4, 4), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole4.grid(row=1, column=0, padx=10, pady=10)

    pole5 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole5, 5), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole5.grid(row=1, column=1, padx=10, pady=10)

    pole6 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole6, 6), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole6.grid(row=1, column=2, padx=10, pady=10)

    pole7 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole7, 7), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole7.grid(row=2, column=0, padx=10, pady=10)

    pole8 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole8, 8), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole8.grid(row=2, column=1, padx=10, pady=10)

    pole9 = tk.Button(root_pvp, text=" ", command=lambda: ruch_c_lub_n(pole9, 9), width=6, height=1, font=("Arial", 40), bg="#FFFFFF", relief="raised")
    pole9.grid(row=2, column=2, padx=10, pady=10)

    bRESET = tk.Button(root_pvp, text='RESET', command=reset_gry, width=10, height=1, font=("Arial", 20), bg="#FF6961", relief="raised")
    bRESET.grid(row=3, column=1, pady=10)

tworzenie_guzikow()
root_pvp.mainloop()