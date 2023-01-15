import tkinter as tk
from tkinter import Checkbutton


# Add task function
def add_task(entry, text, checkboxes, root):
    # Get the text entered in the text box
    task = entry.get()
    # Create a checkbox for the task
    checkbox = Checkbutton(root, text="")
    # Add the checkbox to the list of checkboxes
    checkboxes.append(checkbox)
    checkbox.pack(side="left")
    # Add the text to the "to-do" list
    text.insert(tk.END, task + "\n")
    

# Delete task function
def delete_task(text, checkboxes):
    # Get the selected text in the "to-do" list
    task = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    # Remove the text from the list
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)
    # Remove the checkbox from the list of checkboxes
    index = text.index(tk.SEL_FIRST)
    checkboxes.pop(index)

# Mark task as done function
def mark_done(text, checkboxes):
    # Get the selected text in the "to-do" list
    task = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    # Remove the text from the list
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)
    # Get the checkbox
    index = text.index(tk.SEL_FIRST)
    checkbox = checkboxes.pop(index)
    # deselect the checkbox 
    checkbox.deselect()
    # Add the text to the "done" list
    text.insert(tk.END, task + "\n", "done")