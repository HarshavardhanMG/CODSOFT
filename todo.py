import tkinter as tk
from tkinter import ttk, simpledialog

class DoList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Do List")

        self.create_widgets()

    def create_widgets(self):
        self.tasks = ttk.Treeview(self, columns=('Details'))
        self.tasks.heading('#0', text='Tasks')
        self.tasks.heading('#1', text='Details')
        self.tasks.pack(fill=tk.BOTH, expand=True)

        self.tasks.bind('<Double-1>', self.on_double_click)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X)

        self.add_button = ttk.Button(self.button_frame, text='Add', command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.remove_button = ttk.Button(self.button_frame, text='Remove', command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT)

        self.edit_button = ttk.Button(self.button_frame, text='Edit', command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT)

    def add_task(self):
        task_name = simpledialog.askstring('Add Task', 'Enter task name:')
        if task_name:
            self.tasks.insert('', 'end', text=task_name, values=('',))

    def remove_task(self):
        selected_item = self.tasks.selection()
        if selected_item:
            self.tasks.delete(selected_item)

    def edit_task(self):
        selected_item = self.tasks.selection()
        if selected_item:
            task_name = simpledialog.askstring('Edit Task', 'Enter new task name:')
            if task_name:
                self.tasks.item(selected_item, text=task_name)

    def on_double_click(self, event):
        selected_item = self.tasks.selection()
        if selected_item:
            task_details = simpledialog.askstring('Task Details', 'Enter task details:')
            if task_details:
                self.tasks.item(selected_item, values=(task_details,))

if __name__ == "__main__":
    app = DoList()
    app.mainloop()