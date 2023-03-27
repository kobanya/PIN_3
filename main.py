'''
NB-2023.03.27

Írj egy kódot, amely az előre rögzített PIN  Megadására biztosít 3 lehetőséget.
Amennyiben azt eltalálod, vagy 3 alkalommal hibás PIN-t adsz meg a BEVITEL gomb eltűnik
'''

import tkinter as tk
import tkinter.messagebox as messagebox

PIN = "2023"

def check_PIN():
    global attempts
    attempts += 1
    if attempts < 4:
        proba = pin_entry.get()
        if proba == PIN:
            #messagebox.showinfo("Siker", "Helyes PIN-kód")
            pin_entry.delete(0, tk.END)
            attempts = 0
            button.grid_forget()
            vege_label.config(text="HELYES PIN",fg="green")
        else:
            messagebox.showerror("Hiba", f"Helytelen PIN-kód. {3-attempts} próbálkozásod maradt.")
            pin_entry.delete(0, tk.END)
            if attempts == 3:
                button.grid_forget()
                vege_label.config(text="Nincs több lehetőséged!!",fg="red")
    else:
        messagebox.showerror("Hiba", "Helytelen PIN-kód, nincs több próbálkozásod.")
        vege_label.config(text="Nincs több lehetőséged!!")
        pin_entry.delete(0, tk.END)

def exit_application():
    root.destroy()

root = tk.Tk()
root.title("PIN megadása")
root.geometry("300x150")
root.configure(bg='Goldenrod')

attempts = 0

pin_label = tk.Label(root, text="PIN-kód:", bg='Goldenrod', font=('Arial', 15))
pin_label.grid(row=1, column=0, padx=5, pady=5)

pin_entry = tk.Entry(root, width=5, borderwidth=2, justify="center", font=('Arial', 30))
pin_entry.grid(row=1, column=1, padx=6, pady=5)

button = tk.Button(root, text="\u2714  BEVITEL", command=check_PIN)
button.grid(row=2, column=1, padx=5, pady=5)

exit_button = tk.Button(root, text="\u274c  Kilépés", command=exit_application)
exit_button.grid(row=2, column=0, padx=5, pady=5)

vege_label = tk.Label(root, text="", bg='Goldenrod', font=('Arial', 18,'bold'))
vege_label.grid(row=3, column=0, padx=5, pady=5, columnspan=3)

root.mainloop()


