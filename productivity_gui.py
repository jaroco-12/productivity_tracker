import tkinter as tk
from tkinter import ttk

from database import Database


class ProductivityGUI():
    def __init__(self, database):
        self.db = database
        self.data_tree = None
        self.entry_window = None
        self.root = tk.Tk()
        self._main_window()



    def _main_window(self):
        self.root.geometry('1000x500')
        self.root.title('Productivity Tracker')
        self.root.anchor("center")


        self._main_header()
        self._tree_log()

        ttk.Button(self.root, text="Add Entry", command=self._open_entry_window).grid(column=0, row=2)


        self.root.mainloop()

    def _main_header(self):
        ttk.Label(self.root, text='Productivity Tracker', font=("Ariel", 16, "bold")).grid(column=0, row=0)

    def _tree_log(self):
        self.data_tree = ttk.Treeview(self.root)
        self.data_tree.grid(column=0, row=1)
        self.data_tree["columns"] = ("Activity", "Context")
        self.data_tree.column("#0", minwidth=50)  # #0 = special "tree" column
        self.data_tree.column("Activity", width=200, anchor="w")
        self.data_tree.column("Context", width=250, anchor="w")

        self.data_tree.heading("#0", text="Time", anchor="w")
        self.data_tree.heading("Activity", text="Activity")
        self.data_tree.heading("Context", text="Context")
        self._update_tree()


    def _open_entry_window(self):

        if self.entry_window and self.entry_window.winfo_exists():
            self.entry_window.lift()
            self.entry_window.focus()
            return

        entry_root = tk.Toplevel(self.root)
        self.entry_window = entry_root
        entry_root.geometry('500x500')
        entry_root.title('Entry')
        ttk.Label(entry_root, text="Enter Activity Name").grid(column=0, row=0)
        ttk.Label(entry_root, text="Enter Context Name").grid(column=0, row=1)

        activity = ttk.Entry(entry_root)
        context = ttk.Entry(entry_root)
        activity.grid(column=1, row=0)
        context.grid(column=1, row=1)

        submit = ttk.Button(entry_root, text="Submit", command=lambda: (self.db.insert_data([activity.get(), context.get()]), (entry_root.destroy()), self._update_tree()))
        submit.grid(column=0, row=2)


        return
    def _update_tree(self):
        if self.data_tree:
            self.data_tree.delete(*self.data_tree.get_children())

        data = self.db.query_data_all()
        for row in data:
            self.data_tree.insert('', 'end', text=row[0], values=(row[1], row[2]))


if __name__ == '__main__':
    database = Database()
    productivity = ProductivityGUI(database)