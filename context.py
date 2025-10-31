import tkinter as tk
import tkinter.ttk as ttk
import database as db

db = db.Database()

def
root = tk.Tk()
root.title("CHECK IN")
root.geometry("500x500")

frame = tk.Frame(root)
frame.pack(anchor="center")

label = tk.Label(frame, text="Please Enter Activity")
label.grid(column=0, row=0)


activity = tk.Entry(frame, width=50)
activity.grid(column=0, row=1)

context = tk.Entry(frame, width=50)
context.grid(column=0, row=2)

submit_button = tk.Button(frame, text="Enter", command=lambda: db.insert_data([activity.get(), context.get()]))
submit_button.grid(column=0, row=3)

print_button = tk.Button(frame, text="Print", command=lambda: print(db.query_data_all()))
print_button.grid(column=0, row=4)

delete_button = ttk.Button(frame, text="NUCLEAR BUTTON", command=db.clear_database)
delete_button.grid(column=0, row=5)

root.mainloop()