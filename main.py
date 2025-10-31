import tkinter as tk
import database as db
from tkinter import ttk
from datetime import datetime
import productivity_gui

db = db.Database()
#
# data = db.query_data_all()
#
#
#
# root = tk.Tk()
# root.geometry('1500x750')
#
# frame = tk.Frame(root)
# frame.pack()
#
# label = ttk.Label(frame, text="THIS IS A LABEL")
# label.pack()
#
# tree = ttk.Treeview(frame)
# tree.pack()
#
# tree["columns"] = ("Activity", "Context")
# tree.column("#0", minwidth=100)  # #0 = special "tree" column
# tree.column("Activity", width=100, anchor="center")
# tree.column("Context", width=120, anchor="w")
#
# # Define headings
# tree.heading("#0", text="Time", anchor="w")
# tree.heading("Activity", text="Activity")
# tree.heading("Context", text="Context")
#
# time = datetime.time(datetime.now())
#
# # Insert data
# for item in data:
#     tree.insert("", "end", text=item[0], values=(item[1], item[2]))
#
#
# root.mainloop()

productivity_gui.ProductivityGUI(db)
