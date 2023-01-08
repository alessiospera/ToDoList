import tkinter as tk

def add_task(entry, text):
    # Prendi il testo inserito nella casella di testo
    task = entry.get()
    # Aggiungi il testo alla lista di "to-do"
    text.insert(tk.END, task + "\n")

def delete_task(text):
    # Prendi il testo selezionato nella lista di "to-do"
    task = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    # Rimuovi il testo dalla lista
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)



def mark_done(text):
    # Prendi il testo selezionato nella lista di "to-do"
    task = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    # Rimuovi il testo dalla lista
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)
    # Aggiungi il testo alla lista di "completate"
    text.insert(tk.END, task + "\n", "done")