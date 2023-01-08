import tkinter as tk
from functions import add_task, delete_task, mark_done

#Create the main window of the application using tkinder
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")

# Create a text box to enter new "to-do" items
entry = tk.Entry(root)
entry.pack()

# Create a button to add items to the list
button = tk.Button(root, text="Add")
button.pack()

# Create a text widget to display the "to-do" list
text = tk.Text(root)
text.pack()

# Create a button to delete selected items from the list
delete_button = tk.Button(root, text="Delete")
delete_button.pack()

# Create a button to mark items as completed
done_button = tk.Button(root, text="Done")
done_button.pack()

# Create a "done" style for the text in the "completed" list
text.tag_configure("done", foreground="#666666")

# Bind the "add_task" function to the "Add" button
button.bind("<Button-1>", lambda event: add_task(entry, text))

# Bind the "delete_task" function to the "Delete" button
delete_button.bind("<Button-1>", lambda event: delete_task(text))

# Bind the "mark_done" function to the "Done" button
done_button.bind("<Button-1>", lambda event: mark_done(text))

root.mainloop()

