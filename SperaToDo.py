import tkinter as tk

class TodoApp:
    def __init__(self):
        # Create the main window of the application using tkinder
        self.root = tk.Tk()
        self.root.iconbitmap("D:\Spera\Progetti\ToDoList\media\mark.ico")
        self.root.title("Spera To-Do List")
        self.root.geometry("500x600")

        # Create a list to store the checkboxes
        self.checkboxes = []
        # Create a text box to enter new "to-do" items
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        # Create a button to add items to the list
        self.button = tk.Button(self.root, text="Add", command=self.add_task)
        self.button.pack()
        # Create a text widget to display the "to-do" list
        self.text = tk.Text(self.root)
        self.text.pack()
        # Create a button to delete selected items from the list
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_task)
        self.delete_button.pack()
        # Create a button to mark items as completed
        self.done_button = tk.Button(self.root, text="Done", command=self.mark_done)
        self.done_button.pack()
        # Create a "done" style for the text in the "completed" list
        self.text.tag_configure("done", foreground="#666666")
        # Bind the "delete_task" function to the "Delete" button
        self.text.bind("<Button-3>", lambda event: self.delete_task())
        # Bind the "mark_done" function to the "Done" button
        self.text.bind("<Button-3>", lambda event: self.mark_done())

    def add_task(self):
        """
        Add task in the "to-do" list
        """
        task = self.entry.get()
        frame = tk.Frame(self.text)
        cb = tk.Checkbutton(frame)
        cb.grid(row=0, column=0)
        self.checkboxes.append(cb)
        t = tk.Label(frame, text=task)
        t.grid(row=0, column=1)
        frame.grid(row=self.num_of_tasks, column=0, columnspan=2)
        self.num_of_tasks += 1


    def delete_task(self):
        """
        Delete a selected task from the "to-do" list
        """
        task = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def mark_done(self):
        """
        Mark a selected task as done
        """
        task = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.insert(tk.END, task + "\n", "done")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TodoApp()
    app.run()




# from functions import add_task, delete_task, mark_done

# # Create a list to store the checkboxes for each task
# checkboxes = []

# #Create the main window of the application using tkinder
# root = tk.Tk()
# root.iconbitmap("D:\Spera\Progetti\ToDoList\media\mark.ico")
# root.title("Spera To-Do List")
# root.geometry("500x600")

# # Create a text box to enter new "to-do" items
# entry = tk.Entry(root)
# entry.pack()

# # Create a text widget to display the "to-do" list
# text = tk.Text(root)
# text.pack()

# # Create a button to add items to the list
# button = tk.Button(root, text="Add")
# button.pack()

# # Create a button to delete selected items from the list
# delete_button = tk.Button(root, text="Delete")
# delete_button.pack()

# # Create a button to mark items as completed
# done_button = tk.Button(root, text="Done")
# done_button.pack()

# # Create a "done" style for the text in the "completed" list
# text.tag_configure("done", foreground="#666666")

# # Bind the "add_task" function to the "Add" button
# button.bind("<Button-1>", lambda event: add_task(entry, text))

# # Bind the "delete_task" function to the "Delete" button
# delete_button.bind("<Button-1>", lambda event: delete_task(text))

# # Bind the "mark_done" function to the "Done" button
# done_button.bind("<Button-1>", lambda event: mark_done(text))

# root.mainloop()

