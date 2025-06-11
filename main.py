import tkinter as tk

root_main = tk.Tk()
root_main.geometry('700x400')
root_main.title("Tic Tac Toe")

frame = tk.Frame(root_main)
frame.place(relx=0.5, rely=0.5, anchor='center')

def open_PvP_mode():
    import tic_tac_toe_PvP

def open_PvC_mode():
    import tic_tac_toe_PvC

b_pvc = tk.Button(frame, text="Player VS Computer", command=open_PvC_mode, width=20, height=1, font=("Arial", 40), bg="#FF0000", relief="raised")
b_pvc.grid(row=0, column=0)

b_pvp = tk.Button(frame, text="Player VS Player", command=open_PvP_mode, width=20, height=1, font=("Arial", 40), bg="#FF0000", relief="raised")
b_pvp.grid(row=1, column=0)

root_main.mainloop()