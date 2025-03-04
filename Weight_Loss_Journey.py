import os 
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import datetime
import matplotlib.pyplot as plt


history_dates =[] #initializam o listă goala history_dates pentru a stoca datele(zi/luna/ora) în istoric
history_bmi =[]   #initializam o listă goala history_bmi pentru a stoca valorile BMI în istoric



def validate_input(greutate, inaltime):
    try:
        greutate = float(greutate)
        inaltime = float(inaltime)
        if greutate > 0 and inaltime > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def calcul_bmi(greutate, inaltime, sex):
    if not validate_input(greutate, inaltime):
        messagebox.showwarning("Date Invalide", "Introduceți greutatea și înălțimea corect.")
        return

    greutate = float(greutate)
    inaltime = float(inaltime)

    bmi = greutate / ((inaltime / 100) ** 2)
    messagebox.showinfo("BMI", f"BMI-ul tău este {bmi:.2f}")

    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history_dates.append(current_date) #se salveaza data curenta si BMI in istoric
    history_bmi.append(bmi)

    if sex == "masculin" or sex == "feminin":
        if bmi < 18.5:
            recomandare = "Ai nevoie să te îngrași."
        elif 18.5 <= bmi < 24.9:    #https://www.usz.ch/en/bmi-calculator/
            recomandare = "Greutatea ta este în parametrii normali."
        else:
            recomandare = "Ai nevoie să slăbești."
    else:
        recomandare = "Sex necunoscut."

    messagebox.showinfo("Recomandare", recomandare)

    try:
        os.startfile(r"C:\Users\ASUS\Desktop\data1.xlsx")
    except Exception as e:
        messagebox.showerror("Eroare", f"A apărut o eroare la deschiderea fișierului Excel: {str(e)}")

def plot_bmi_history():
    plt.plot(history_dates, history_bmi)
    plt.xlabel('Data')
    plt.ylabel('BMI')
    plt.title('Evoluția BMI-ului')
    plt.show()

root = tk.Tk()
root.title("Plan Alimentar")
root.geometry("400x350")  
root.configure(bg="magenta")  

label_greutate = tk.Label(root, text="Greutate (kg):", bg="magenta", fg="black")
label_greutate.pack()
entry_greutate = tk.Entry(root)
entry_greutate.pack()

label_inaltime = tk.Label(root, text="Înălțime (cm):", bg="magenta", fg="black")
label_inaltime.pack()
entry_inaltime = tk.Entry(root)
entry_inaltime.pack()

label_sex = tk.Label(root, text="Sex:", bg="magenta", fg="black")
label_sex.pack()
optiuni_sex = ["masculin", "feminin"]
sex_var = tk.StringVar(root)
sex_var.set(optiuni_sex[0])
sex_dropdown = tk.OptionMenu(root, sex_var, *optiuni_sex)
sex_dropdown.pack()

buton_bmi = tk.Button(root, text="Calcul BMI", command=lambda: calcul_bmi(entry_greutate.get(), entry_inaltime.get(), sex_var.get()), bg="#FFC0CB", fg="black", relief="flat", width=10)
buton_bmi.pack()

buton_istoric = tk.Button(root, text="Afișare Istoric BMI", command=plot_bmi_history, bg="#FFC0CB", fg="black", relief="flat", width=20)
buton_istoric.pack()

root.mainloop()
